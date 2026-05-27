import os

PROMPTS_DIR = "/Users/cyberial/.gemini/antigravity/worktrees/friendly-chandrasekhar/audit-claude-system-prompts/system-prompts"

all_files = sorted([f for f in os.listdir(PROMPTS_DIR) if f.endswith(".md")])
matches = []

for f in all_files:
    filepath = os.path.join(PROMPTS_DIR, f)
    # Check filename
    if "model" in f.lower() or "migration" in f.lower() or "sdk" in f.lower() or "reference" in f.lower() or "api" in f.lower():
        matches.append((f, "filename"))
        continue
        
    # Check content
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read().lower()
            if "model" in content or "migration" in content or "sdk" in content:
                matches.append((f, "content"))
    except:
        pass

print(f"Found {len(matches)} files matching 'model', 'migration', or 'sdk':")
for idx, (f, match_type) in enumerate(matches):
    print(f" {idx + 1:2d}. {f} (matched by {match_type})")
