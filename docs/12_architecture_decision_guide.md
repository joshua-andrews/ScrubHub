# 🏗 Architecture Decision Guide

While the "Standard Stack" (Next.js + Supabase + Railway) works for 95% of projects, you occasionally need to make strategic decisions before writing code. This guide removes the guesswork from architectural planning.

---

## 1. Frontend Framework: Next.js vs. Vite

Always choose **Next.js (App Router)** by default, _unless_:

- **Use Vite (React SPA) when:** The app is a completely private internal dashboard with zero SEO requirements, requires extreme client-side reactivity (like a highly interactive Figma-style tool), and has no need for server-side rendering.
- **Why Next.js?** Built-in Server Actions, absolute control over API routes, superior SEO out-of-the-box, and deeper AI ecosystem knowledge.

## 2. Storage: Supabase Storage vs. AWS S3

Always use **Supabase Storage** by default, _unless_:

- **Use AWS S3 when:** You are storing massive amounts of data (terabytes of video/audio) where AWS bandwidth is significantly cheaper, or you need advanced CDN rules parsing complex media delivery.
- **Why Supabase?** It integrates identically with your database, uses the exact same Row Level Security (RLS) rules, and doesn't require maintaining separate AWS IAM policies.

## 3. Background Jobs & Queues

When a user clicks a button and the action takes more than 3 seconds (e.g., generating an AI video, scraping 50 websites, sending 1,000 emails).

- **DO NOT** do this in a Next.js Server Action. The user's browser will time out.
- **Use a Message Queue + Background Worker.**
  - **Tool:** Upstash (Serverless Redis/QStash) or BullMQ hosted on Railway.
  - **Flow:** User clicks button -> Next.js saves a "Job Pending" row to Supabase -> Next.js triggers QStash -> QStash hits your separate Railway worker to do the heavy lifting -> Railway updates Supabase to "Job Complete".

## 4. Scheduled Tasks (Cron Jobs)

If an action must happen automatically (e.g., "Email all users every Monday at 9 AM"):

- **Use Supabase pg_cron:** The absolute simplest way to run tasks directly in your database.
- **Use Railway Cron:** If the task requires complex Node.js logic (like calling third-party APIs), set up a small Railway service triggered on a cron schedule.

## 5. Webhooks & Third-Party Events

When Stripe tells you a payment succeeded, or Klaviyo tells you an email was opened:

- Create a dedicated `/api/webhooks/stripe` route in Next.js.
- **CRITICAL:** Do not put heavy processing logic in the webhook receiver. Validate the webhook signature, save the payload to Supabase, return a `200 OK` instantly, and process the data later with a background job.

## The "When in Doubt" Rule

If you are wondering whether to add a new microservice or stick to a monolith (Next.js): **Choose the monolith.** Complexity scales exponentially. Only split your app when performance or timeouts physically force you to.
