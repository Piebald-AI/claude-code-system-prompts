import json

def main():
    with open('/Users/cyberial/.gemini/antigravity/worktrees/friendly-chandrasekhar/audit-claude-system-prompts/prompts_db.json', 'r') as f:
        db = json.load(f)
    
    # Filter for IDs 35 to 58 inclusive
    target_ids = list(range(35, 59))
    records = [r for r in db if r['id'] in target_ids]
    
    print(f"Extracted {len(records)} records.")
    for r in records:
        print(f"ID: {r['id']} - Name: {r['name']} - Filename: {r['filename']}")
        
    with open('/Users/cyberial/.gemini/antigravity/worktrees/friendly-chandrasekhar/audit-claude-system-prompts/scratch/records_to_audit.json', 'w') as f:
        json.dump(records, f, indent=2)

if __name__ == '__main__':
    main()
