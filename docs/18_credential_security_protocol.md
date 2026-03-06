🔐 Credential & Secret Management Protocol

This document defines strict rules for handling sensitive information during development.
Security is not optional. Even in development environments, poor secret handling creates long-term risk.

From this point forward, these rules apply to all projects.

1. Absolute Rule: Never Reveal Sensitive Credentials in Chat

Under no circumstances should sensitive credentials be written directly in:

Chat conversations

Code snippets shown in chat

Git commit messages

Pull request descriptions

Markdown documentation

Comments in code

Screenshots

Logs shared publicly

Sensitive credentials include:

API keys

Database passwords

Supabase service keys

Stripe secret keys

OAuth client secrets

JWT secrets

Private keys

AWS credentials

Webhook signing secrets

SMTP credentials

Any production tokens

If a credential must be referenced, it should always appear in placeholder format.

Example:

SUPABASE_URL=your-supabase-url
SUPABASE_ANON_KEY=your-anon-key

Never paste real values.

2. All Secrets Must Live in Environment Files

All credentials must be stored in:

.env.local (for local development)

.env.production (for deployment)

Railway/Vercel environment variable dashboard

Secure secret manager

Never hardcode secrets directly in code.

Incorrect:

const supabase = createClient("https://abc.supabase.co", "real-secret-key")

Correct:

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
)
3. Never Repeat Secret Values

If a credential is provided once, it must not be repeated in chat.

Antigravity must:

Acknowledge the credential

Confirm it has been stored in .env

Never echo the value back

Example acceptable response:

Supabase URL and key received and stored in .env.local. I will reference them via environment variables only.

Not acceptable:

Your Supabase key is: sk-xyz-123...

Even partial repetition of keys is not allowed.

4. Git Ignore Enforcement

Sensitive files must never be committed to Git.

The following must be included in .gitignore:

.env
.env.local
.env.production
.env.*.local
node_modules

If .env files are accidentally staged, Antigravity must immediately stop and warn:

Sensitive file detected in staging. Removing from commit.

5. Public vs Private Environment Variables

Understand the distinction:

Public Variables

Prefixed with:

NEXT_PUBLIC_

These are exposed to the browser and must not contain secrets.

Only safe-to-expose values go here:

Public Supabase URL

Public anon key

Feature flags

Private Variables

Stored without public prefix and accessed server-side only.

Never expose:

Service role keys

Secret API keys

Stripe secret key

Webhook secrets

If uncertain whether a key is safe to expose, assume it is NOT safe.

6. Production Safety Rules

Before deploying:

Antigravity must confirm:

All secrets are stored in platform environment variables

No secrets are hardcoded

No .env files are committed

No console logs print secret values

No error responses expose keys

7. Accidental Exposure Protocol

If a secret is accidentally exposed in chat or committed:

Immediate steps:

Rotate the key in the provider dashboard.

Generate a new secret.

Replace the old key in environment variables.

Remove the key from commit history if necessary.

Confirm the old key is fully invalidated.

Never assume exposure is harmless.

8. Antigravity Operational Directive

Antigravity must operate under these rules:

Never display secrets

Never repeat secrets

Always use .env

Always enforce .gitignore

Always warn if sensitive data appears staged

Always treat credentials as confidential

Security Confirmation Statement

At the start of any project involving credentials, Antigravity should operate under this principle:

All sensitive data will be stored exclusively in environment variables.
No secrets will be revealed in chat.
Git commits will exclude all sensitive files.
Credential security enforced at all times.

You’re now building like a serious technical founder.

This level of operational discipline is what separates:

hobby projects
from

real scalable systems.