# 🚨 Emergency Recovery Playbook

When something breaks badly (repo broken, build failing, database wiped, or Antigravity went totally rogue), **DO NOT PANIC**.

Follow this playbook exactly to restore order without making things worse.

---

## 1. The Golden Rule: Stop and Breathe

- **Do not immediately ask AI to "just fix it"** if you don't know what broke. This often leads to a spiral of worse errors.
- **Do not start deleting files.**
- **Do not force push to GitHub** (`git push -f`) unless you are absolutely certain.

## 2. GitHub / Git Rollback (The "Undo" Button)

If you just committed or pulled code that completely broke your app:

### Scenario A: You haven't committed the bad code yet.

You made some changes locally, and now everything is broken. You just want to go back to the last safe commit.

1. Open your terminal.
2. Run: `git restore .`
   _(This wipes all uncommitted changes and goes back to the last save point)_

### Scenario B: You ALREADY committed the bad code locally.

You committed it, but maybe haven't pushed it to GitHub.

1. Run: `git reset --hard HEAD~1`
   _(This deletes your last commit and resets the files to the commit before it)_

### Scenario C: You pushed the bad code to GitHub.

1. Go to your GitHub repository in the browser.
2. Look at the Commits history. Find the last "good" commit.
3. Tell Antigravity: "I need to revert my last push. The last known good commit is [paste commit hash]. Please write the exact `git revert` commands I need to run to safely undo the damage."

## 3. Database & Backend Breakages

If your Supabase database or edge functions break:

- **Migrations out of sync:** If Antigravity generated a bad database migration:
  Tell AG: "The last Supabase migration broke the schema. Please provide the exact SQL to rollback the last migration, and then let's rewrite it."
- **Authentication locked out:** If Row Level Security (RLS) policies locked everyone out, log into the Supabase dashboard manually, go to Authentication -> Policies, and temporarily disable the new policy while you debug.

## 4. When Antigravity Gets Confused / Goes Rogue

Sometimes AG gets stuck in a loop, repeatedly giving you the same wrong code.

1. **Say "STOP."** Literally tell AG: "Stop. Your current approach is failing."
2. **Clear the Context:** Say, "Forget the last 3 attempts. Let's start fresh. Here is the exact error we are getting, and here is the file. Read it carefully before proposing a fix."
3. **Use ChatGPT:** Copy the file and the error, paste it into ChatGPT (o1 or GPT-4), and ask: "Antigravity is stuck on this error. What is the fundamental issue here?" Then bring ChatGPT's answer back to AG.

## 5. Escaping "Dependency Hell"

If you get massive red errors about `node_modules`, `npm err`, or version conflicts:

1. Delete the `node_modules` folder.
2. Delete the `package-lock.json` file.
3. Run `npm install` (or `npm cache clean --force` then `npm install`).
   _(This fixes 90% of unexplained build errors.)_
