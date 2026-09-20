import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from anthropic import Anthropic
from dotenv import load_dotenv

from src.agents.base_agent import (
    AgentRunResult,
    BaseCodingAgent,
)
from src.tools.repository_tools import RepositoryTools


# ============================================================
# Environment
# ============================================================

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parents[2]
)

ENV_PATH = (
    PROJECT_ROOT
    / ".env"
)

load_dotenv(
    dotenv_path=ENV_PATH
)


# ============================================================
# Module-Level Helper
# ============================================================

def _filter_tool_definitions(
    tool_definitions: List[
        Dict[str, Any]
    ],
    allowed_names: set[str],
) -> List[
    Dict[str, Any]
]:
    """
    Select tool definitions whose names are included in
    allowed_names.

    This helper is intentionally defined outside the class.

    Python list comprehensions inside a class body use a separate
    scope, so referring directly to another class variable from a
    class-body comprehension can raise NameError.
    """

    return [
        tool
        for tool in tool_definitions
        if tool["name"]
        in allowed_names
    ]


# ============================================================
# Claude Target Coding Agent
# ============================================================

class ClaudeCodingAgent(
    BaseCodingAgent
):
    """
    API-based TARGET coding agent.

    IMPORTANT:

    This is the agent whose knowledge is being tested.

    It is separate from FixedLLMClient, which is the auxiliary LLM
    used for semantic operations such as:

        - gap discovery
        - repository retrieval planning
        - target construction
        - question generation
        - semantic verification
        - candidate matching
        - recomposition

    Every target-agent run starts with a completely fresh message
    history.

    Two execution modes are provided:

        normal
            Full coding-agent tools.

        read_only_probe
            Read-only repository tools for Stage 2 / Stage 3
            diagnostic probing.
    """

    # ========================================================
    # Full Repository Tool Definitions
    # ========================================================

    TOOL_DEFINITIONS = [
        {
            "name": "list_files",
            "description": (
                "List files and directories inside the current "
                "repository. Use this to understand repository "
                "structure before inspecting specific files."
            ),
            "input_schema": {
                "type": "object",
                "properties": {
                    "relative_path": {
                        "type": "string",
                        "description": (
                            "Path relative to repository root. "
                            "Use '.' for the repository root."
                        ),
                    },
                    "max_depth": {
                        "type": "integer",
                        "description": (
                            "Maximum directory depth to list."
                        ),
                    },
                },
                "required": [],
            },
        },

        {
            "name": "read_file",
            "description": (
                "Read a range of lines from a text file inside "
                "the current repository."
            ),
            "input_schema": {
                "type": "object",
                "properties": {
                    "relative_path": {
                        "type": "string",
                        "description": (
                            "File path relative to repository root."
                        ),
                    },
                    "start_line": {
                        "type": "integer",
                        "description": (
                            "First line to read, starting at 1."
                        ),
                    },
                    "end_line": {
                        "type": "integer",
                        "description": (
                            "Last line to read."
                        ),
                    },
                },
                "required": [
                    "relative_path",
                ],
            },
        },

        {
            "name": "search_text",
            "description": (
                "Search for text or a pattern inside repository "
                "files. Use this to locate symbols, errors, "
                "configuration values, tests, and dependencies."
            ),
            "input_schema": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": (
                            "Text or regex pattern to search for."
                        ),
                    },
                    "relative_path": {
                        "type": "string",
                        "description": (
                            "Directory or file path relative to "
                            "repository root."
                        ),
                    },
                    "max_results": {
                        "type": "integer",
                        "description": (
                            "Maximum number of matching results."
                        ),
                    },
                },
                "required": [
                    "query",
                ],
            },
        },

        {
            "name": "run_command",
            "description": (
                "Run a shell command inside the repository. "
                "Use this for tests, builds, dependency inspection, "
                "git status, and other repository-related commands."
            ),
            "input_schema": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": (
                            "Shell command to execute from the "
                            "repository root."
                        ),
                    },
                },
                "required": [
                    "command",
                ],
            },
        },

        {
            "name": "write_file",
            "description": (
                "Write or replace a UTF-8 text file inside the "
                "repository. Use this when the software engineering "
                "task requires code or configuration changes."
            ),
            "input_schema": {
                "type": "object",
                "properties": {
                    "relative_path": {
                        "type": "string",
                        "description": (
                            "File path relative to repository root."
                        ),
                    },
                    "content": {
                        "type": "string",
                        "description": (
                            "Complete new content of the file."
                        ),
                    },
                },
                "required": [
                    "relative_path",
                    "content",
                ],
            },
        },
    ]

    # ========================================================
    # Read-Only Probe Tool Definitions
    # ========================================================

    READ_ONLY_TOOL_NAMES = {
        "list_files",
        "read_file",
        "search_text",
    }

    READ_ONLY_TOOL_DEFINITIONS = (
        _filter_tool_definitions(
            TOOL_DEFINITIONS,
            READ_ONLY_TOOL_NAMES,
        )
    )

    # ========================================================
    # System Prompts
    # ========================================================

    DEFAULT_SYSTEM_PROMPT = """
You are a software engineering coding agent operating inside a
repository.

Use the available repository tools whenever needed to inspect the
codebase, understand errors, read tests and configuration, run
commands, modify files, and verify your work.

Work only within the provided repository.

When solving a software engineering task:

- inspect relevant repository evidence before making unsupported
  assumptions;

- make only changes needed for the task;

- run appropriate tests or checks when possible.

When answering a diagnostic question:

- inspect the repository when needed;

- answer the specific question directly;

- do not assume information that is not supported by the
  repository.

Do not claim that you inspected a file, test, command output, or
repository instruction unless you actually obtained it through the
available tools.
""".strip()

    READ_ONLY_PROBE_SYSTEM_PROMPT = """
You are a software engineering coding agent operating inside a
repository.

Answer the supplied repository-specific question using the task
description and repository context.

You may inspect the repository through the available tools when
needed.

The repository must remain unchanged during this run.

Answer the question directly.

Do not claim that you inspected repository information unless you
actually obtained it through an available tool.
""".strip()

    # ========================================================
    # Initialization
    # ========================================================

    def __init__(
        self,
        model: str = "claude-sonnet-4-6",
        max_turns: int = 50,
        max_tokens_per_turn: int = 4096,
        command_timeout: int = 120,
    ):
        super().__init__(
            model=model,
            max_turns=max_turns,
        )

        api_key = os.getenv(
            "ANTHROPIC_AGENT_API_KEY"
        )

        if not api_key:
            raise RuntimeError(
                "ANTHROPIC_AGENT_API_KEY was not found.\n"
                f"Expected it in: {ENV_PATH}"
            )

        self.client = Anthropic(
            api_key=api_key
        )

        self.max_tokens_per_turn = (
            max_tokens_per_turn
        )

        self.command_timeout = (
            command_timeout
        )

    # ========================================================
    # Tool Execution
    # ========================================================

    def _execute_tool(
        self,
        tools: RepositoryTools,
        tool_name: str,
        tool_input: Dict[
            str,
            Any
        ],
        allowed_tool_names: Optional[
            set[str]
        ] = None,
    ) -> Tuple[
        str,
        bool,
    ]:
        """
        Execute one repository tool.

        Returns:

            (tool_output, is_error)

        allowed_tool_names forms a hard tool permission boundary.

        For read-only probing this prevents the target agent from
        invoking run_command or write_file even if it attempts to
        request them.
        """

        # ----------------------------------------------------
        # Hard permission boundary
        # ----------------------------------------------------

        if (
            allowed_tool_names
            is not None
            and tool_name
            not in allowed_tool_names
        ):
            return (
                (
                    "PermissionError: tool is not available "
                    f"in this session: {tool_name}"
                ),
                True,
            )

        try:

            # ------------------------------------------------
            # list_files
            # ------------------------------------------------

            if (
                tool_name
                == "list_files"
            ):
                result = (
                    tools.list_files(
                        relative_path=(
                            tool_input.get(
                                "relative_path",
                                ".",
                            )
                        ),
                        max_depth=(
                            tool_input.get(
                                "max_depth",
                                2,
                            )
                        ),
                    )
                )

            # ------------------------------------------------
            # read_file
            # ------------------------------------------------

            elif (
                tool_name
                == "read_file"
            ):
                result = (
                    tools.read_file(
                        relative_path=(
                            tool_input[
                                "relative_path"
                            ]
                        ),
                        start_line=(
                            tool_input.get(
                                "start_line",
                                1,
                            )
                        ),
                        end_line=(
                            tool_input.get(
                                "end_line",
                                400,
                            )
                        ),
                    )
                )

            # ------------------------------------------------
            # search_text
            # ------------------------------------------------

            elif (
                tool_name
                == "search_text"
            ):
                result = (
                    tools.search_text(
                        query=(
                            tool_input[
                                "query"
                            ]
                        ),
                        relative_path=(
                            tool_input.get(
                                "relative_path",
                                ".",
                            )
                        ),
                        max_results=(
                            tool_input.get(
                                "max_results",
                                100,
                            )
                        ),
                    )
                )

            # ------------------------------------------------
            # run_command
            # ------------------------------------------------

            elif (
                tool_name
                == "run_command"
            ):
                result = (
                    tools.run_command(
                        command=(
                            tool_input[
                                "command"
                            ]
                        ),
                    )
                )

            # ------------------------------------------------
            # write_file
            # ------------------------------------------------

            elif (
                tool_name
                == "write_file"
            ):
                result = (
                    tools.write_file(
                        relative_path=(
                            tool_input[
                                "relative_path"
                            ]
                        ),
                        content=(
                            tool_input[
                                "content"
                            ]
                        ),
                    )
                )

            else:
                return (
                    (
                        "Unknown tool: "
                        f"{tool_name}"
                    ),
                    True,
                )

            return (
                str(
                    result
                ),
                False,
            )

        except Exception as exc:
            return (
                (
                    f"{type(exc).__name__}: "
                    f"{exc}"
                ),
                True,
            )

    # ========================================================
    # Serialization Helper
    # ========================================================

    @staticmethod
    def _serialize_block(
        block: Any,
    ) -> Dict[
        str,
        Any
    ]:
        """
        Convert an Anthropic content block into a plain dictionary.

        Plain dictionaries are used for:

            - trajectory logging
            - feeding assistant content back into later tool turns
        """

        if hasattr(
            block,
            "model_dump",
        ):
            return (
                block.model_dump()
            )

        return {
            "type": getattr(
                block,
                "type",
                "unknown",
            ),
            "text": getattr(
                block,
                "text",
                None,
            ),
        }

    # ========================================================
    # Internal Fresh Tool-Loop Session
    # ========================================================

    def _run_session(
        self,
        repository_path: str,
        prompt: str,
        system_prompt: str,
        tool_definitions: List[
            Dict[str, Any]
        ],
        allowed_tool_names: set[str],
        mode: str,
    ) -> AgentRunResult:
        """
        Run one fresh Claude coding-agent session.

        Critical experimental property:

        Every invocation creates a completely new message history.

        Therefore separate baseline trials do not share
        conversational state.
        """

        repository = (
            Path(
                repository_path
            )
            .expanduser()
            .resolve()
        )

        # ----------------------------------------------------
        # Validate repository
        # ----------------------------------------------------

        if not repository.exists():
            return (
                AgentRunResult(
                    final_answer="",
                    trajectory=[],
                    metadata={
                        "model": (
                            self.model
                        ),
                        "mode": (
                            mode
                        ),
                    },
                    success=False,
                    error=(
                        "Repository path does not exist: "
                        f"{repository}"
                    ),
                )
            )

        if not repository.is_dir():
            return (
                AgentRunResult(
                    final_answer="",
                    trajectory=[],
                    metadata={
                        "model": (
                            self.model
                        ),
                        "mode": (
                            mode
                        ),
                    },
                    success=False,
                    error=(
                        "Repository path is not a directory: "
                        f"{repository}"
                    ),
                )
            )

        repository_path = str(
            repository
        )

        tools = (
            RepositoryTools(
                repository_root=(
                    repository_path
                ),
                command_timeout=(
                    self.command_timeout
                ),
            )
        )

        # ----------------------------------------------------
        # IMPORTANT:
        #
        # Fresh context every run.
        #
        # No previous target-agent messages are reused.
        # ----------------------------------------------------

        messages: List[
            Dict[str, Any]
        ] = [
            {
                "role": (
                    "user"
                ),
                "content": (
                    prompt
                ),
            }
        ]

        trajectory: List[
            Dict[str, Any]
        ] = []

        latest_text_answer = ""

        total_input_tokens = 0
        total_output_tokens = 0

        try:

            for turn_index in range(
                1,
                self.max_turns + 1,
            ):

                # ============================================
                # Target-Agent API Call
                # ============================================

                response = (
                    self.client.messages.create(
                        model=(
                            self.model
                        ),
                        max_tokens=(
                            self.max_tokens_per_turn
                        ),
                        system=(
                            system_prompt
                        ),
                        tools=(
                            tool_definitions
                        ),
                        messages=(
                            messages
                        ),
                    )
                )

                # ============================================
                # Usage
                # ============================================

                usage = getattr(
                    response,
                    "usage",
                    None,
                )

                if (
                    usage
                    is not None
                ):
                    total_input_tokens += int(
                        getattr(
                            usage,
                            "input_tokens",
                            0,
                        )
                        or 0
                    )

                    total_output_tokens += int(
                        getattr(
                            usage,
                            "output_tokens",
                            0,
                        )
                        or 0
                    )

                # ============================================
                # Serialize Assistant Content
                # ============================================

                serialized_content = [
                    self._serialize_block(
                        block
                    )
                    for block
                    in response.content
                ]

                trajectory.append(
                    {
                        "turn": (
                            turn_index
                        ),
                        "event": (
                            "assistant"
                        ),
                        "content": (
                            serialized_content
                        ),
                        "stop_reason": (
                            response.stop_reason
                        ),
                    }
                )

                # Add assistant output to tool-loop history.
                messages.append(
                    {
                        "role": (
                            "assistant"
                        ),
                        "content": (
                            serialized_content
                        ),
                    }
                )

                # ============================================
                # Collect Text and Tool Calls
                # ============================================

                text_parts: List[
                    str
                ] = []

                tool_blocks: List[
                    Any
                ] = []

                for block in (
                    response.content
                ):

                    block_type = getattr(
                        block,
                        "type",
                        None,
                    )

                    if (
                        block_type
                        == "text"
                    ):
                        block_text = (
                            getattr(
                                block,
                                "text",
                                "",
                            )
                            or ""
                        )

                        if (
                            block_text.strip()
                        ):
                            text_parts.append(
                                block_text
                            )

                    elif (
                        block_type
                        == "tool_use"
                    ):
                        tool_blocks.append(
                            block
                        )

                if text_parts:
                    latest_text_answer = (
                        "\n".join(
                            text_parts
                        )
                        .strip()
                    )

                # ============================================
                # No Tool Calls -> Final Answer
                # ============================================

                if not tool_blocks:

                    return (
                        AgentRunResult(
                            final_answer=(
                                latest_text_answer
                            ),
                            trajectory=(
                                trajectory
                            ),
                            metadata={
                                "model": (
                                    self.model
                                ),
                                "mode": (
                                    mode
                                ),
                                "turns": (
                                    turn_index
                                ),
                                "input_tokens": (
                                    total_input_tokens
                                ),
                                "output_tokens": (
                                    total_output_tokens
                                ),
                                "allowed_tools": (
                                    sorted(
                                        allowed_tool_names
                                    )
                                ),
                            },
                            success=True,
                            error=None,
                        )
                    )

                # ============================================
                # Execute Requested Tools
                # ============================================

                tool_results: List[
                    Dict[str, Any]
                ] = []

                for block in (
                    tool_blocks
                ):

                    tool_name = str(
                        getattr(
                            block,
                            "name",
                            "",
                        )
                    )

                    raw_tool_input = (
                        getattr(
                            block,
                            "input",
                            {},
                        )
                    )

                    if isinstance(
                        raw_tool_input,
                        dict,
                    ):
                        tool_input = (
                            raw_tool_input
                        )

                    else:
                        try:
                            tool_input = dict(
                                raw_tool_input
                            )

                        except Exception:
                            tool_input = {}

                    (
                        tool_output,
                        is_error,
                    ) = (
                        self._execute_tool(
                            tools=(
                                tools
                            ),
                            tool_name=(
                                tool_name
                            ),
                            tool_input=(
                                tool_input
                            ),
                            allowed_tool_names=(
                                allowed_tool_names
                            ),
                        )
                    )

                    # ----------------------------------------
                    # Record actual target-agent tool use
                    # ----------------------------------------

                    trajectory.append(
                        {
                            "turn": (
                                turn_index
                            ),
                            "event": (
                                "tool"
                            ),
                            "tool_name": (
                                tool_name
                            ),
                            "tool_input": (
                                tool_input
                            ),
                            "tool_output": (
                                tool_output
                            ),
                            "is_error": (
                                is_error
                            ),
                        }
                    )

                    # ----------------------------------------
                    # Tool result returned to Claude
                    # ----------------------------------------

                    tool_results.append(
                        {
                            "type": (
                                "tool_result"
                            ),
                            "tool_use_id": (
                                block.id
                            ),
                            "content": (
                                tool_output
                            ),
                            "is_error": (
                                is_error
                            ),
                        }
                    )

                messages.append(
                    {
                        "role": (
                            "user"
                        ),
                        "content": (
                            tool_results
                        ),
                    }
                )

            # =================================================
            # Max Turns Reached
            # =================================================

            return (
                AgentRunResult(
                    final_answer=(
                        latest_text_answer
                    ),
                    trajectory=(
                        trajectory
                    ),
                    metadata={
                        "model": (
                            self.model
                        ),
                        "mode": (
                            mode
                        ),
                        "turns": (
                            self.max_turns
                        ),
                        "input_tokens": (
                            total_input_tokens
                        ),
                        "output_tokens": (
                            total_output_tokens
                        ),
                        "allowed_tools": (
                            sorted(
                                allowed_tool_names
                            )
                        ),
                    },
                    success=False,
                    error=(
                        "Maximum target-agent turn "
                        "limit reached."
                    ),
                )
            )

        except Exception as exc:

            return (
                AgentRunResult(
                    final_answer=(
                        latest_text_answer
                    ),
                    trajectory=(
                        trajectory
                    ),
                    metadata={
                        "model": (
                            self.model
                        ),
                        "mode": (
                            mode
                        ),
                        "input_tokens": (
                            total_input_tokens
                        ),
                        "output_tokens": (
                            total_output_tokens
                        ),
                        "allowed_tools": (
                            sorted(
                                allowed_tool_names
                            )
                        ),
                    },
                    success=False,
                    error=(
                        f"{type(exc).__name__}: "
                        f"{exc}"
                    ),
                )
            )

    # ========================================================
    # BaseCodingAgent Required Implementation
    # ========================================================

    def run_fresh_session(
        self,
        repository_path: str,
        prompt: str,
        system_prompt: Optional[
            str
        ] = None,
    ) -> AgentRunResult:
        """
        Run one NORMAL fresh target-agent session.

        Used for the original no-skill software-engineering task.

        Available tools:

            list_files
            read_file
            search_text
            run_command
            write_file
        """

        if (
            system_prompt
            is None
        ):
            system_prompt = (
                self.DEFAULT_SYSTEM_PROMPT
            )

        full_tool_names = {
            tool["name"]
            for tool
            in self.TOOL_DEFINITIONS
        }

        return (
            self._run_session(
                repository_path=(
                    repository_path
                ),
                prompt=(
                    prompt
                ),
                system_prompt=(
                    system_prompt
                ),
                tool_definitions=(
                    self.TOOL_DEFINITIONS
                ),
                allowed_tool_names=(
                    full_tool_names
                ),
                mode=(
                    "normal"
                ),
            )
        )

    # ========================================================
    # Read-Only Fresh Probe Session
    # ========================================================

    def run_read_only_fresh_session(
        self,
        repository_path: str,
        prompt: str,
        system_prompt: Optional[
            str
        ] = None,
    ) -> AgentRunResult:
        """
        Run one completely fresh READ-ONLY target-agent session.

        Intended for:

            Stage 2 baseline probing
            Stage 3 intervention probing

        Available repository tools:

            list_files
            read_file
            search_text

        NOT available:

            run_command
            write_file

        Therefore diagnostic probing cannot alter the repository
        through the target-agent tool interface.
        """

        if (
            system_prompt
            is None
        ):
            system_prompt = (
                self.READ_ONLY_PROBE_SYSTEM_PROMPT
            )

        return (
            self._run_session(
                repository_path=(
                    repository_path
                ),
                prompt=(
                    prompt
                ),
                system_prompt=(
                    system_prompt
                ),
                tool_definitions=(
                    self.READ_ONLY_TOOL_DEFINITIONS
                ),
                allowed_tool_names=(
                    set(
                        self.READ_ONLY_TOOL_NAMES
                    )
                ),
                mode=(
                    "read_only_probe"
                ),
            )
        )