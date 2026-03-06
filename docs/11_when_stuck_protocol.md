# 🛑 The "When Stuck" Protocol

Development is mostly problem-solving. You _will_ get stuck. Code won't compile, the database won't connect, or AG will get confused.

When you hit a roadblock, **stop guessing** and follow this decision tree.

---

## Phase 1: The 15-Minute Rule

If you spend more than 15 minutes fighting the exact same error with Antigravity:

1. **Stop.** Do not try the same prompt a 4th time.
2. Acknowledge that you are stuck.
3. Move to Phase 2.

## Phase 2: The Decision Tree

### 🌳 Branch A: Is the error highly specific to your custom logic?

_(e.g., "The user profile is saving the name, but the avatar URL is null")_

- **Action:** Ask AG for a "State Dump."
- **Prompt:** "AG, stop coding. Tell me step-by-step how you understand the logic flow for saving the profile, and exactly what variables you think are being passed. Let's find the gap."

### 🌳 Branch B: Is it a generic framework/library error?

_(e.g., "React Hook useEffect has a missing dependency" or "Supabase JWT expired")_

- **Action:** Do not rely solely on AG.
- **Prompt AG:** "Wait here."
- **External Action:** Copy the exact error and the code block. Paste it into **ChatGPT (o1/GPT-4)** or search Google/StackOverflow. ChatGPT is often better at spotting widespread framework bugs because its context window isn't cluttered by your entire project history.
- **Bring it back:** Copy the solution from ChatGPT and tell AG: "ChatGPT suggests this fix: [paste]. Review it and implement it safely."

### 🌳 Branch C: Did the app work 20 minutes ago, and now it's completely broken?

- **Action:** Rollback immediately. Do not try to "fix forward" if you don't know what broke.
- **Consult:** Open `09_emergency_recovery.md` and follow the `git restore` or `git reset` steps. Once restored, try building the feature again in smaller, safer steps.

## Phase 3: The "Nuclear" Option (Scrapping the Feature)

If a feature is taking days and holding up the entire app launch:

- Ask yourself: **Is this feature strictly necessary for V1?**
- If NO: Comment out the code, hide the button in the UI, write a note in your backlog to fix it later, and move on to the next feature.
- **Momentum is more important than perfection.**

## Guidelines for Genesis (or other collaborators)

If a team member gets stuck:

1. They must immediately open a Pull Request (PR) with their broken code.
2. They must NOT merge it into the `main` branch.
3. They should notify you: "I am stuck on X. I made a PR on branch `feature/X-fix` so you can look at it."
4. You can pull their branch locally, use AG to review it, fix the bug, and push it back.
