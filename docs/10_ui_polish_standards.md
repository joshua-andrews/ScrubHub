# UI Polish & Modern Design Standards ✨

This document enforces the visual quality of the application. Everything built by Antigravity must adhere to these standards. **Functional but ugly is not acceptable.**

---

## 1. The Core Aesthetic

The app must look premium, modern, and high-trust. It should feel like a top-tier SaaS product or a beloved consumer app (think Apple, Stripe, Linear).

### Key Themes:

- **Cleanliness:** Ample whitespace, no cluttered interfaces.
- **Depth:** Subtle use of shadows and layering (glassmorphism where appropriate).
- **Feedback:** Every interactive element must respond to the user (hover states, active states, micro-animations).

## 2. Spacing & Layout

- **Never use cramped spacing.**
- Use a consistent spacing scale (e.g., Tailwind's `p-4`, `p-6`, `p-8` spacing system).
- Instead of using a single giant container, use cards with subtle borders (`border-gray-200` or `border-white/10` in dark mode) to group information.

## 3. Typography

- **No default browser fonts.** Always use a modern, clean sans-serif (e.g., Inter, Roboto, SF Pro, or Outfit).
- **Hierarchy is critical:**
  - H1 headings should be large, bold, and sometimes feature a subtitle below them.
  - Body text should usually be a softer color (e.g., `text-gray-600` or `text-gray-400` in dark mode) rather than harsh pure black or pure white.
- **Line height:** Ensure readable line heights (e.g., `leading-relaxed`).

## 4. Modern UI Elements

When AG is generating UI components, it _must_ include these finishing touches:

### A. Glassmorphism & Blurs

- For overlays, sticky headers, or modals, use backdrop blur.
- Example Tailwind: `bg-white/70 backdrop-blur-md border border-white/20`.

### B. Gradients

- Avoid flat, generic colors (e.g., standard `#FF0000` red or `#0000FF` blue).
- Use subtle linear or radial gradients for primary buttons or hero backgrounds.
- Example Tailwind: `bg-gradient-to-r from-blue-500 to-indigo-600`.

### C. Shadows & Borders

- Use soft, diffused shadows, not harsh drops.
- `shadow-sm` for cards, `shadow-lg` for dropdowns/modals.
- Always combine soft shadows with a very subtle 1px border to give elements crisp edges.

## 5. Animations & Micro-Interactions

UI elements must feel alive:

- **Buttons:** Must have a hover state (slight opacity change or slight lift) and an active state (scale down slightly).
  - Example: `transition-all hover:-translate-y-0.5 active:translate-y-0`.
- **Page Transitions:** Ensure content fades in gracefully rather than snapping into place abruptly.
- **Loading States:** Never freeze the screen. Always show a beautiful spinner or skeleton loader.

## 6. Enforcing This Standard with AI

When asking AG to build or fix a UI component, always end your prompt with:

> "Ensure the design adheres strictly to the `10_ui_polish_standards.md`. It must have proper spacing, modern typography, hover states, and feel premium."
