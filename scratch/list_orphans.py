import os
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(ROOT_DIR, 'prompts_db.json')
PROMPTS_DIR = os.path.join(ROOT_DIR, 'system-prompts')

with open(DB_PATH, 'r', encoding='utf-8') as f:
    db = json.load(f)

print(f"Total database records: {len(db)}")
if db:
    print("Last record:")
    print(json.dumps(db[-1], indent=2, ensure_ascii=False))

all_files = sorted([f for f in os.listdir(PROMPTS_DIR) if f.endswith('.md')])
referenced = set(r['filename'] for r in db)
orphans = sorted([f for f in all_files if f not in referenced])

print(f"Total files in system-prompts/: {len(all_files)}")
print(f"Total referenced files: {len(referenced)}")
print(f"Total orphan files: {len(orphans)}")

# Let's print the list of orphans with index starting from 151
print("\nFirst 10 orphans:")
for idx, f in enumerate(orphans[:10], start=151):
    print(f"{idx}: {f}")

# Write the list of orphans to a JSON file in scratch
with open(os.path.join(ROOT_DIR, 'scratch', 'orphans_list.json'), 'w', encoding='utf-8') as f:
    json.dump(orphans, f, indent=2)
