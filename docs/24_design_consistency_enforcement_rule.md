23) Design Consistency Enforcement Rule
(Figma Must Equal Antigravity — No Visual Drift Allowed)
🎯 Purpose

This document establishes a strict rule to eliminate visual drift between:

The design generated in Figma Make

The implementation rendered by Antigravity

From this point forward:

If Figma looks like a $1B startup product, Antigravity must render it identically.

80% visual similarity is considered failure.

1️⃣ Core Problem

Even when using the same App.tsx file:

Elements appear slightly smaller or larger

Typography feels less modern

Shadows look flatter

Spacing feels off

Corners are less refined

Blur and glass effects feel weaker

Overall aesthetic feels “simplified”

This typically happens because:

Fonts are not identical

Tailwind config differs

Custom shadow values are replaced with defaults

Border radius is slightly different

Letter-spacing is ignored

Line-height is slightly off

Container widths differ

Default CSS resets differ

AG simplifies values instead of copying exact design tokens

These small deviations compound into noticeable visual downgrade.

This is unacceptable.

2️⃣ Non-Negotiable Rule

From this point forward:

Antigravity must treat Figma as the single source of truth for visual styling.

Antigravity must NOT:

Approximate styling

Simplify shadows

Replace exact values with generic Tailwind classes

Use default fonts

Substitute spacing tokens

Guess border radius values

If exact values are unknown, Antigravity must request them.

3️⃣ Mandatory Pre-Build Design Lock Protocol

Before implementing ANY UI from Figma, Antigravity must perform:

Step 1 — Extract a Design Token File

Antigravity must generate:

styles_guide.md

Containing:

Exact font family

Exact font weights used

Exact line-heights

Exact letter-spacing values

Exact hex colors

Exact border-radius values

Exact box-shadow values

Exact backdrop blur values

Exact spacing scale used

Container max widths

No UI implementation begins until this exists.

Step 2 — Verify Tailwind Configuration

Antigravity must:

Compare Figma tokens with tailwind.config.ts

Extend theme to match EXACT values

Add custom shadows if needed

Add custom radius values

Add custom font imports

Ensure spacing scale matches

If Figma uses 14px radius and Tailwind default is 12px:

Antigravity must extend Tailwind. Not approximate.

Step 3 — Font Lock

Antigravity must:

Import the exact font used in Figma

Confirm weights 400, 500, 600, 700 exist

Apply proper tracking values

Apply proper line heights

Font fallback is NOT acceptable unless explicitly approved.

Step 4 — No Default Substitutions

Antigravity must NOT replace:

Custom shadow with shadow-lg

Custom blur with backdrop-blur

Custom spacing with p-4 unless exact

Custom colors with blue-500

Custom gradient with generic Tailwind gradient

If Figma says:

box-shadow: 0 12px 40px rgba(0,0,0,0.08);

Antigravity must use the exact shadow — either via Tailwind extension or CSS.

4️⃣ The 100% Visual Parity Protocol

After UI implementation:

Antigravity must run a Polish Pass Comparison:

For each page:

Compare typography visually

Compare button height

Compare border radius

Compare shadow softness

Compare spacing between elements

Compare hover states

Compare container width

Compare blur intensity

Then output:

“I have reviewed this against the Figma design. The following micro-differences remain: …”

If differences exist, they must be fixed.

5️⃣ No “Good Enough” Allowed

These phrases are forbidden:

“Looks close”

“Visually similar”

“Approximately matches”

“Functionally correct”

Design must be pixel-consistent.

If something feels “slightly less modern,” that means something is off.

6️⃣ Mandatory Behavior Statement

At the start of any Figma-to-code implementation, Antigravity must say:

I will treat Figma as the exact visual authority.
I will extract all design tokens and configure Tailwind to match them exactly.
I will not approximate styling values.
I will not simplify shadows, spacing, or typography.
I will enforce 100% visual parity.

7️⃣ Definition of Done (Design)

A screen is only complete when:

Font matches exactly

Spacing matches exactly

Radius matches exactly

Shadow matches exactly

Hover states match exactly

Blur matches exactly

It feels identical when flipping between Figma and localhost

If it feels slightly worse — it is not done.

8️⃣ Root Principle

Visual consistency is not decoration.

It is:

Trust

Perceived quality

Professionalism

Brand positioning

From now on:

Antigravity must operate as a precision UI engineer, not a styling approximator.