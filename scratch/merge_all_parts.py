import json
import os

ROOT_DIR = "/Users/cyberial/.gemini/antigravity/worktrees/friendly-chandrasekhar/audit-claude-system-prompts"
DB_PATH = os.path.join(ROOT_DIR, "prompts_db.json")
SCRATCH_DIR = os.path.join(ROOT_DIR, "scratch")

# Load existing database (records 1 to 150)
if os.path.exists(DB_PATH):
    with open(DB_PATH, "r", encoding="utf-8") as f:
        db = json.load(f)
else:
    db = []

print(f"Initial prompts_db.json has {len(db)} records.")

# Load new parts
files = [
    "records_part1.json",
    "records_part2.json",
    "records_part3.json"
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

# Index by ID to deduplicate and sort
db_dict = {item["id"]: item for item in db}

for record in all_new_records:
    db_dict[record["id"]] = record

# Sort by ID
merged_db = [db_dict[i] for i in sorted(db_dict.keys())]

# Save back to prompts_db.json
with open(DB_PATH, "w", encoding="utf-8") as f:
    json.dump(merged_db, f, indent=2)

print(f"Merged database saved to {DB_PATH}. Total records: {len(merged_db)}")
