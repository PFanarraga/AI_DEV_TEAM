#!/usr/bin/env python3
"""Validate AI DEV TEAM inventories, structure, guide coverage and references."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / ".agents"
SKILLS = BASE / "skills"


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def main() -> None:
    required = [
        ROOT / "AGENTS.md", ROOT / "README.md",
        BASE / "agents", BASE / "skills", BASE / "workflows",
        BASE / "runtime" / "ORCHESTRATION.md",
        ROOT / "adapters" / "README.md",
        ROOT / "docs" / "IDE-COMPATIBILITY.md",
        ROOT / "docs" / "integrations" / "README.md",
        ROOT / "docs" / "PROJECT-BOOTSTRAP.md",
        ROOT / "prompts" / "01-configure-assistant.md",
        ROOT / "prompts" / "02-start-project.md",
        ROOT / "scripts" / "install_ai_dev_team.py",
        ROOT / "templates" / "agent-task.md",
        ROOT / "CLAUDE.md", ROOT / "GEMINI.md",
        ROOT / ".github" / "copilot-instructions.md",
        ROOT / ".cursor" / "rules" / "ai-dev-team.mdc",
        ROOT / ".junie" / "AGENTS.md",
    ]
    for path in required:
        if not path.exists():
            fail(f"Missing required path: {path.relative_to(ROOT)}")

    agents = sorted(p for p in (BASE / "agents").glob("*.md") if p.name != "README.md")
    if len(agents) != 18:
        fail(f"Expected 18 agent profiles (excluding README), found {len(agents)}")

    skills = sorted(SKILLS.rglob("SKILL.md"))
    names = [p.parent.name for p in skills]
    duplicates = sorted({n for n in names if names.count(n) > 1})
    if duplicates:
        fail("Duplicate Skill names: " + ", ".join(duplicates))
    if len(skills) != 57:
        fail(f"Expected 57 unique Skills, found {len(skills)}")

    workflows = sorted((BASE / "workflows").glob("*.md"))
    if len(workflows) != 8:
        fail(f"Expected 8 workflows, found {len(workflows)}")

    missing = []
    for agent in agents:
        for line in agent.read_text(encoding="utf-8").splitlines():
            candidate = line.removeprefix("- ").strip()
            if candidate.endswith("/SKILL.md") and not (SKILLS / candidate).is_file():
                missing.append(f"{agent.relative_to(ROOT)} -> {candidate}")
    if missing:
        fail("Missing Skill references:\\n" + "\\n".join(missing))

    guides_dir = ROOT / "docs" / "integrations"
    guides = sorted(p for p in guides_dir.glob("*.md") if p.name != "README.md")
    if len(guides) != 14:
        fail(f"Expected 14 assistant integration guides, found {len(guides)}")
    for guide in guides:
        body = guide.read_text(encoding="utf-8")
        if "Prompt base" not in body:
            fail(f"Missing assistant base prompt: {guide.relative_to(ROOT)}")
    index = (guides_dir / "README.md").read_text(encoding="utf-8")
    for guide in guides:
        if guide.name not in index:
            fail(f"Integration index missing {guide.name}")

    bootstrap = (ROOT / "docs" / "PROJECT-BOOTSTRAP.md").read_text(encoding="utf-8")
    for required_text in ("AGENTS.md", ".agents/", "Prompt 1", "Prompt 2", "--dry-run"):
        if required_text not in bootstrap:
            fail(f"Bootstrap guide missing required content: {required_text}")

    for prompt_name in ("01-configure-assistant.md", "02-start-project.md"):
        prompt = (ROOT / "prompts" / prompt_name).read_text(encoding="utf-8")
        if "AI DEV TEAM" not in prompt or "INSTRUCCIONES" not in prompt and "INSTRUCCIONES PARA EL DIRECTOR" not in prompt:
            fail(f"Prompt missing required instructions: prompts/{prompt_name}")

    for filename in ("AGENTS.md", "README.md", "TUTORIAL_MAESTRO_AI_DEV_TEAM.md"):
        path = ROOT / filename
        if not path.is_file() or ".agents/" not in path.read_text(encoding="utf-8"):
            fail(f"{filename} must document .agents/")

    print("AI DEV TEAM validation: OK")
    print(f"Agents: {len(agents)}")
    print(f"Unique Skills: {len(skills)}")
    print(f"Workflows: {len(workflows)}")
    print(f"Assistant integration guides: {len(guides)}")
    print("Assistant base prompts: OK")
    print("Project bootstrap, two-stage prompts and safe installer: OK")
    print("Agent Skill references: OK")


if __name__ == "__main__":
    main()
