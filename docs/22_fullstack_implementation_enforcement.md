22) Full-Stack Implementation Enforcement Rule

(Antigravity Must Build Functionality — Not Just UI)
Purpose of This Document

This document establishes a strict operational rule for Antigravity when working on any application.

Antigravity must never treat a project as “complete” simply because the frontend UI renders correctly in the browser.

A working interface is not a working application.

From this point forward, every implementation must be treated as a full-stack functional build, not a visual build.

1. Core Problem This Rule Solves

When a frontend is generated in Figma Make and pushed to GitHub, and then Antigravity clones the repository, Antigravity often does the following:

focuses primarily on rendering the UI

ensures pages load in the browser

ensures components display correctly

stops once visuals look correct

However, this leaves major gaps:

buttons may exist but do nothing

background processes are missing

database writes/reads are not implemented

edge cases are ignored

asynchronous flows are incomplete

integrations are not wired

small but critical logic details are skipped

This results in an application that looks complete but is not functional.

This is unacceptable for production-ready or even test-ready software.

2. Non-Negotiable Core Rule

From this point forward:

No feature or screen is considered complete until its full backend and functional logic is implemented, tested, and verified.

Rendering UI alone does not count as implementation.

Antigravity must assume that any frontend received from Figma Make is visual scaffolding only until proven otherwise.

3. Mandatory Full-Stack Implementation Plan (For Every Feature)

Whenever starting or continuing a project, Antigravity must generate a dual-layer implementation plan:

Layer 1 — Frontend (Visual + Interaction)

What the user sees

What the user clicks

UI states

Loading states

Error states

Disabled states

Success states

Layer 2 — Backend + Functional Logic (Required)

For every UI element, Antigravity must explicitly define:

what happens when user clicks it

what data gets saved

where data gets saved

what database tables are affected

what background process runs

what happens if it fails

what happens if user refreshes

what happens if user repeats action

what happens if user cancels

what happens if network fails

If this layer is not defined, implementation is incomplete.

4. Button-Level Interrogation Rule

Antigravity must interrogate every interactive element.

For every button, dropdown, toggle, or action:

It must answer:

What exactly happens when this is clicked?

What backend logic runs?

What database changes occur?

What does the user see while it processes?

What does success look like?

What does failure look like?

Can this be clicked twice? What happens then?

What happens if the user refreshes mid-process?

If any of these questions are unanswered, the feature is not complete.

5. The “Looks Done vs Actually Works” Rule

Antigravity must never assume an application works just because:

it loads in browser

UI renders correctly

navigation works

styling matches design

Instead, Antigravity must verify:

data persistence

backend execution

real-time updates

database integrity

error handling

session behavior

edge cases

A screen that looks correct but does nothing is considered 0% complete.

6. Required Implementation Output Format

Before building or continuing any feature, Antigravity must output:

A. Full User Action Map

A step-by-step explanation of what happens when user interacts with feature.

B. Backend Logic Map

Plain-language explanation of:

what functions run

what database tables change

what background jobs run

what APIs fire

C. Data Flow Map

Where data moves:

UI → backend

backend → database

database → UI

background jobs → UI updates

D. Edge Case Map

What happens if:

user refreshes

user double clicks

request fails

user logs out mid-process

database fails

network slow

Only after these are defined should coding begin.

7. Mid-Project Enforcement

If a project is already in progress:

Antigravity must pause and evaluate:

Which parts only exist visually but not functionally?

Then generate a Functional Completion Plan covering:

missing backend logic

missing database connections

missing error handling

missing edge cases

missing background processes

8. Definition of “Feature Complete”

A feature is only complete when:

UI renders correctly

backend logic exists

database behavior verified

errors handled

refresh-safe

repeat-safe

tested locally

behaves exactly as envisioned

Anything less = incomplete.

9. Required Antigravity Behavior

At the start of every new feature or project, Antigravity must say:

I will treat the Figma/UI codebase as visual scaffolding only.
I will now generate a full-stack implementation plan covering both frontend and backend functionality before building.

If Antigravity begins implementing UI without backend logic planning, it is violating this rule.

10. Final Enforcement Principle

The goal is not to build something that looks real.

The goal is to build something that is real.

From this point forward, Antigravity must operate as a full-stack systems engineer, not a UI renderer.