import os
import subprocess
from pathlib import Path
from typing import List


class RepositoryTools:
    """
    Local repository tools used by the target coding agent.

    All file operations are restricted to repository_root.
    """

    def __init__(
        self,
        repository_root: str,
        command_timeout: int = 120,
        max_output_chars: int = 30000,
    ):
        self.root = Path(repository_root).expanduser().resolve()

        if not self.root.exists():
            raise FileNotFoundError(
                f"Repository does not exist: {self.root}"
            )

        if not self.root.is_dir():
            raise NotADirectoryError(
                f"Repository path is not a directory: {self.root}"
            )

        self.command_timeout = command_timeout
        self.max_output_chars = max_output_chars

    # ========================================================
    # Internal helpers
    # ========================================================

    def _resolve_path(self, relative_path: str) -> Path:
        """
        Resolve a path while preventing access outside the repo.
        """
        target = (self.root / relative_path).resolve()

        try:
            target.relative_to(self.root)
        except ValueError:
            raise ValueError(
                f"Path escapes repository root: {relative_path}"
            )

        return target

    def _truncate(self, text: str) -> str:
        """
        Prevent extremely large tool outputs from flooding
        the agent context.
        """
        if len(text) <= self.max_output_chars:
            return text

        return (
            text[: self.max_output_chars]
            + "\n\n...[output truncated]..."
        )

    # ========================================================
    # Tool 1: list_files
    # ========================================================

    def list_files(
        self,
        relative_path: str = ".",
        max_depth: int = 2,
    ) -> str:
        """
        List repository files/directories up to max_depth.
        """
        target = self._resolve_path(relative_path)

        if not target.exists():
            raise FileNotFoundError(
                f"Path does not exist: {relative_path}"
            )

        if not target.is_dir():
            raise NotADirectoryError(
                f"Path is not a directory: {relative_path}"
            )

        base_depth = len(target.parts)
        entries: List[str] = []

        for current_root, dirs, files in os.walk(target):
            current = Path(current_root)
            depth = len(current.parts) - base_depth

            if depth >= max_depth:
                dirs[:] = []

            # Avoid common large/unhelpful directories.
            dirs[:] = [
                d for d in dirs
                if d not in {
                    ".git",
                    ".venv",
                    "node_modules",
                    "__pycache__",
                }
            ]

            for directory in sorted(dirs):
                path = current / directory
                entries.append(
                    str(path.relative_to(self.root)) + "/"
                )

            for filename in sorted(files):
                path = current / filename
                entries.append(
                    str(path.relative_to(self.root))
                )

        return self._truncate("\n".join(entries))

    # ========================================================
    # Tool 2: read_file
    # ========================================================

    def read_file(
        self,
        relative_path: str,
        start_line: int = 1,
        end_line: int = 400,
    ) -> str:
        """
        Read a range of lines from a UTF-8 text file.
        """
        target = self._resolve_path(relative_path)

        if not target.exists():
            raise FileNotFoundError(
                f"File does not exist: {relative_path}"
            )

        if not target.is_file():
            raise IsADirectoryError(
                f"Path is not a file: {relative_path}"
            )

        if start_line < 1:
            raise ValueError("start_line must be >= 1.")

        if end_line < start_line:
            raise ValueError(
                "end_line must be >= start_line."
            )

        with target.open(
            "r",
            encoding="utf-8",
            errors="replace",
        ) as handle:
            lines = handle.readlines()

        selected = lines[start_line - 1:end_line]

        numbered = []

        for number, line in enumerate(
            selected,
            start=start_line,
        ):
            numbered.append(
                f"{number}: {line.rstrip()}"
            )

        return self._truncate("\n".join(numbered))

    # ========================================================
    # Tool 3: search_text
    # ========================================================

    def search_text(
        self,
        query: str,
        relative_path: str = ".",
        max_results: int = 100,
    ) -> str:
        """
        Search repository text using ripgrep if available.
        """
        target = self._resolve_path(relative_path)

        command = [
            "rg",
            "--line-number",
            "--no-heading",
            "--color",
            "never",
            "--max-count",
            str(max_results),
            query,
            str(target),
        ]

        try:
            completed = subprocess.run(
                command,
                cwd=str(self.root),
                capture_output=True,
                text=True,
                timeout=self.command_timeout,
            )
        except FileNotFoundError:
            raise RuntimeError(
                "ripgrep (rg) is required for search_text."
            )

        # rg return code 1 means no matches.
        if completed.returncode not in (0, 1):
            raise RuntimeError(
                "Repository search failed.\n"
                f"{completed.stderr}"
            )

        output = completed.stdout.strip()

        if not output:
            return "No matches found."

        # Convert absolute repo path back to relative paths.
        output = output.replace(
            str(self.root) + "/",
            "",
        )

        return self._truncate(output)

    # ========================================================
    # Tool 4: run_command
    # ========================================================

    def run_command(
        self,
        command: str,
    ) -> str:
        """
        Run a shell command with repository_root as cwd.

        This tool is intended for the coding-agent environment,
        where commands such as tests, builds, git status, etc.
        are required.
        """
        try:
            completed = subprocess.run(
                ["/bin/zsh", "-lc", command],
                cwd=str(self.root),
                capture_output=True,
                text=True,
                timeout=self.command_timeout,
            )
        except subprocess.TimeoutExpired:
            return (
                f"Command timed out after "
                f"{self.command_timeout} seconds."
            )

        stdout = completed.stdout.strip()
        stderr = completed.stderr.strip()

        result = (
            f"exit_code: {completed.returncode}\n"
            f"stdout:\n{stdout}\n"
            f"stderr:\n{stderr}"
        )

        return self._truncate(result)

    # ========================================================
    # Tool 5: write_file
    # ========================================================

    def write_file(
        self,
        relative_path: str,
        content: str,
    ) -> str:
        """
        Write a UTF-8 text file inside the repository.
        Parent directories are created automatically.
        """
        target = self._resolve_path(relative_path)

        target.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        target.write_text(
            content,
            encoding="utf-8",
        )

        return (
            f"Wrote {len(content)} characters to "
            f"{target.relative_to(self.root)}"
        )