import os
import json

ROOT_DIR = "/Users/cyberial/.gemini/antigravity/worktrees/friendly-chandrasekhar/audit-claude-system-prompts"
PROMPTS_DIR = os.path.join(ROOT_DIR, "system-prompts")
PART_1_FILES_PATH = os.path.join(ROOT_DIR, "scratch/part_1_files.json")

with open(PART_1_FILES_PATH, "r", encoding="utf-8") as f:
    files = json.load(f)

metadata = []
for idx, filename in enumerate(files):
    file_id = 151 + idx
    filepath = os.path.join(PROMPTS_DIR, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        continue
    
    with open(filepath, "r", encoding="utf-8") as pf:
        content = pf.read()
    
    words = content.split()
    word_count = len(words)
    tokens = int(word_count * 1.3)
    
    # Extract a clean name from the filename
    # e.g., agent-prompt-agent-creation-architect.md -> Agent Prompt: Agent creation architect
    name_parts = filename.replace(".md", "").split("-")
    category = "Unknown"
    if name_parts[0] == "agent" and name_parts[1] == "prompt":
        category = "Agent Prompts"
        name = "Agent Prompt: " + " ".join(name_parts[2:]).capitalize()
    elif name_parts[0] == "system" and name_parts[1] == "prompt":
        category = "System Prompt"
        name = "System Prompt: " + " ".join(name_parts[2:]).capitalize()
    elif name_parts[0] == "system" and name_parts[1] == "reminder":
        category = "System Reminders"
        name = "System Reminder: " + " ".join(name_parts[2:]).capitalize()
    elif name_parts[0] == "skill":
        category = "Builtin Tool Descriptions" # or similar
        name = "Skill: " + " ".join(name_parts[1:]).capitalize()
    elif name_parts[0] == "data":
        category = "Data Templates"
        name = "Data: " + " ".join(name_parts[1:]).capitalize()
    elif name_parts[0] == "tool" and name_parts[1] == "description":
        category = "Builtin Tool Descriptions"
        name = "Tool Description: " + " ".join(name_parts[2:]).capitalize()
    else:
        name = " ".join(name_parts).capitalize()
    
    # Let's read the first few lines of the file for a description if available
    lines = content.strip().split("\n")
    desc = ""
    for line in lines[:5]:
        if line.strip() and not line.startswith("#") and not line.startswith("---"):
            desc = line.strip()[:150]
            if len(line.strip()) > 150:
                desc += "..."
            break
    if not desc:
        desc = f"System prompt/skill for {name}."
        
    metadata.append({
        "id": file_id,
        "filename": filename,
        "name": name,
        "category": category,
        "status": "",
        "description": desc,
        "tokens": tokens,
        "word_count": word_count
    })

output_path = os.path.join(ROOT_DIR, "scratch/part_1_metadata.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2)

print(f"Generated metadata for {len(metadata)} files in {output_path}")
