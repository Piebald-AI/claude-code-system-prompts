import json

with open("prompts_db.json") as f:
    db = json.load(f)

range_records = [r for r in db if 1 <= r["id"] <= 34]

for r in range_records:
    print(f"================================================================================")
    print(f"ID {r['id']}: {r['name']} ({r['filename']})")
    print(f"Category: {r['category']} | Status: {r['status']}")
    print(f"Description: {r['description']}")
    print(f"Audit Details: {r.get('audit_details', '')}")
    print(f"Gemini Rationale:\n{r.get('gemini_rationale', '')}")
    print(f"Gemini Strategy:\n{r.get('gemini_strategy', '')}")
    print(f"================================================================================\n")
