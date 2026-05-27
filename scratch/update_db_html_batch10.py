import json
import os

ROOT_DIR = "/Users/cyberial/.gemini/antigravity/worktrees/friendly-chandrasekhar/audit-claude-system-prompts"
db_path = os.path.join(ROOT_DIR, "prompts_db.json")
html_path = os.path.join(ROOT_DIR, "index.html")

# Load database JSON
with open(db_path, "r", encoding="utf-8") as f:
    db_data = json.load(f)

formatted_db = json.dumps(db_data, indent=2)

# Load HTML content
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# 1. Update localDatabase content in index.html
db_start_marker = "    const localDatabase ="
close_idx = html_content.find("];", html_content.find(db_start_marker))

if db_start_marker in html_content and close_idx != -1:
    # We will format the db to have correct indentation
    indented_db = "\n"
    for line in formatted_db.split("\n"):
        if line.strip():
            indented_db += "    " + line + "\n"
    
    html_content = html_content[:html_content.find(db_start_marker) + len(db_start_marker)] + indented_db + "    ];" + html_content[close_idx + 2:]
    print("Successfully replaced localDatabase array in HTML.")
else:
    print("Error: Could not locate localDatabase markers in HTML.")

# 2. Update Header Stat Label
html_content = html_content.replace(
    'Audited (Batch 1-9)',
    'Audited (Batch 1-10)'
)

# 3. Update Batch selector buttons
btn_old = '<button class="batch-btn" id="btn-batch9">Batch 9: Managed Agents (95-106)</button>'
btn_new = (
    '<button class="batch-btn" id="btn-batch9">Batch 9: Managed Agents (95-106)</button>\n'
    '          <button class="batch-btn" id="btn-batch10">Batch 10: Migration & SDK (107-150)</button>'
)
html_content = html_content.replace(btn_old, btn_new)

# 4. Update pending tool placeholder tooltip
html_content = html_content.replace("Batch 10+ - Pending", "Batch 11+ - Pending")

# 5. Update populateGrid batch filter conditions
filter_old = """          } else if (activeBatch === 'batch9' && (i < 95 || i > 106)) {
            cell.classList.add('batch-inactive');
          }"""
filter_new = """          } else if (activeBatch === 'batch9' && (i < 95 || i > 106)) {
            cell.classList.add('batch-inactive');
          } else if (activeBatch === 'batch10' && (i < 107 || i > 150)) {
            cell.classList.add('batch-inactive');
          }"""
html_content = html_content.replace(filter_old, filter_new)

# 6. Update setupTabs variables and tab arrays
tabs_vars_old = """      const btnB8 = document.getElementById('btn-batch8');
      const btnB9 = document.getElementById('btn-batch9');

      const tabs = [btnAll, btnB1, btnB2, btnB3, btnB4, btnB5, btnB6, btnB7, btnB8, btnB9];"""
tabs_vars_new = """      const btnB8 = document.getElementById('btn-batch8');
      const btnB9 = document.getElementById('btn-batch9');
      const btnB10 = document.getElementById('btn-batch10');

      const tabs = [btnAll, btnB1, btnB2, btnB3, btnB4, btnB5, btnB6, btnB7, btnB8, btnB9, btnB10];"""
html_content = html_content.replace(tabs_vars_old, tabs_vars_new)

# 7. Update setupTabs click event listeners
listeners_old = """      btnB9.addEventListener('click', () => {
        clearActive();
        btnB9.classList.add('active');
        populateGrid('batch9');
      });"""
listeners_new = """      btnB9.addEventListener('click', () => {
        clearActive();
        btnB9.classList.add('active');
        populateGrid('batch9');
      });

      btnB10.addEventListener('click', () => {
        clearActive();
        btnB10.classList.add('active');
        populateGrid('batch10');
      });"""
html_content = html_content.replace(listeners_old, listeners_new)

# Save the updated index.html
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully updated index.html with all dynamic stats, UI components, and new database elements.")
