✅ Merge-to-Main Release Gate SOP (Zero-Surprises Workflow)

This document defines the exact process Antigravity must follow to ensure a feature branch is safe to merge into main without breaking the application.

The purpose is to make main behave like a stable, production-safe branch at all times.

This SOP is designed for:

beginner-friendly execution

maximum safety

minimal “oops I broke main” moments

consistent results across projects

smooth collaboration (Josh + Genesis)

Important Reality: You can never guarantee 100% that a merge will be bug-free.
The goal is to reduce risk to near-zero by enforcing a repeatable release gate.

0) Definitions (Read This First)
main

The stable branch.

Represents the version we trust the most.

Should always be runnable and deployable.

Feature Branch

Any branch that includes new work (feature, bugfix, refactor).

Example: feature/prospects-table, bugfix/login-refresh

Release Gate

A strict checklist that must pass before merging into main.

1) Core Rule: No Direct Push to Main

Antigravity must never instruct or perform:

git push origin main

All merges into main must happen via:

Pull Request (PR)

Review + verification

Successful local validation

If asked to push to main, Antigravity must respond:

We should merge via PR after passing the Release Gate SOP.

2) The Release Gate Overview (High Level)

Before merging to main, Antigravity must ensure:

The app runs locally with no fatal errors

Core user flows work end-to-end

No secrets were added or exposed

Latest main is merged into the branch first (to catch conflicts early)

The app still works after that merge

A PR is created and reviewed

Only then is it safe to merge

This is the exact procedure below.

3) Step-by-Step Procedure (Antigravity Must Follow Exactly)
Step 1 — Confirm Local Server Is Running

Before testing, ensure the dev server is running (persistent).

Confirm the dev server is active at localhost:3000

If not running, start it immediately:

npm run dev

Antigravity must confirm:

Server running on localhost:3000.

Step 2 — Run a “Clean Startup” Check

This is the fastest way to detect hidden issues.

What to look for:

No red errors in terminal

No fatal errors in browser

No immediate crash loops

No missing environment variable errors

If any crash happens:

stop the merge process

fix first

retest from Step 1

Step 3 — Execute the Core Flow Test (Manual End-to-End)

This is the most important safety step.

Antigravity must test the application as if a real user is using it.

The Core Flow Test must include (customize per app):

At minimum, verify:

Authentication

Sign up (if enabled)

Login

Logout

Refresh the page while logged in

Confirm user stays logged in (unless intentionally configured otherwise)

Primary App Feature

Load main page/dashboard

Create a core object (e.g., prospect/task/post)

Confirm it appears in UI immediately

Confirm it exists in Supabase

Update it in UI

Confirm update persists in Supabase

Refresh page → confirm data persists

Delete (if applicable) → confirm deletion persists

Navigation & UI Stability

Navigate between primary pages

Ensure no broken routes

Ensure no UI state breaks

Confirm no layout corruption

Console + Network Errors

Browser console: no critical errors

Network tab: no 401/403 loops unless expected

Terminal logs: no repeated errors

If the feature branch changes backend behavior, Antigravity must validate both UI and database behavior.

Antigravity must summarize results:

what was tested

what passed

what failed (if anything)

what was fixed

Step 4 — Confirm No Secrets / Sensitive Data Were Introduced

Before pushing or PR creation, Antigravity must verify:

No .env files are staged

No credentials appear in code or docs

.gitignore includes env exclusions

Run:

git status

If .env or secrets appear:

stop immediately

remove from staging

rotate keys if exposed

re-verify

Step 5 — Pull Latest main (Prevent Surprise Conflicts)

This ensures your branch is compatible with current main.

Antigravity must do the following sequence:

git checkout main
git pull origin main
git checkout <your-feature-branch>
git merge main
What this accomplishes:

it catches conflicts now (safe place)

prevents merging broken code into main later

If merge conflicts occur:

resolve them carefully

explain every conflict resolution

do not “guess” resolutions

rerun tests afterward

Step 6 — Re-Run the Core Flow Test (Post-Merge Verification)

This is the step beginners skip — and it’s why main breaks.

After merging main into the feature branch, Antigravity must:

Ensure server is running

Reload localhost:3000

Repeat the Core Flow Test

Why:

conflicts or dependency differences can break things

code may behave differently after merge

this verifies branch is still stable

If anything fails:

fix

rerun this step again until clean

Step 7 — Commit Final Changes (Only if Needed)

If conflict resolution or fixes were made, commit cleanly:

git add .
git commit -m "Resolve merge conflicts and verify feature"

Important:

Don’t commit broken or partial states.

Don’t commit with vague messages like “fix”.

Step 8 — Push Branch (Not Main)

Push the feature branch to GitHub:

git push origin <your-feature-branch>
Step 9 — Open Pull Request (PR)

Create a PR from:
<your-feature-branch> → main

PR description must include:

What changed

What was tested locally

Confirmation that Core Flow Test passed

Any known limitations

Template:

Summary:
What I tested locally:
Database verification (Supabase):
Notes / Risks:

Step 10 — Final “Pre-Merge” Sanity Check

Before clicking merge, Antigravity must do a final check:

✅ app runs locally

✅ no terminal red errors

✅ core flow test passed

✅ no secrets staged

✅ branch includes latest main

✅ PR description includes testing summary

If all yes → safe to merge.

4) Optional Best Practice: Add Automated Checks (CI)

If you want an additional safety layer:

Add GitHub Actions to run:

lint

typecheck

build

tests (if you write them)

This makes GitHub prevent merges unless checks pass.

Note: This is not required for V1, but it is valuable as the app grows.

5) Unit Tests Explained (Simple + Practical)
What unit tests are

Unit tests verify small pieces of logic in isolation.

Example:

validating an email

transforming data

calculating totals

What they are NOT

They do not guarantee the whole app works.

For your workflow, the most valuable tests early are:

end-to-end manual flow tests

basic automated “build does not break” checks

Unit tests become most useful when:

logic becomes complex

many devs contribute

regressions happen often

business logic must be correct (payments, scoring, calculations)

6) Non-Negotiable Final Rule

If Antigravity is uncertain about stability:

It must not recommend merging.

Instead it must say:

I’m not confident this branch is fully stable yet. We should resolve X and retest before merging into main.

Because main must remain stable.

✅ Required Completion Confirmation (Antigravity Response)

After passing all steps, Antigravity must respond with:

Release Gate Passed:

App runs locally on localhost:3000

Core flow tested end-to-end

No secrets staged or exposed

Latest main merged into branch

Core flow tested again post-merge

PR created and ready to merge

Safe to merge into main.