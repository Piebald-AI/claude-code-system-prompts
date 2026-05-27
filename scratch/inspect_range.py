import json
import os

with open("prompts_db.json", "r") as f:
    db = json.load(f)

range_records = [r for r in db if 107 <= r["id"] <= 316]
print(f"Number of records: {len(range_records)}")

categories = set()
statuses = set()
for r in range_records:
    categories.add(r["category"])
    statuses.add(r["status"])

print("Categories:", sorted(list(categories)))
print("Statuses:", sorted(list(statuses)))

# Look at one example
example = range_records[0]
print("\nExample Record (ID 107):")
print(json.dumps(example, indent=2))
