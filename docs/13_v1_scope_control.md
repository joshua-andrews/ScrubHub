# 🛑 V1 Scope Control

The number one reason AI-assisted apps fail is **overbuilding**. Since it's easy to ask AI to "add a chat feature," you end up with 20 half-finished features instead of 1 working app.

This document enforces a strict discipline for V1 (Version 1 / MVP).

---

## 1. The V1 Rulebook

When building the first version of an app to launch, you must abide by these constraints:

### A. Max 3 Core Features

An app should solve one primary problem.

- **Example:** A textbook scraper app needs: 1) Scraping, 2) Text Processing, 3) Displaying Posts.
- **Do not add:** AI avatars, dark/light mode toggles (pick one), complex notification systems, internal admin panels (use Supabase directly).

### B. "Ugly but Functional" Beats "Beautiful but Broken"

You cannot spend 3 days tweaking the drop-shadow on a button if the checkout flow doesn't process credit cards.

- UI Polish (`10_ui_polish_standards.md`) happens _after_ the raw data and logic are proven to work end-to-end.
- If Antigravity proposes adding complex GSAP/Framer Motion animations for V1, say: **"Stop. Remove animations. Keep it static for V1."**

### C. No "Premature Optimization"

Don't build infrastructure for 100,000 users when you have 0 users.

- Do not build a custom image CDN. Just use standard Supabase Storage URLs.
- Do not set up Redis caching unless the page explicitly takes >5 seconds to load.

## 2. Launching > Perfect

If the core value is delivered, launch it.

- **Rule:** If the user can pay you, use the core feature, and receive the result—it is ready to launch.
- Minor UI misalignments on obscure mobile screen sizes do not matter for V1.

## 3. Controlling Antigravity (AG)

AG is an enthusiastic AI. If you ask for a login screen, it might build a login screen with Google, Apple, Twitter, Facebook, and Magic Links.

**Enforce Scope in your prompt:**

> "Build the login page. **Scope constraint:** Only implement Email/Password login. Do not add OAuth providers or 'Forgot Password' flows for V1."
