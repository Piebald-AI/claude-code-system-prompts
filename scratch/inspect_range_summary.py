import json
import os

with open("prompts_db.json", "r") as f:
    db = json.load(f)

records = [r for r in db if 107 <= r["id"] <= 316]
print(f"Total: {len(records)}")

out = []
for r in records:
    filepath = os.path.join("system-prompts", r["filename"])
    exists = os.path.exists(filepath)
    out.append({
        "id": r["id"],
        "filename": r["filename"],
        "name": r["name"],
        "category": r["category"],
        "status": r["status"],
        "exists": exists,
        "desc": r.get("description", "")
    })

with open("scratch/range_summary.json", "w") as f:
    json.dump(out, f, indent=2)

print("Wrote scratch/range_summary.json")
