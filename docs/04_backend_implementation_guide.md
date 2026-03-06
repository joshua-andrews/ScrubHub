# ⚙️ Backend Implementation Guide

The backend is where logic happens. Unlike the frontend, if the backend is 80% correct, the app is 100% broken.

This guide ensures backend processes function exactly as envisioned the first time, without endless "please fix" loops.

---

## 1. Pre-Build Logic Verification

Never ask AG to "just build the backend feature." It will guess your database structure and hallucinate column names.

**The Verification Prompt:**
Before writing code, tell AG:

> "We are about to build the User Invite system. Before you write any code, write a step-by-step logic map. List exactly which database tables you will query, what data you will insert, and what edge cases you predict (e.g., what if the user already exists?). Wait for my approval."

If AG's map misses a step, correct the map _before_ it writes code.

## 2. Prompt Structures for the AI

Use structured prompts to constrain AG.

### The "API Route" Prompt

> "I need a Server Action (or Next.js API route) to handle creating a new Post.
> **Input:** `title` (string), `content` (string), `author_id` (UUID).
> **Validation:** Ensure the user is authenticated via Supabase Auth before allowing the insert.
> **Database:** Insert into the `posts` table.
> **Output:** Return success or throw a specific error if it fails."

## 3. The Validation Checklist

Before you consider a backend feature "done," run through this checklist with AG:

- [ ] **Auth Check:** Did we ensure only logged-in users can trigger this function?
- [ ] **RLS Check:** Does the Supabase Row Level Security policy actually allow this insert/select?
- [ ] **Error Handling:** If the database goes down, does the user see a friendly error or does the app crash?
- [ ] **Edge Cases:** Did we test what happens with empty inputs?

## 4. Keeping Antigravity Focused

If the backend starts behaving differently from your intent:

1. **Stop AG immediately.**
2. Tell it to output `console.log` statements for every variable at every step of the function.
3. Run the app, trigger the function, and look at your terminal.
4. Show AG the exact console logs so it sees exactly where the data becomes `null` or `undefined`.
