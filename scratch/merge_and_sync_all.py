import json
import os

ROOT_DIR = "/Users/cyberial/.gemini/antigravity/worktrees/friendly-chandrasekhar/audit-claude-system-prompts"
db_path = os.path.join(ROOT_DIR, "prompts_db.json")
html_path = os.path.join(ROOT_DIR, "index.html")
scratch_dir = os.path.join(ROOT_DIR, "scratch")

# Load subagent files
files = [
    "records_subagent1.json",
    "records_subagent2.json",
    "records_subagent3.json",
    "records_subagent4.json",
    "records_subagent5.json"
]

db_dict = {}

for filename in files:
    filepath = os.path.join(scratch_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            records = json.load(f)
            for record in records:
                db_dict[record["id"]] = record
            print(f"Loaded {len(records)} records from {filename}")
    else:
        print(f"ERROR: {filepath} does not exist!")

# Verify total count and IDs
total_loaded = len(db_dict)
print(f"Total unique records loaded: {total_loaded}")

missing_ids = []
for i in range(1, 317):
    if i not in db_dict:
        missing_ids.append(i)

if missing_ids:
    print(f"WARNING: Missing IDs: {missing_ids}")
else:
    print("SUCCESS: All IDs from 1 to 316 are accounted for!")

# Sort by ID
merged_db = [db_dict[i] for i in sorted(db_dict.keys())]

# Write to prompts_db.json
with open(db_path, "w", encoding="utf-8") as f:
    json.dump(merged_db, f, indent=2, ensure_ascii=False)
print(f"Saved merged database to {db_path}.")

# Format the db to have correct indentation in index.html
formatted_db = json.dumps(merged_db, indent=2, ensure_ascii=False)

# Load HTML content
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace localDatabase in index.html
db_start_marker = "    const localDatabase ="
close_idx = html_content.find("];", html_content.find(db_start_marker))

if db_start_marker in html_content and close_idx != -1:
    indented_db = "\n"
    for line in formatted_db.split("\n"):
        if line.strip():
            indented_db += "    " + line + "\n"
    
    html_content = html_content[:html_content.find(db_start_marker) + len(db_start_marker)] + indented_db + "    ];" + html_content[close_idx + 2:]
    print("Successfully replaced localDatabase array in HTML.")
else:
    print("Error: Could not locate localDatabase markers in HTML.")

# Save updated index.html
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Saved updated {html_path}.")
