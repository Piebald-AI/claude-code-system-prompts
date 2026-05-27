import os

search_root = "/Users/cyberial"
ignore_dirs = {
    "Library", "Pictures", "Music", "Movies", ".npm", ".cargo", ".rustup",
    ".gemini", "node_modules", ".git", "Library/Mobile Documents"
}

found = []
for root, dirs, files in os.walk(search_root):
    # Prune ignored directories
    dirs[:] = [d for d in dirs if d not in ignore_dirs and not d.startswith(".")]
    
    if "friendly-chandrasekhar" in dirs:
        full_path = os.path.join(root, "friendly-chandrasekhar")
        found.append(full_path)
        print(f"FOUND: {full_path}")
        
    # Limit depth to avoid infinite walks
    depth = root.replace(search_root, "").count(os.sep)
    if depth > 4:
        dirs[:] = []

print(f"Search complete. Found paths: {found}")
