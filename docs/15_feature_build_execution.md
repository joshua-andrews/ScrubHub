# 🚀 Feature Build Execution

To prevent chaotic building, every single feature in this application must follow this exact step-by-step build order. This creates predictable momentum and reduces debugging loops by 80%.

---

## The 11-Step Build Order

When you and Antigravity start a new feature, do not jump straight to the UI. Follow this exact sequence:

### 1. Write the Logic Map

- Tell AG what you want to build.
- Ask AG to output a step-by-step logic map of how it will work under the hood.
- _Do not proceed until the logic makes sense._

### 2. Confirm the Database Schema

- Ensure the Supabase tables and Row Level Security (RLS) policies exist to support this logic.
- If they don't, write the SQL migration with AG.

### 3. Build the Backend Endpoint / Server Action

- Write the Next.js API route or Server Action that talks to the database.
- Establish the inputs it needs and the outputs it will return.

### 4. Test the Endpoint (with Console Logs)

- Call the endpoint manually or run a quick test script.
- Put `console.log()` everywhere to ensure the exact correct data is returning from Supabase.
- _If it fails here, debug here. Do not build UI on top of broken data._

### 5. Build the UI Shell (The 80%)

- Have AG build the React component, focusing _only_ on the layout and the form inputs.
- Do not worry about extreme visual polish or micro-animations yet.

### 6. Connect UI to the Backend

- Wire the buttons and forms to the Server Action.
- Display the actual data fetched from the database in the UI.

### 7. Test the Full Flow Locally

- Click the button. Submit the form.
- Does the loading state work?
- Did the row actually save in Supabase?
- Did the UI update without crashing?

### 8. Polish the UI (The 20%)

- Now that the feature works perfectly, enforce the `10_ui_polish_standards.md`.
- Add the hover states, the glassmorphism, the clean typography, and the empty states.

### 9. Commit Locally

- `git add .`
- `git commit -m "feat: built the [Name] feature end-to-end"`

### 10. Push the Branch

- `git push origin feature/[name-of-branch]`

### 11. Open the Pull Request

- Go to GitHub, open the PR, request review (from Genesis or yourself), and merge safely into `main`.

---

**Rule for Antigravity:** When instructed to build a feature, AG must mentally (or explicitly) iterate through these 11 steps in order. If told to stop or wait at a specific step, AG must comply before moving on.
