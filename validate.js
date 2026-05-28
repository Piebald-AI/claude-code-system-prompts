import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = __dirname;
const DB_PATH = path.join(ROOT_DIR, 'prompts_db.json');
const PROMPTS_DIR = path.join(ROOT_DIR, 'system-prompts');

const REQUIRED_FIELDS = [
  'id', 'filename', 'name', 'category', 'status', 'description', 
  'tokens', 'audit_details', 'gemini_rationale', 'gemini_strategy'
];

const PLACEHOLDER_PATTERNS = [
  /^\s*todo:?/i,
  /^placeholder$/i,
  /\[insert/i,
  /^tbd$/i,
  /^n\/a$/i,
  /^no description/i,
  /^none$/i,
  /^\s*$/
];

async function validate() {
  if (!fs.existsSync(DB_PATH)) {
    console.error(`Error: ${DB_PATH} does not exist`);
    process.exit(1);
  }

  const dbContent = fs.readFileSync(DB_PATH, 'utf-8');
  let records;
  try {
    records = JSON.parse(dbContent);
  } catch (err) {
    console.error('Error parsing JSON:', err.message);
    process.exit(1);
  }

  console.log(`Loaded ${records.length} records from prompts_db.json`);

  const anomalies = [];
  const filesChecked = new Set();

  records.forEach((record, index) => {
    const recordId = record.id || `index_${index}`;
    const name = record.name || 'Unnamed';
    
    // Check required fields
    REQUIRED_FIELDS.forEach(field => {
      if (!(field in record)) {
        anomalies.push({
          id: recordId,
          name,
          issue: `Missing field: ${field}`
        });
      } else {
        const val = record[field];
        if (val === null || val === undefined) {
          anomalies.push({
            id: recordId,
            name,
            issue: `Field ${field} is null/undefined`
          });
        } else if (typeof val === 'string') {
          // Check placeholder patterns
          PLACEHOLDER_PATTERNS.forEach(pattern => {
            if (pattern.test(val)) {
              anomalies.push({
                id: recordId,
                name,
                issue: `Field ${field} has placeholder value: "${val.length > 60 ? val.substring(0, 60) + '...' : val}" (matched ${pattern})`
              });
            }
          });
        } else if (field === 'tokens' && (typeof val !== 'number' || val <= 0)) {
          anomalies.push({
            id: recordId,
            name,
            issue: `Field tokens has invalid value: ${val}`
          });
        }
      }
    });

    // Check actual file existence
    if (record.filename) {
      const filePath = path.join(PROMPTS_DIR, record.filename);
      filesChecked.add(record.filename);
      if (!fs.existsSync(filePath)) {
        anomalies.push({
          id: recordId,
          name,
          issue: `File does not exist: system-prompts/${record.filename}`
        });
      } else {
        // Read file and make sure the prompt logic matches
        const fileContent = fs.readFileSync(filePath, 'utf-8');
        // Let's do some sanity checks: is the file content matching the prompt description or details?
        if (fileContent.trim().length === 0) {
          anomalies.push({
            id: recordId,
            name,
            issue: `File system-prompts/${record.filename} is empty`
          });
        }
      }
    }
  });

  // Report anomalies
  if (anomalies.length > 0) {
    console.log(`\nFound ${anomalies.length} issues/anomalies:`);
    anomalies.forEach((a, i) => {
      console.log(`${i + 1}. [ID: ${a.id}] ${a.name}: ${a.issue}`);
    });
    process.exit(1);
  } else {
    console.log('\nNo anomalies found. All records are valid!');
    process.exit(0);
  }

  // Check for orphan markdown files in system-prompts/
  try {
    const allFiles = fs.readdirSync(PROMPTS_DIR).filter(f => f.endsWith('.md'));
    const orphans = allFiles.filter(f => !filesChecked.has(f));
    if (orphans.length > 0) {
      console.log(`\nFound ${orphans.length} orphan markdown files in system-prompts/ not referenced in prompts_db.json:`);
      // Just print first 10
      orphans.slice(0, 10).forEach(f => console.log(` - ${f}`));
      if (orphans.length > 10) console.log(` ... and ${orphans.length - 10} more`);
    }
  } catch (err) {
    console.error('Error reading prompts directory:', err.message);
  }
}

validate();

