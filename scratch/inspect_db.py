import json
import os

scratch_dir = "/Users/cyberial/.gemini/antigravity/worktrees/friendly-chandrasekhar/audit-claude-system-prompts/scratch"
db_path = "/Users/cyberial/.gemini/antigravity/worktrees/friendly-chandrasekhar/audit-claude-system-prompts/prompts_db.json"

with open(db_path) as f:
    db = json.load(f)
print(f"Total db records: {len(db)}")
print(f"Db IDs range: {db[0]['id']} to {db[-1]['id']}")

files = [
    "records_part1.json",
    "records_part2.json",
    "records_part3.json",
    "records_subagent1.json",
    "records_subagent2.json",
    "records_subagent3.json"
]

for file in files:
    path = os.path.join(scratch_dir, file)
    if os.path.exists(path):
        with open(path) as f:
            data = json.load(f)
        ids = [x["id"] for x in data]
        print(f"{file}: length={len(data)}, min_id={min(ids)}, max_id={max(ids)}")
    else:
        print(f"{file} does not exist")
