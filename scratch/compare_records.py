import json

with open("prompts_db.json") as f:
    db = json.load(f)

with open("scratch/records_subagent1.json") as f:
    sub1 = json.load(f)

db_map = {r["id"]: r for r in db if 1 <= r["id"] <= 34}
sub1_map = {r["id"]: r for r in sub1}

print("Comparing IDs 1-34:")
all_ok = True
for i in range(1, 35):
    db_rec = db_map.get(i)
    sub_rec = sub1_map.get(i)
    
    if not db_rec:
        print(f"ID {i} missing from prompts_db.json in range 1-34!")
        all_ok = False
        continue
    
    if not sub_rec:
        print(f"ID {i} missing from records_subagent1.json!")
        all_ok = False
        continue
        
    if db_rec["filename"] != sub_rec["filename"]:
        print(f"ID {i}: filename mismatch! DB: '{db_rec['filename']}', Sub1: '{sub_rec['filename']}'")
        all_ok = False
        
    if db_rec["name"] != sub_rec["name"]:
        print(f"ID {i}: name mismatch! DB: '{db_rec['name']}', Sub1: '{sub_rec['name']}'")
        all_ok = False

if all_ok:
    print("All IDs, filenames, and names match perfectly between prompts_db.json and records_subagent1.json.")
else:
    print("Mismatches found!")
