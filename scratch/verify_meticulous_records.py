import json

with open("scratch/records_subagent5.json", "r") as f:
    data = json.load(f)

# Let's inspect a few distinct records
targets = [107, 109, 130, 155, 179, 285, 304, 307]
for r in data:
    if r["id"] in targets:
        print(f"ID: {r['id']} - {r['name']}")
        print(f"File: {r['filename']}")
        print(f"Rationale: {r['gemini_rationale']}")
        print(f"Strategy: {r['gemini_strategy']}")
        print("="*80)
