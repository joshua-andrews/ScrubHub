21) Plain-Language Implementation Plans (So Clear a 10-Year-Old Can Follow)
Why this document exists

Right now, implementation plans are often written like this:

“Modify Upload.tsx”

“Update triggerGeneration”

“Add callback function”

“Insert records into content_pieces”

“Remove redundant API call”

This might be accurate, but it’s not clear.

It doesn’t answer the question you actually care about:

“When I press Proceed, what exactly happens — step by step — and how do I know it worked?”

This document defines a new standard.

From now on, every implementation plan must be written in plain language, with a click-by-click story of what happens in the app, plus a verification checklist so you can confirm it’s working.

The Core Rule

Implementation plans must be understandable to someone with zero coding knowledge.

If a plan requires developer knowledge to understand, it fails this SOP.

The “10-Year-Old Plan Format” (Required Template)

Every implementation plan must include these sections, in this exact order.

1) What are we building? (One sentence)

Say what we’re adding or fixing, in plain words.

Example:
“We are adding support for uploading Markdown (.md) files, and we are making content generation happen in batches of 5.”

2) Why are we doing this? (One short paragraph)

Explain the problem and the goal.

Example:
“Right now the app only accepts PDF uploads. We want it to also accept Markdown files. Also, generation should happen in groups of 5 so the app doesn’t try to generate too much at once.”

3) What will the user see? (Before vs After)
Before

“Upload page only accepts PDF.”

“Generation triggers in a confusing way.”

After

“Upload page accepts PDF and Markdown.”

“When upload finishes, the app starts generating the first 5 items in the background.”

“When user presses Generate again, it generates the next 5 items only.”

4) The Step-By-Step Story (This is the most important part)

This section must read like a story of what happens when a user clicks buttons.

REQUIRED RULES FOR THIS SECTION

Each step must start with either User: or App:

No code words unless explained in parentheses

No “modify X file” language here

Must include what the user sees on screen

Must include what the app saves in the database (in plain words)

5) What gets saved and where? (Database, in plain English)

Explain what new info is stored, and why.

6) How to test it (Checklist)

A simple checklist you can follow on localhost.

If the plan doesn’t include a test checklist, it’s incomplete.

7) What could go wrong? (Common problems + what to do)

List likely errors and how to fix them.

Example: Rewrite of Your Current Plan (Plain-Language Version)
Feature Name: Upload Markdown Files + Generate in Batches of 5
1) What are we building?

We are allowing users to upload Markdown (.md) files, and we are making content generation happen 5 items at a time.

2) Why are we doing this?

Some books/content exist as Markdown files, not PDFs. Also, generating everything at once can be slow and confusing. Generating 5 at a time makes it easier to control, easier to test, and easier to see progress.

3) What will the user see?

After this change:

On the Upload screen, the user will see that they can upload PDF or Markdown

After upload finishes, the app will automatically:

find the list of topics

start generating the first 5 topics in the background

The progress number will go up live (like “Topics found: 12… 24… 38…”)

If the user clicks “Generate More”, it will only generate the next 5, not everything again

4) Step-By-Step Story: What happens when I press Proceed?
A) Uploading a Markdown file

User:

The user goes to the Upload page.

The user drags in a .md file (or selects it).

App:
3. The app accepts the file because .md is now allowed.
4. The app uploads the file to the backend.
5. The backend reads the text inside the Markdown file.
6. The backend creates a new “Book” record in the database (a row that represents the uploaded file).

It also saves what type of file it is: markdown.

It saves the extracted text so we can generate from it later.

User sees:
7. The upload finishes and the UI shows the book was successfully uploaded.
8. The UI immediately starts showing progress (like a live status) without the user doing anything else.

B) Topic Extraction (the app finding the list of topics)

App:
9. Right after upload, the backend starts scanning the book text to find a list of topics.
10. While it scans, it keeps updating a “progress counter” so the frontend can show something like:

“Found 10 topics…”

“Found 22 topics…”

“Found 37 topics…”

User sees:
11. The progress number ticks upward in real-time.

App:
12. When extraction finishes, the backend briefly pauses (~3 seconds) and changes the progress message to a clear status like:
✅ “Found 42 topics! Starting generation of the first 5 soon…”

C) Automatic Generation of the first 5 items

App:
13. After extraction, the backend automatically starts generating content for the first 5 topics only.
14. It saves the generated content in the database (each generated piece becomes a new record).
15. It updates progress so the frontend can show that generation is happening.

User sees:
16. The progress updates and the library/content list starts filling with generated items.

D) Clicking “Generate More” later

User:
17. The user clicks “Generate More” (or “Begin Generation”) to make more content.

App:
18. The frontend sends a request that means:
“Generate the next 5 topics, not all topics.”

Backend:
19. The backend checks the database to see which topics already have generated content.
20. It picks the next 5 topics that are still missing content.
21. It generates content only for those 5.
22. It saves them.
23. It returns success.

User sees:
24. 5 more items appear. Nothing duplicates. No “start from scratch” behavior.

5) What gets saved and where? (Plain English)

In Supabase we store:

A Book row (one row per uploaded file) containing:

file type (pdf or markdown)

extracted raw text (so the app can generate from it)

extracted topics list (so we know what to generate)

A Content Pieces table containing:

generated items

which topic they came from

which book they belong to

This is how the app remembers:

what topics exist

what is already generated

what still needs generating

6) How to test it (Localhost checklist)

On localhost:3000:

Upload a .md file

Confirm upload succeeds (no errors)

Confirm progress appears automatically (without clicking Generate)

Confirm “topics found” number increases during extraction

Confirm you see the message: “Found X topics! Starting generation of the first 5 soon…”

Confirm 5 generated items appear

Click “Generate More”

Confirm exactly 5 more appear

Confirm no duplicates

Refresh the page

Confirm you are still logged in (if expected) and data is still there

7) What could go wrong? (Most common issues)

Problem: Upload succeeds but progress never updates
Fix: The frontend isn’t polling the progress endpoint, or the backend isn’t saving progress updates.

Problem: Generate More generates everything again
Fix: The backend isn’t correctly checking what’s already generated.

Problem: You get logged out on refresh
Fix: Session cookie / auth persistence misconfigured.

Problem: Data appears in the wrong Supabase project
Fix: Wrong environment variables are loaded (see Supabase Project Verification SOP).

Required “No-Jargon” Translation Rule

If the plan mentions any technical term (examples below), it must add a parenthesis explanation:

“API route” (a URL endpoint the frontend calls)

“polling” (checking for updates every few seconds)

“callback” (a function the backend calls to report progress)

“insert records” (save new rows into the database)

“RLS” (database rules that control who can see what)

If Antigravity can’t explain the term simply, it must not use it.

Final Output Requirement (for Antigravity)

For every implementation plan going forward, Antigravity must produce:

The one-sentence goal

What the user will see (before vs after)

The click-by-click Step-By-Step Story (User/App format)

What gets saved (plain English)

Testing checklist

What could go wrong + fixes

Only after that is complete should Antigravity include:

“files to change”

“functions to update”

“code-level notes”

Because those are only useful after you understand what happens when you click.

If you want, I can also write a second companion doc for this called:

22_implementation_plan_template.md
…which is literally a fill-in-the-blanks form AG must follow every time (so it can’t slip back into vague bullet points).