import os
import json

ROOT_DIR = "/Users/cyberial/.gemini/antigravity/worktrees/friendly-chandrasekhar/audit-claude-system-prompts"
PROMPTS_DIR = os.path.join(ROOT_DIR, "system-prompts")
PART_1_FILES_PATH = os.path.join(ROOT_DIR, "scratch/part_1_files.json")

with open(PART_1_FILES_PATH, "r", encoding="utf-8") as f:
    files = json.load(f)

output_file = os.path.join(ROOT_DIR, "scratch/headers_output.txt")
with open(output_file, "w", encoding="utf-8") as out:
    for idx, filename in enumerate(files):
        file_id = 151 + idx
        filepath = os.path.join(PROMPTS_DIR, filename)
        if not os.path.exists(filepath):
            out.write(f"[{file_id}] File not found: {filename}\n")
            continue
        
        with open(filepath, "r", encoding="utf-8") as pf:
            lines = pf.readlines()
        
        out.write("=" * 80 + "\n")
        out.write(f"[{file_id}] {filename} (Total lines: {len(lines)})\n")
        out.write("-" * 40 + "\n")
        for line in lines[:30]:
            out.write(line)
        out.write("\n" + "=" * 80 + "\n\n")

print(f"Headers output written to {output_file}")
