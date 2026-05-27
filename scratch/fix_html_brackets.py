with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's replace the duplicate bracket sequence
content_fixed = content.replace("    ]\n    ];", "    ];")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content_fixed)

print("Successfully fixed duplicate bracket sequence in index.html!")
