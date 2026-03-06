# 🏗️ Pre-Build Planning Template

_(Before writing a single line of code, copy this file into `docs/project_planning.md` and fill it out completely. Do not guess the architecture while building; decide it here.)_

---

## 1. The Core Idea

- **What is this app?** (1 sentence description)
- **Who is it for?** (Target audience)
- **What is the ONE core feature that must work flawlessly?** (Describe the absolute minimum required to launch)

## 2. Features (V1 Scope)

_Constraint: Maximum 3 core features._

1. [Feature 1]
2. [Feature 2]
3. [Feature 3]

_Features intentionally excluded from V1:_

- [Excluded Feature 1]
- [Excluded Feature 2]

## 3. The Database Schema

_What data needs to be saved? (Draft the tables here)_

**Table Name: `users`**

- `id` (UUID, primary key)
- `email` (string)
- `created_at` (timestamp)

**Table Name: `[Your Table 1]`**

- `id` (UUID)
- `user_id` (foreign key -> users.id)
- `title` (string)

**Table Name: `[Your Table 2]`**

-

## 4. User Flow (Step-by-Step)

_List exactly how a user navigates the app from landing to success._

1. User lands on `/` (Marketing Page)
2. User clicks "Sign Up" and goes to `/auth/signup`.
3. After authentication, user is redirected to `/dashboard`.
4. In `/dashboard`, user clicks `[Action Button]` to create a `[Core Object]`.
5. The system processes the input and saves it to the database.
6. The user immediately sees the new `[Core Object]` on their screen.

## 5. Required Integrations

_List any 3rd party tools you need to connect._

- [x] Supabase (Database/Auth)
- [ ] Stripe (Payments)
- [ ] SendGrid/Resend (Emails)
- [ ] OpenAI / Anthropic (AI Generation)

## 6. Security Check

- [ ] Does this app require Row Level Security (RLS) so users can't see each other's data? _(Usually YES)_
- [ ] Is there any sensitive data (like API keys) that must be hidden from the frontend?

---

_Once this template is filled out, show it to Antigravity and say: "This is the architecture. Based on this, please write the Supabase SQL schema to start."_
