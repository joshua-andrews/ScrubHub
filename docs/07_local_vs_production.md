# 🌍 Local vs. Production Workflow

Beginners often confuse exactly _where_ their code lives. This document clarifies the three environments and when to push code between them.

---

## The Three Environments

### 1. Local (Your Computer)

- **What it is:** The code running on your machine (`localhost:3000`).
- **Purpose:** Fast feedback. If you break it, nobody sees it.
- **Rule:** Write, test, and break all new features here.

### 2. GitHub (The Vault)

- **What it is:** The remote storage for your code.
- **Purpose:** Backup, history, and collaboration.
- **Rule:** Never edit code directly in the GitHub UI. GitHub is for reading and reviewing, not writing.

### 3. Production (The Internet)

- **What it is:** The live app hosted on Railway or Vercel (e.g., `myapp.com`).
- **Purpose:** Real users.
- **Rule:** If it's not 100% tested locally, it does not go to production.

---

## 📅 The Best-Practice Cadence

### Every Hour: Commit Locally

When a small piece of a feature works, save it locally.

```bash
git add .
git commit -m "added the login button"
```

_Why? If you break the app 10 minutes later, you can restore to this working commit._

### Every Day / End of Session: Push to GitHub

At the end of your coding session, push your branch to GitHub.

```bash
git push origin feature/my-branch
```

_Why? If your computer dies, your code is safe in the cloud._

### When a Feature is 100% Done: Merge & Deploy

Only once the feature is fully tested locally, open a PR on GitHub, merge it to `main`, and let Railway auto-deploy it.

---

## 🚫 What NEVER to do

1. **Never commit `.env` files.** They contain your secret passwords. Git ignores them by default (via `.gitignore`), but never force add them.
2. **Never commit `node_modules`.** This folder is huge and generates automatically.
3. **Never test in Production.** "I'll just see if it works live" is how databases get wiped. Test on localhost first.
