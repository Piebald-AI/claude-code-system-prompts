import json
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORPHANS_PATH = os.path.join(ROOT_DIR, 'scratch', 'orphans_list.json')

with open(ORPHANS_PATH, 'r', encoding='utf-8') as f:
    orphans = json.load(f)

print(f"Total orphans: {len(orphans)}")

# Let's divide them into 3 parts
n = len(orphans)
part_size = n // 3
remainder = n % 3

parts = []
start = 0
for i in range(3):
    size = part_size + (1 if i < remainder else 0)
    parts.append(orphans[start:start+size])
    start += size

for i, part in enumerate(parts):
    print(f"Part {i+1}: {len(part)} files, from {part[0]} to {part[-1]}")
    with open(os.path.join(ROOT_DIR, f'scratch/part_{i+1}_files.json'), 'w', encoding='utf-8') as f:
        json.dump(part, f, indent=2)
