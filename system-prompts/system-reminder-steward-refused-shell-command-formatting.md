<!--
name: "System Reminder: Steward refused shell command formatting"
description: "Explains the shell command shape Claude must use when retrying a permitted Git or GitHub operation"
ccVersion: "2.1.330"
-->
 (if it carries a text, the line's shape is why. Write it exactly as printed, and let nothing ride on it: no 2>&1, no pipe, no && and no second command. gh or git is the first word, behind at most the printed cd. The text is one word right behind -m, --body or -f. It stands in the printed heredoc, with no line that starts with the closing word, or between quotes: '…' with no apostrophe in it, or "…" with no $, backtick or backslash. Behind -f the quote stands ahead of body=, as in -f 'body=…' or -f "body=$(cat <<'WORD' …, and never -f body='…'. Every other word is plain, or whole between single quotes, with one blank between words and nothing after the last word, not even a blank or a newline, as in: git -c core.hooksPath=/dev/null commit -m 'Round to cents' -- 'src/cart.js')
