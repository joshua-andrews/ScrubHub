# Master SOP: Working with Antigravity 🤖

Welcome to the command center. Antigravity (AG) is an incredibly powerful AI, but it is a tool—and like any high-performance tool, **it requires an operator who knows how to drive it.**

This document explains exactly how you should interact with AG to get elite results, avoid "rogue AI" behavior, and prevent endless loops of "please fix."

---

## 1. The Core Philosophy

- **AG is your Co-Pilot, You are the Architect.** Do not ask AG to "build an app." Ask it to "build the authentication module based on the `08_project_context_template.md` guidelines."
- **Prevent Over-Engineering.** AG loves to write complex code if left unchecked. Always instruct it to pick the _simplest_ path first.
- **Small Bites > Big Chunks.** Never ask AG to write 1,000 lines of code at once. Break it down: "Step 1: Setup database schema. Step 2: Build the UI surface. Step 3: Wire them together."

## 2. Prompting Best Practices

When talking to AG, structure your requests clearly:

### The "Perfect Prompt" Formula

1. **Context/Goal:** "We are working on the checkout page."
2. **Current State:** "The UI is built in Figma, but the Antigravity implementation looks slightly off."
3. **Exact Instruction:** "Please review the code in `Checkout.js` and make the spacing and typography match the modern UI standard described in `10_ui_polish_standards.md`."
4. **Boundary:** "Do not add any new logic or change the backend connection, focus ONLY on the styling."

## 3. When to Step In vs. Let AG Run

**Let AG Run when:**

- Scaffolding a new, standard feature (like creating a login form).
- Refactoring messy code into cleaner functions.
- Performing tedious tasks like updating imports across 20 files.

**Step In (Stop AG) when:**

- It starts modifying files entirely unrelated to your current goal.
- It suggests installing 5 new external libraries for a simple problem.
- It starts "guessing" how your database is structured instead of checking the schema.

_If AG starts going rogue, say: "Stop. Discard that approach. Let's return to the exact plan we discussed."_

## 4. The "Check-in" Cadence

AG should not work in the dark for an hour. Enforce check-ins:

- "Please write the plan for this feature, and WAIT for my approval before executing."
- "Write the first function, then show me."

## 5. Structuring the Relationship

- Always point AG to the SOPs: If something breaks, tell AG: "Consult the `11_when_stuck_protocol.md` before attempting another fix."
- If the UI isn't to your liking, tell AG: "Consult `10_ui_polish_standards.md` from the docs and apply it here."

## 6. Keeping AG Structured

By default, AG can get distracted by its own thoughts. To keep it focused:

- **Use Checklist Prompts:** "Here is a 3-step checklist. Complete Step 1, verify it works, then pause for my confirmation before Step 2."
- **Enforce State Dumps:** Before asking AG to build something complex, ask it: "Before you start, summarize your understanding of what we are building and what files you intend to touch." This immediately reveals if AG is on the wrong track.

---

**Summary:** You are managing a brilliant but overzealous engineer. Give it strict boundaries, clear context from the master SOPs, and never let it guess your intent.
