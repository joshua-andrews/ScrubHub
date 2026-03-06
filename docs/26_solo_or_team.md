🧭 Project Mode Detection Rule (Team vs Solo)

Before beginning any implementation, modification, or push, Antigravity must determine whether the current project is a team collaboration project or a solo project.

This prevents unnecessary conflict scanning on solo builds while enforcing strict protection on shared builds.

🟢 Step 0 — One-Time Project Mode Confirmation (Per Session)

At the start of a new project session OR when entering a project for the first time, Antigravity must ask:

"Is this a team project with Genesis and Josh collaborating, or a solo project with Josh only?"

Antigravity must then WAIT for confirmation.

🔒 Ask Once Rule

Antigravity must ask this question only once per session or project start.

Once the user confirms:

Team Project
or

Solo Project

Antigravity must store this mode for the entire session and must NOT repeatedly ask again unless:

A new session begins

A new project/repository begins

The user explicitly changes project mode

🏷️ Required Confirmation Message

After user confirms the project type, Antigravity must reply with a clear verification statement:

If TEAM project:

"Confirmed: This is a TEAM collaboration project.
Activating full Global Conflict Prevention Protocol for this session."

If SOLO project:

"Confirmed: This is a SOLO project (Josh only).
Running standard safety protections without teammate conflict scanning."

This confirmation locks the mode for the session.

🧠 Persistent Session Awareness Rule

For the remainder of the session:

Antigravity must remember the confirmed mode and operate under it without re-asking.

Team Mode → Full protection active

Cross-branch checks

Supabase/schema validation

Backend/frontend compatibility

Railway/background job checks

Env alignment

Safe merge enforcement

Solo Mode → Standard protection active

No teammate branch scanning

No Genesis conflict checks

Still protect database + infrastructure

Still confirm before major refactors

Antigravity must not repeatedly ask which mode is active during normal workflow.

👥 If Team Project (Collaboration Mode)

If confirmed as a team project, Antigravity must:

Activate the Global Conflict Prevention & Safe Merge SOP fully.

Assume:

Multiple people may modify any part of the system at any time.

All protection protocols apply.

Example active team projects:

R3 Genesis

Any future shared builds

Any repo where Genesis & Josh both contribute

🧑‍💻 If Solo Project (Josh Only)

If confirmed as solo:

Antigravity may:

Skip cross-branch teammate scans

Skip Genesis branch comparisons

But must still:

Protect database integrity

Protect env variables

Prevent destructive schema changes

Confirm before major refactors

Follow backend safety SOPs

Solo mode removes team conflict checks,
but does NOT remove system safety.

🔄 Switching Modes Mid-Project

If the user indicates the project status has changed:

Example:

“Genesis is joining this project now”

Antigravity must respond:

"Understood. Switching project to TEAM collaboration mode.
Activating full conflict-prevention safeguards."

Then remain in that mode for the rest of the session.

🛑 Absolute Rule

Antigravity must never assume project type.

It must confirm once, lock it for the session, and operate accordingly.

This prevents:

Repetitive questioning

Workflow interruptions

Accidental overwrites

Silent branch conflicts

Backend/frontend mismatches

Production breakages

🏁 System Principle

Ask once → Confirm → Lock mode → Operate safely.

Not:
Ask every 5 minutes.
