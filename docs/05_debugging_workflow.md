# 🐞 The Debugging Workflow

Errors are inevitable. The difference between a senior developer and a beginner is not _fewer_ errors, it is knowing how to resolve them efficiently.

Currently, the workflow of copying an error to ChatGPT, then copying the answer to Antigravity, is slow and fragmented. This SOP centralizes the process.

---

## 1. Do Not Panic or Guess

When a red error screen appears:

1. **Read the error.** The answer is usually in the first two lines.
2. If it says `module not found`, you forgot to `npm install` something.
3. If it says `cannot read properties of undefined (reading 'id')`, your database query failed to return data.

## 2. The AI-to-AI Collaboration Strategy

Antigravity (AG) is inside your codebase. ChatGPT is an outside expert. They play different roles.

### Phase 1: Let AG Try (Once)

1. Show the error to AG: _"I am getting this error when clicking the Save button: [paste error]. Please investigate."_
2. If AG fixes it on the first try, great.
3. If AG fails or suggests a massive, complicated refactor to fix a tiny bug, **stop AG**.

### Phase 2: Escalate to ChatGPT

1. Copy the exact file (`SaveButton.js`) and the exact error.
2. Paste both into ChatGPT.
3. **Prompt ChatGPT:** _"I am getting this error in my Next.js file: [paste error]. Here is the file: [paste file]. Find the root cause and provide the exact fix."_
4. ChatGPT is often better at spotting logical errors without the distraction of your entire codebase history.

### Phase 3: Bringing the Fix Back to AG

1. Do not try to type out ChatGPT's fix yourself if it's complex.
2. Paste ChatGPT's response directly to AG.
3. **Prompt AG:** _"ChatGPT suggests this fix: [paste ChatGPT's response]. Please review it, ensure it fits our architecture, and apply it to the file."_

## 3. Print Debugging (The Ultimate Truth)

AI often hallucinates why an error is happening. The console never lies.

- If a variable is inexplicably empty, tell AG: _"Add `console.log()` statements before line 45 to print the value of `user` and `post_id`. Let's see what is actually happening."_
- Check your browser console (Right-click -> Inspect -> Console) for frontend errors.
- Check your terminal (where you ran `npm run dev`) for backend errors.
