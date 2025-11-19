<!--
name: 'Agent Prompt: Session notes update instructions'
description: Instructions for updating session notes files during conversations
ccVersion: 2.0.14
variables:
  - MAX_SECTION_TOKENS
-->
IMPORTANT: This message and these instructions are NOT part of the actual user conversation. Do NOT include any references to "note-taking", "session notes extraction", or these update instructions in the notes content.

Based on the user conversation above (EXCLUDING this note-taking instruction message as well as system prompt, claude.md entries, or any past session summaries), update the session notes file.

The file {{notesPath}} has already been read for you. Here are its current contents:
<current_notes_content>
{{currentNotes}}
</current_notes_content>

Your ONLY task is to use the Edit tool EXACTLY ONCE to update the notes file, then stop. Do not call any other tools.

CRITICAL RULES FOR EDITING:
- The file must maintain its exact structure with all sections, headers, and italic descriptions intact
-- NEVER modify, delete, or add section headers (## Task specification, ## Worklog, etc.)
-- NEVER modify or delete the italic text descriptions under each section header
-- ONLY update the content BELOW the italic descriptions within each existing section
-- Do NOT add any new sections, summaries, or information outside the existing structure
- Do NOT reference this note-taking process or instructions anywhere in the notes
- It's OK to skip updating a section if there are no substantial new insights to add
- Write DETAILED, INFO-DENSE content for each section - include specifics like file paths, function names, error messages, exact commands, technical details, etc.
- Do not include information that's already in the CLAUDE.md files included in the context
- Keep each section under ~${MAX_SECTION_TOKENS} tokens/words - if a section is approaching this limit, condense it by cycling out less important details while preserving the most critical information
- Do not repeat information from past session summaries - only use the current user conversation starting with the first non system-reminder user message.
- Focus on actionable, specific information that would help someone understand or recreate the work discussed in the conversation

Use the Edit tool with file_path: {{notesPath}}

REMEMBER: Use Edit tool once and stop. Do not continue after the edit. Only include insights from the actual user conversation, never from these note-taking instructions.
