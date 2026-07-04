# 💰 Cost Optimization Guide for Agent Operations

**Purpose:** Rules for minimizing token usage and API costs while maintaining maximum productivity. Follow these religiously.

---

## 0. Caveman Prompt Rules — Shorter = Cheaper

### Every response must follow these token rules:

| Situation | Max Words | Example |
|-----------|-----------|---------|
| **Confirming a task** | 5 words | "Done. Pushed to GitHub." |
| **Explaining what changed** | 15 words | "Fixed the proxy rewrite bug. Root cause: `/api` prefix stripped." |
| **Asking a question** | 10 words | "Ready for the Day 5 prompt?" |
| **Teaching a concept** | 30 words | "OAuth: User clicks LinkedIn → redirect to LinkedIn → code sent back → exchanged for token → profile fetched." |
| **Summarizing results** | 20 words | "4 files updated. Scores: Py 5.2, DSA 2.8, Confidence 9.4." |
| **Error messages** | 10 words | "Replacement failed. Check whitespace around target." |

### 🚫 No-nos (waste tokens):
- **No greetings** — never "Good morning!", "Hey!", "Hope you're doing well!"
- **No filler phrases** — never "I think", "It seems like", "Let me", "I'll go ahead and"
- **No polite padding** — never "Please", "Thank you", "You're welcome", "My pleasure"
- **No meta-commentary** — never "I've analyzed your request and", "Based on my understanding"
- **No transitions** — never "Now let me", "Moving on to", "First of all"
- **No sign-offs** — never "Let me know if you need anything else!", "Happy coding!"
- **No apologies** — never "Sorry about that", "My apologies", "You're right"
- **No asking permission** — just do it. Don't ask "Shall I proceed?"

### ✅ Examples of caveman mode:

**Bad (40 words):**
> "Good morning! I've analyzed the changes you requested and I think the best approach would be to update the learning plan first. Let me go ahead and do that."

**Good (4 words):**
> "Updated learning plan. Done."

**Bad (50 words):**
> "I see that the file has been updated with the new content. Let me check the current state of things before making any changes. Based on my understanding of what you're looking for, I'll proceed with the following approach."

**Good (8 words):**
> "Read the file. Changes applied. Pushing now."

### Caveman = respect user's time and money. Every word costs. Make it count.

---

## 1. Read Operations — Be Efficient

### ❌ Expensive (Avoid)
```
read_file (small ranges, many calls)
  → read lines 1-10
  → read lines 11-20
  → read lines 21-30
```

### ✅ Optimal
```
read_file (large meaningful chunk)
  → read lines 1-100 at once
```
OR use `grep_search` on a single file to find exact lines before reading.

### Rules
- **Read 50-100 lines at a time**, not 10-20
- **Use `grep_search` first** to find exact locations, then read only what's needed
- **Use `file_search`** to find files instead of guessing paths
- **Use `semantic_search`** when you don't know exact terms — but only when necessary (it's expensive)
- **Never re-read a file** you already have in context
- **Avoid `list_dir`** when `file_search` with a pattern is faster

---

## 2. Edit Operations — Batch Everything

### ❌ Expensive (Avoid)
```
replace_string_in_file (file1, change1)
replace_string_in_file (file1, change2)
replace_string_in_file (file2, change1)
```

### ✅ Optimal
```
multi_replace_string_in_file ([
  {file1, change1},
  {file1, change2},
  {file2, change1}
])
```

### Rules
- **Always use `multi_replace_string_in_file`** for 2+ changes — never sequential `replace_string_in_file`
- Group all independent edits into one call
- If editing 1 file but multiple spots → batch them
- If editing multiple files → batch them
- Only use single `replace_string_in_file` for ONE isolated change

---

## 3. Terminal Commands — Consolidate

### ❌ Expensive (Avoid)
```
run_in_terminal: cd /path && git status
run_in_terminal: cd /path && git add .
run_in_terminal: cd /path && git commit -m "..."
run_in_terminal: cd /path && git push
```

### ✅ Optimal
```
run_in_terminal: cd /path && git add . && git commit -m "..." && git push
```

### Rules
- **Chain commands with `&&`** instead of separate calls
- **Use `cd` once** at the start of a chain
- **Prefer `sync` mode** (default) — it returns full output inline, no follow-up needed
- **Only use `async` mode** for long-running processes (servers, watchers)
- **Never call `get_terminal_output`** after a `sync` command — output is already returned
- **Never use `sleep`** in terminal — you'll be notified automatically when async tasks complete

---

## 4. File Creation — Don't Split

### ❌ Expensive (Avoid)
```
create_file (file1 part 1)
create_file (file1 part 2)
```

### ✅ Optimal
```
create_file (file1 complete content)
```

### Rules
- **Write complete files in one `create_file` call** — don't create then edit
- Use `create_new_workspace` only for complete project scaffolding (not single files)
- For new notebook cells, prefer `edit_notebook_file` with a single insert

---

## 5. Information Gathering — Use Subagents Strategically

### ❌ Expensive (Avoid)
```
semantic_search (query 1)
semantic_search (query 2)
file_search (pattern)
grep_search (term)
read_file (file)
read_file (file2)
```

### ✅ Optimal
```
runSubagent (explore all of the above in one go)
```

### Rules
- **Use `runSubagent` with the `Explore` agent** for multi-step research instead of chaining 5+ tool calls
- But don't overuse subagents — for simple reads/searches, do it yourself
- **Threshold:** If you need 3+ read/search calls to answer one question → use a subagent

---

## 6. Memory System — Leverage Effectively

### Rules
- **Store repetitive context in memory** instead of re-reading files
- Use `/memories/repo/` for workspace facts (build commands, project structure)
- Use `/memories/session/` for current task plan
- **Check memory FIRST** before searching — the info might already be stored
- Update memory when you discover something you'll need again

---

## 7. Thinking — Be Concise

### Rules
- **Keep thinking brief** — don't narrate every option
- Only think through complex logic; skip obvious decisions
- If the next action is clear from context, take it without lengthy reasoning
- Use todo list to track state instead of re-reading previous conversation

---

## 9. Syllabus Sync — Never Guess What's Next

### Always check `agent/day_syllabus.md` before:
- Generating a day prompt
- Planning upcoming topics
- Answering "what's next?"

### Rules
- **Never assume** what was taught. Check the Completed table.
- **Never plan** more than 3 days ahead. Let actual pace dictate.
- **Update day_syllabus.md** after each day completes — append to Completed, move next to Current.
- The learning_plan.md has WEEK-level goals. day_syllabus.md has the actual DAY-level reality.
- If the user's pace differs from the plan → update day_syllabus.md, don't force the plan.

### ❌ Expensive (Avoid)
```
# Already know the file exists
file_search (**/*.py)

# Just created the file, then re-read it
create_file (file)
read_file (file)
```

### ✅ Optimal
- **Don't verify what you already know** — if you just wrote a file, you know its content
- **Don't search for files you just created**
- **Don't check git status after every change** — only when needed
- **Don't re-read instruction files** unless the task specifically requires it

---

## 9. Browser Operations — Minimize

### Rules
- **Only open browser when necessary** for frontend tasks
- **Read page** is cheaper than **screenshot** — prefer accessibility snapshots
- **Don't screenshot** unless visual verification is critical (UI layout, colors)
- Reuse existing browser pages instead of opening new ones

---

## 10. Error Recovery — Fast

### ❌ Expensive (Avoid)
```
replace_string_in_file (fails)
→ read_file to check content
→ try again
→ fails again
→ read whole file
```

### ✅ Optimal
- Read the file ONCE fully before retrying an edit
- Use `multi_replace_string_in_file` for first attempt (not single replace then batch)
- If a replacement fails → read 20 lines around the target to see exact formatting
- Don't retry more than 2 times — switch strategy

---

## Summary Cheat Sheet

| Situation | Do This | Saves |
|-----------|---------|-------|
| 2+ edits | `multi_replace_string_in_file` | 50%+ calls |
| Need to find something | `grep_search` first, then `read_file` | 60%+ tokens |
| Multi-step research | `runSubagent` Explore | 40%+ calls |
| Chain commands | `&&` in one terminal call | 50%+ calls |
| Complete new file | One `create_file` | 100% of follow-ups |
| Know the answer | Just respond | 100% of tool calls |
| Repetitive info | Store in memory | Varies |
