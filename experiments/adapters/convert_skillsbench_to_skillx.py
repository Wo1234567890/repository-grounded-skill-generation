import argparse
import json
from pathlib import Path


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_reward(result):
    rewards = result.get("rewards")
    if isinstance(rewards, dict):
        return float(rewards.get("reward", 0.0))
    if isinstance(rewards, (int, float)):
        return float(rewards)
    return 0.0


def convert(atif, result, atif_path, result_path):
    task_id = result.get("task_name", "")
    trajectory_id = atif.get("session_id", task_id)

    history = []
    user_task = ""

    for step in atif.get("steps", []):
        source = step.get("source", "")
        message = step.get("message", "") or ""
        reasoning = step.get("reasoning_content", "") or ""

        if source == "user":
            if not user_task and message.strip():
                user_task = message

            # BenchFlow may duplicate the initial user prompt.
            if (
                history
                and history[-1].get("role") == "user"
                and history[-1].get("content") == message
            ):
                continue

            history.append({
                "role": "user",
                "content": message,
            })

        elif source == "agent":
            # Preserve the available reasoning/action text in the unified history.
            parts = []
            if reasoning.strip():
                parts.append(reasoning.strip())
            if message.strip():
                parts.append(message.strip())

            assistant_step = {
                "role": "assistant",
                "content": "\n\n".join(parts),
            }

            raw_tool_calls = step.get("tool_calls") or []
            if raw_tool_calls:
                assistant_step["tool_calls"] = [
                    {
                        "id": tc.get("tool_call_id", ""),
                        "name": tc.get("function_name", ""),
                        "arguments": tc.get("arguments", {}) or {},
                        "requestor": "assistant",
                    }
                    for tc in raw_tool_calls
                ]

            history.append(assistant_step)

            # ATIF stores tool results inside observation.
            observation = step.get("observation") or {}
            for obs in observation.get("results", []) or []:
                history.append({
                    "role": "tool",
                    "content": obs.get("content", "") or "",
                    "id": obs.get("source_call_id", ""),
                })

        elif source == "tool":
            history.append({
                "role": "tool",
                "content": message,
                "id": step.get("tool_call_id", ""),
            })

    reward = get_reward(result)

    return {
        "trajectory_id": trajectory_id,
        "benchmark": "skillsbench",
        "task_id": task_id,
        "user_task": user_task,
        "task_history": history,
        "reward": reward,
        "metadata": {
            "source": "skillsbench",
            "atif_schema_version": atif.get("schema_version"),
            "agent": atif.get("agent", {}),
            "original_atif_path": str(atif_path),
            "original_result_path": str(result_path),
            "skill_mode": result.get("skill_mode"),
            "model": result.get("model"),
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--atif", required=True)
    parser.add_argument("--result", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    atif_path = Path(args.atif)
    result_path = Path(args.result)
    output_path = Path(args.output)

    atif = load_json(atif_path)
    result = load_json(result_path)

    trajectory = convert(
        atif,
        result,
        atif_path,
        result_path,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(trajectory, ensure_ascii=False) + "\n")

    print("Created SkillX trajectory:")
    print(output_path)
    print()
    print("trajectory_id:", trajectory["trajectory_id"])
    print("task_id:", trajectory["task_id"])
    print("benchmark:", trajectory["benchmark"])
    print("reward:", trajectory["reward"])
    print("history steps:", len(trajectory["task_history"]))
    print("user task chars:", len(trajectory["user_task"]))


if __name__ == "__main__":
    main()
