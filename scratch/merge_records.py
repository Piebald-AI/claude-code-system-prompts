import json
import os

ROOT_DIR = "/Users/cyberial/.gemini/antigravity/worktrees/friendly-chandrasekhar/audit-claude-system-prompts"
DB_PATH = os.path.join(ROOT_DIR, "prompts_db.json")
SCRATCH_DIR = os.path.join(ROOT_DIR, "scratch")

# Load existing database
if os.path.exists(DB_PATH):
    with open(DB_PATH, "r", encoding="utf-8") as f:
        db = json.load(f)
else:
    db = []

print(f"Initial database has {len(db)} records.")

# Load subagent files
files = [
    "records_subagent1.json",
    "records_subagent2.json",
    "records_subagent3.json"
]

all_new_records = []
for filename in files:
    filepath = os.path.join(SCRATCH_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            records = json.load(f)
            all_new_records.extend(records)
            print(f"Loaded {len(records)} records from {filename}")
    else:
        print(f"Error: {filepath} does not exist!")

# Deduplicate existing and new records by ID
db_dict = {item["id"]: item for item in db}

for record in all_new_records:
    # Ensure all fields are present
    db_dict[record["id"]] = record

# Sort and save
merged_db = [db_dict[i] for i in sorted(db_dict.keys())]

with open(DB_PATH, "w", encoding="utf-8") as f:
    json.dump(merged_db, f, indent=2)

print(f"Merged database saved to {DB_PATH}. Total records: {len(merged_db)}")
