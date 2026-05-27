import json

with open('/Users/cyberial/.gemini/antigravity/worktrees/friendly-chandrasekhar/audit-claude-system-prompts/prompts_db.json', 'r') as f:
    db = json.load(f)

# Find records with ID between 59 and 82 inclusive
records = [r for r in db if 59 <= r.get('id', -1) <= 82]

print(f"Loaded {len(records)} records.")
for r in records:
    print(f"ID: {r['id']}, Title: {r.get('title')}, Path: {r.get('filepath')}")
