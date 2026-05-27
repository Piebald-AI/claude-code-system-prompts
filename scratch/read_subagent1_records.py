import json

with open("scratch/records_subagent1.json") as f:
    records = json.load(f)

print(f"Loaded {len(records)} records.")
for r in records:
    print(f"ID {r['id']}: {r['filename']} | {r['status']}")
    print(f"  Rationale: {r.get('gemini_rationale', '')[:80]}...")
    print(f"  Strategy:  {r.get('gemini_strategy', '')[:80]}...")
