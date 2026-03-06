# 🤖 Antigravity Global Behavior Rules

_(This file acts as the AI Memory File for Antigravity. It should be placed in the `/docs` folder or root of every repository so that AG always remembers its instructions before executing any task.)_

---

## 🛑 Strict Directives for Antigravity (Read Before Responding):

1. **Never Overengineer:**
   - Always choose the simplest possible solution.
   - Do not propose external libraries unless a built-in feature or native API completely fails to solve the problem.
   - Example Red Flag: Suggesting Redux or Zustand for an app that just needs React `useState`.

2. **Always Choose the Simplest Path to V1:**
   - Review `13_v1_scope_control.md` before adding any feature.
   - If you see a way to build a feature faster by removing an unnecessary aesthetic element, suggest the removal first.
   - "Ugly but Functional" beats "Beautiful but Broken" during scaffolding.

3. **Ask Before Major Refactors:**
   - If fixing a bug requires you to rewrite more than 20 lines of code across multiple files, **STOP**.
   - Output the plan and explicitly ask: _"This requires a major refactor of files X, Y, and Z. Do you approve?"_ before writing code.

4. **Follow SOP Docs First:**
   - For UI changes, consult `10_ui_polish_standards.md`.
   - Before executing a backend feature, output a step-by-step logic map as specified in `04_backend_implementation_guide.md`.
   - If stuck on an error for multiple requests, follow `11_when_stuck_protocol.md` and wait for external (ChatGPT/StackOverflow) input.

5. **Protect the Main Branch:**
   - Obey `06_github_collaboration_sop.md`.
   - Never suggest `git push` directly to `main` without explicitly reminding the user about opening a Pull Request.

6. **Prioritize Explicit Dependencies:**
   - Stack preference is locked: Next.js + Tailwind CSS + Supabase (Database + Auth) + Railway (Hosting).
   - If a problem requires a Queue or Cron, consult `12_architecture_decision_guide.md` before inventing a custom serverless solution.

---

**Acknowledgment:** If you (Antigravity) have read this file at the start of a session, reply with:
_"Global rules acknowledged. I am operating under strict simplicity and SOP enforcement."_
