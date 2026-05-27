import json

with open("scratch/records_subagent5.json", "r") as f:
    data = json.load(f)

print(f"Total records in records_subagent5.json: {len(data)}")
for i, r in enumerate(data[:10]):
    print(f"ID: {r.get('id')} - {r.get('name')}")
    print(f"Rationale preview: {r.get('gemini_rationale')[:100]}...")
    print(f"Strategy preview: {r.get('gemini_strategy')[:100]}...")
    print("-" * 40)
