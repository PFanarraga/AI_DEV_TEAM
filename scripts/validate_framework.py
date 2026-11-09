#!/usr/bin/env python3
"""Validate AI DEV TEAM structure and agent Skill references."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / ".agents"
SKILLS = BASE / "skills"


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def main() -> None:
    required = [ROOT / "AGENTS.md", ROOT / "README.md", BASE / "agents",
                BASE / "skills", BASE / "workflows", BASE / "runtime" / "ORCHESTRATION.md"]
    for path in required:
        if not path.exists():
            fail(f"Missing required path: {path.relative_to(ROOT)}")

    agents = sorted((BASE / "agents").glob("*.md"))
    if len(agents) != 12:
        fail(f"Expected 12 agents, found {len(agents)}")

    skills = sorted(SKILLS.rglob("SKILL.md"))
    names = [p.parent.name for p in skills]
    duplicates = sorted({n for n in names if names.count(n) > 1})
    if duplicates:
        fail("Duplicate Skill names: " + ", ".join(duplicates))
    if len(skills) != 41:
        fail(f"Expected 41 unique Skills, found {len(skills)}")

    workflows = sorted((BASE / "workflows").glob("*.md"))
    if len(workflows) != 5:
        fail(f"Expected 5 workflows, found {len(workflows)}")

    missing = []
    for agent in agents:
        for line in agent.read_text(encoding="utf-8").splitlines():
            candidate = line.removeprefix("- ").strip()
            if candidate.endswith("/SKILL.md") and not (SKILLS / candidate).is_file():
                missing.append(f"{agent.relative_to(ROOT)} -> {candidate}")
    if missing:
        fail("Missing Skill references:\n" + "\n".join(missing))

    for filename in ("AGENTS.md", "README.md", "TUTORIAL_MAESTRO_AI_DEV_TEAM.md"):
        p = ROOT / filename
        if not p.is_file() or ".agents/" not in p.read_text(encoding="utf-8"):
            fail(f"{filename} must document .agents/")

    print("AI DEV TEAM validation: OK")
    print(f"Agents: {len(agents)}")
    print(f"Unique Skills: {len(skills)}")
    print(f"Workflows: {len(workflows)}")
    print("Agent Skill references: OK")


if __name__ == "__main__":
    main()
