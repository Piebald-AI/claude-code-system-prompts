import os
import json
import re

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(ROOT_DIR, 'prompts_db.json')
PROMPTS_DIR = os.path.join(ROOT_DIR, 'system-prompts')

REQUIRED_FIELDS = [
    'id', 'filename', 'name', 'category', 'status', 'description', 
    'tokens', 'audit_details', 'gemini_rationale', 'gemini_strategy'
]

PLACEHOLDER_PATTERNS = [
    re.compile(r'^\s*todo:?', re.IGNORECASE),
    re.compile(r'^placeholder$', re.IGNORECASE),
    re.compile(r'\[insert', re.IGNORECASE),
    re.compile(r'^tbd$', re.IGNORECASE),
    re.compile(r'^n/a$', re.IGNORECASE),
    re.compile(r'^no description$', re.IGNORECASE),
    re.compile(r'^none$', re.IGNORECASE),
    re.compile(r'^\s*$')
]

def validate():
    if not os.path.exists(DB_PATH):
        print(f"Error: {DB_PATH} does not exist")
        return

    with open(DB_PATH, 'r', encoding='utf-8') as f:
        try:
            records = json.load(f)
        except Exception as e:
            print(f"Error parsing JSON: {e}")
            return

    print(f"Loaded {len(records)} records from prompts_db.json")

    anomalies = []
    files_checked = set()

    for idx, record in enumerate(records):
        record_id = record.get('id', f'index_{idx}')
        name = record.get('name', 'Unnamed')
        
        # Check required fields
        for field in REQUIRED_FIELDS:
            if field not in record:
                anomalies.append({
                    'id': record_id,
                    'name': name,
                    'issue': f"Missing field: {field}"
                })
            else:
                val = record[field]
                if val is None:
                    anomalies.append({
                        'id': record_id,
                        'name': name,
                        'issue': f"Field {field} is None"
                    })
                elif isinstance(val, str):
                    # Check placeholder patterns
                    for pattern in PLACEHOLDER_PATTERNS:
                        if pattern.search(val):
                            anomalies.append({
                                'id': record_id,
                                'name': name,
                                'issue': f"Field {field} contains placeholder pattern: '{val}'"
                            })
        
        if 'filename' in record:
            file_path = os.path.join(PROMPTS_DIR, record['filename'])
            files_checked.add(record['filename'])
            if not os.path.exists(file_path):
                anomalies.append({
                    'id': record_id,
                    'name': name,
                    'issue': f"File does not exist: system-prompts/{record['filename']}"
                })
            else:
                # Read file and make sure it has content
                with open(file_path, 'r', encoding='utf-8') as pf:
                    content = pf.read()
                    if not content.strip():
                        anomalies.append({
                            'id': record_id,
                            'name': name,
                            'issue': f"File system-prompts/{record['filename']} is empty"
                        })

    # Report anomalies
    if anomalies:
        print(f"\nFound {len(anomalies)} issues/anomalies:")
        for i, a in enumerate(anomalies):
            print(f"{i + 1}. [ID: {a['id']}] {a['name']}: {a['issue']}")
    else:
        print("\nNo anomalies found. All records in prompts_db.json are valid!")

    # Check for orphan files in system-prompts/
    try:
        all_files = [f for f in os.listdir(PROMPTS_DIR) if f.endswith('.md')]
        orphans = [f for f in all_files if f not in files_checked]
        if orphans:
            print(f"\nFound {len(orphans)} orphan markdown files in system-prompts/ not referenced in prompts_db.json:")
            for f in orphans[:10]:
                print(f" - {f}")
            if len(orphans) > 10:
                print(f" ... and {len(orphans) - 10} more")
    except Exception as e:
        print(f"Error reading prompts directory: {e}")

if __name__ == '__main__':
    validate()
