import json
import os
import re

ROOT_DIR = "/Users/cyberial/.gemini/antigravity/worktrees/friendly-chandrasekhar/audit-claude-system-prompts"
db_path = os.path.join(ROOT_DIR, "prompts_db.json")
skills_dir = "/Users/cyberial/.gemini/antigravity/skills"

# Load database
with open(db_path, "r", encoding="utf-8") as f:
    db = json.load(f)

# Load skills files
skills_content = {}
for skill_name in os.listdir(skills_dir):
    skill_path = os.path.join(skills_dir, skill_name, "SKILL.md")
    if os.path.exists(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            skills_content[skill_name] = f.read()

# Define critical keywords/rules to check coverage for
checks = [
    {
        "category": "Bash Safety",
        "keywords": ["PAGER=cat", "non-interactive", "-y", "apt-get", "npm init"],
        "description": "Prevention of hung terminals via non-interactive shell flags and pager overrides."
    },
    {
        "category": "Git Safety",
        "keywords": ["git commit --amend", "--no-verify", "EOF", "HEREDOC", "git status"],
        "description": "Git linear history preservation, bypass prevention, and shell escaping."
    },
    {
        "category": "Planning Mode",
        "keywords": ["AskUserQuestion", "ExitPlanMode", "implementation_plan.md", "hash", "timestamp"],
        "description": "Strict plan file writing verification and conversational exit prevention."
    },
    {
        "category": "Memory & Compaction",
        "keywords": ["compaction", "verbatim", "security", "boundaries", "70%", "85%"],
        "description": "Retention of user-stated security boundaries verbatim during context compactions."
    },
    {
        "category": "Stuck Diagnostics",
        "keywords": ["zombie", "uninterruptible sleep", "RSS", "lsof", "CPU load", "pgrep"],
        "description": "Detailed subprocess hanging states and process memory footprint diagnostics."
    },
    {
        "category": "Cron Scheduling",
        "keywords": ["jitter", "UTC", "America/New_York", "timezone", "off-minute"],
        "description": "Thundering herd avoidance and explicit timezone conversions for cron triggers."
    },
    {
        "category": "Model Migration",
        "keywords": ["temperature", "top_p", "thinking: {type:", "effort", "xhigh", "Vertex AI", "Zod", "JSONSchema"],
        "description": "Model parameter validation, schema definitions, and SDK library changes."
    }
]

print("=== GAPS ANALYSIS REPORT ===")
for check in checks:
    print(f"\nCategory: {check['category']} ({check['description']})")
    for keyword in check["keywords"]:
        found = False
        matching_skills = []
        for name, content in skills_content.items():
            if keyword.lower() in content.lower():
                found = True
                matching_skills.append(name)
        if found:
            print(f"  [COVERED]  '{keyword}' in: {', '.join(matching_skills)}")
        else:
            print(f"  [MISSING]  '{keyword}' was NOT found in any skill file!")
