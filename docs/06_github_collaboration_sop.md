# 🤝 Team Collaboration & GitHub SOP

Working on a team (e.g., you + Genesis) introduces the risk of code conflicts and breaking production. This SOP defines a beginner-safe GitHub workflow to ensure nobody ever breaks the main app.

---

## 1. The Golden Rule of `main`

The `main` branch is sacred. It represents the production app.

- **You absolutely NEVER push code directly to `main`.**
- If you push a bug to `main`, the live app breaks for all users.

## 2. Branching Strategy (Feature Branches)

Every new feature, bug fix, or UI change gets its own branch.

### Creating a Branch

Before you or Genesis write any code, create a branch in the terminal:

```bash
git checkout main
git pull            # Get the latest code
git checkout -b feature/user-profile-ui
```

_(Naming convention: `feature/name-of-feature` or `bugfix/what-is-broken`)_

## 3. The Safe Push/Pull Strategy

Once you finish your feature on your branch:

1. **Commit your work:**
   ```bash
   git add .
   git commit -m "Built the user profile UI"
   ```
2. **Push your branch to GitHub:**
   ```bash
   git push origin feature/user-profile-ui
   ```
3. **Open a Pull Request (PR):**
   - Go to GitHub in your browser.
   - You will see a green button to "Compare & pull request". Click it.
   - Describe what the code does.

## 4. Code Review & Merging

- Before merging, the other person (e.g., Genesis creates the PR, you review it) should look at the code.
- You can pull their branch locally to test it:
  ```bash
  git fetch
  git checkout feature/their-branch-name
  npm run dev
  ```
- If it works perfectly locally, go to GitHub, click "Approve", and click "Merge pull request".
- The code is now safely in `main`.

## 5. "Do Not Break Production" Safeguards

To prevent accidents, set up Branch Protection rules in GitHub:

1. Go to your GitHub Repo -> Settings -> Branches.
2. Click "Add branch protection rule".
3. Branch name pattern: `main`.
4. Check **"Require a pull request before merging"**.
5. Check **"Require approvals"** (Set to 1).
   _(This physically prevents anyone from accidentally pushing directly to `main` without a reviewed PR)._
