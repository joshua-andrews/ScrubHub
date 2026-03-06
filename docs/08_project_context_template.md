# 🧠 Project Context Template

_(Copy this template into the `README.md` or a `project_context.md` file at the root of every new repository. This is the **Master System Prompt** that Antigravity reads instantly when you open a project)._

---

## Project Overview

**App Name:** [Insert Name]
**Description:** [Brief 2-3 sentence description of what the app does]
**Target Audience:** [Who is this for?]

## 🛠️ The Stack

- **Frontend:** Next.js (App Router), React, TypeScript
- **Styling:** Tailwind CSS, Lucide Icons
- **Backend:** Next.js Server Actions / API Routes
- **Database:** Supabase (PostgreSQL)
- **Auth:** Supabase Auth
- **Hosting:** Railway (or Vercel)

## 🎨 UI/UX Standards

Antigravity must adhere to `10_ui_polish_standards.md`:

- Clean, modern, premium design.
- Ample spacing, soft shadows, glassmorphism layers.
- Interactive hover/active states for all buttons.
- No default browser fonts or generic colors.

## 🤝 Project Rules & SOPs

Before writing code or solving problems, Antigravity should consult the documentation in the `/docs` folder:

1. **`00_using_antigravity_correctly.md`** - Keep solutions simple, step-by-step, and wait for approval on big refactors.
2. **`04_backend_implementation_guide.md`** - Draft logical maps before writing backend SQL/logic.
3. **`11_when_stuck_protocol.md`** - If stuck on an error for >15 mins, escalate to ChatGPT or Rollback. Never spin in circles.
4. **`09_emergency_recovery.md`** - If a major break occurs, do not guess. Guide me through `git restore` or `git reset`.

## 📍 Current Status

_(Update this section daily so AG knows exactly where we left off)._

- [x] Initialized Next.js
- [x] Connected Supabase
- [ ] Currently working on the User Onboarding Flow
- [ ] Next: Implement Stripe Checkout
