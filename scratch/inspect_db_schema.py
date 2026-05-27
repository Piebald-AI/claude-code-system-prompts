import json

with open("prompts_db.json", "r") as f:
    db = json.load(f)

for r in db:
    if r["id"] == 107:
        print(json.dumps(r, indent=2))
        break
