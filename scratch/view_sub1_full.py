import json

with open("scratch/records_subagent1.json") as f:
    records = json.load(f)

for r in records:
    print(f"================================================================================")
    print(f"ID {r['id']}: {r['name']} ({r['filename']})")
    print(f"Category: {r['category']} | Status: {r['status']}")
    print(f"Description: {r['description']}")
    print(f"Audit Details: {r['audit_details']}")
    print(f"Gemini Rationale:\n{r['gemini_rationale']}")
    print(f"Gemini Strategy:\n{r['gemini_strategy']}")
    print(f"================================================================================\n")
