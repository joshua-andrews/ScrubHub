# 🛠 The Standard Tech Stack Guide

For 95% of the applications you build, the technology stack will be identical. A standardized stack means you never have to guess how to deploy, authenticate, or store data.

**The Standard Stack:**

- **Frontend/Framework:** React + Next.js (or Vite if it's a simple Single Page App)
- **Styling:** Tailwind CSS (Vanilla CSS is fine, but Tailwind is faster for AI)
- **Backend & Database:** Supabase (PostgreSQL)
- **Authentication:** Supabase Auth
- **Hosting:** Railway (or Vercel for purely frontend apps)

---

## 1. Local Project Initialization

When starting a new app, Antigravity should run this exact flow:

1. `npx create-next-app@latest my-app-name`
2. Select: TypeScript = Yes, ESLint = Yes, Tailwind CSS = Yes, `src/` directory = Yes, App Router = Yes.
3. `cd my-app-name`
4. `npm install @supabase/supabase-js lucide-react` _(Lucide is standard for modern icons)_.

## 2. Supabase Setup (Database & Auth)

Supabase handles all data and user accounts.

### A. Creating the Project

1. Log into Supabase dashboard.
2. Click "New Project". Give it the name of your app.
3. Save the **URL** and **anon public API key**.
4. In your local code, create a `.env.local` file and add:
   ```env
   NEXT_PUBLIC_SUPABASE_URL=your-supabase-url
   NEXT_PUBLIC_SUPABASE_ANON_KEY=your-supabase-key
   ```

### B. Setting up Authentication

1. Go to Authentication -> Providers in Supabase.
2. Enable Email (turn off "Confirm email" for faster development testing).
3. If using Google Auth, you need to set up the Google Cloud Console OAuth credentials and paste them here.

### C. Database Tables & RLS

1. Go to the SQL Editor in Supabase.
2. ALWAYS create tables using Antigravity-generated SQL scripts. Do not try to click around the UI to build complex tables.
3. **CRITICAL:** Always enable Row Level Security (RLS).
   - Ask Antigravity: "Write the RLS policies to ensure users can only see their own data."

## 3. Hosting on Railway

Railway is perfect for full-stack apps with custom backends or background jobs.

1. Go to Railway.app and login with GitHub.
2. Click "New Project" -> "Deploy from GitHub repo".
3. Select your application repository.
4. **Environment Variables:** Railway needs the exact same `.env.local` variables you use locally. Go to the "Variables" tab in Railway and paste your Supabase URL and Key.
5. Railway will automatically build and deploy.

### (Alternative) Vercel for Next.js Apps

If it is a pure Next.js application, Vercel is often faster:

1. Go to Vercel.com -> "Add New Project".
2. Import from GitHub.
3. Paste Environment Variables.
4. Deploy.

## 4. Why This Stack?

- **Speed:** Next.js + Tailwind lets you build UIs in hours.
- **Power:** Supabase gives you a real PostgreSQL database, not a toy NoSQL database.
- **AI-Friendly:** Antigravity and ChatGPT know Next.js + Supabase incredibly well. They rarely hallucinate code for this stack.
