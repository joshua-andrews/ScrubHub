# 🎨 Figma-to-Code SOP: Achieving 100% Visual Parity

A common frustrating problem is when Figma looks like a $1B startup, but the Antigravity implementation looks like a 2010 dashboard.

This SOP explains exactly why that mismatch happens and how to close the gap from 80% to 100%.

---

## 1. Why the Mismatch Happens

When AI tools translate Figma to code, they often:

1. **Lose subtleties:** They drop the `box-shadow`, make gradients flat colors, or ignore `backdrop-blur`.
2. **Guess at spacing:** They default to `p-4` instead of reading the exact padding in Figma.
3. **Use default fonts:** Figma's beautiful Inter font gets replaced by standard browser Arial.

## 2. The Solution: The "Polish Pass" Protocol

Do not expect AG to get it 100% right on the first try. You must enforce a two-step process.

### Step 1: Structural Build (The 80%)

Let AG build the component to get the layout and logic working.

- **Prompt:** "Build the Dashboard Header based on the Figma documentation. Focus on getting the grid layout and flexbox behavior correct."
- _Do not complain about colors or spacing yet._

### Step 2: The Polish Pass (The Final 20%)

Once the layout is structurally correct, you run the Polish Pass.

- **Prompt AG:** \*"The structure is good, but it looks visually flat. I need you to do a strict Polish Pass based on `10_ui_polish_standards.md`. Specifically:
  1. Add the exact soft shadows from the design.
  2. Implement the hover states on these buttons.
  3. Fix the padding so it feels less cramped.
     Do not change any logic, only update Tailwind classes."\*

## 3. Best Practices for Figma Exporting

When exporting your documentation from Figma Make:

- Explicitly tell Figma Make: _"Generate a `styles_guide.md` that lists out all the exact hex codes, border radiuses, and shadow values used in this design."_
- Give that `styles_guide.md` directly to Antigravity before it writes a single line of CSS.

## 4. The "Inspect Element" Hack

If AG keeps failing to replicate a subtle blur or shadow:

1. Open Figma in your browser.
2. Go to "Dev Mode" (or right-click the element and select "Copy as CSS").
3. Paste that exact CSS snippet to AG.
4. Tell AG: _"Convert this exact CSS into standard Tailwind classes and apply it to the component."_
