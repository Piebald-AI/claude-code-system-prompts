import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines, start=1):
    if '[' in line or ']' in line:
        # check if it's part of javascript code structure around localDatabase
        if 620 <= idx <= 2440:
            print(f"{idx}: {line.strip()}")
