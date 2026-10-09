#!/usr/bin/env python3
"""Check generated adapters, required files, local links and YAML headers."""
from pathlib import Path
import re
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(ROOT / "scripts/build.py"), "--check"], check=True)
required = ["LICENSE", "README.md", "AGENTS.md", "CONTRIBUTING.md", "VERSION", "spec/ai-tutor.md", "prompts/ai-tutor-minimal.txt", ".github/ISSUE_TEMPLATE/feedback.yml", ".github/ISSUE_TEMPLATE/bug.yml", ".github/ISSUE_TEMPLATE/feature.yml"]
for name in required:
    assert (ROOT / name).is_file(), name
assert re.fullmatch(r"\d+\.\d+\.\d+\n?", (ROOT / "VERSION").read_text())
errors = []
tracked = subprocess.check_output(["git", "ls-files", "-z", "--", "*.md"], cwd=ROOT).decode().split("\0")
for name in filter(None, tracked):
    p = ROOT / name
    if not p.is_file(): continue
    text = p.read_text()
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if "://" in target or target.startswith("#"): continue
        target = target.split("#")[0]
        if not (p.parent / target).exists(): errors.append(f"{p.relative_to(ROOT)}: {target}")
for name, keys in [("skills/ai-tutor/SKILL.md", ["name", "description"]), ("prompts/copilot/ai-tutor.prompt.md", ["name", "description", "agent"])]:
    text = (ROOT / name).read_text()
    assert text.startswith("---\n")
    header = text.split("---", 2)[1]
    for key in keys: assert re.search(rf"^{key}: .+", header, re.M), (name, key)
assert not errors, "Broken links: " + "; ".join(errors)
print("Required files, frontmatter and local links are valid.")
