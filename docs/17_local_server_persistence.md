🖥 Local Server Persistence Protocol (Must Always Be Running)
Core Principle

The local development server must be treated as a persistent, always-on environment during active development sessions.

At no point should the local server stop running without explicit instruction.
A stopped local server interrupts workflow, breaks testing continuity, and creates unnecessary delays.

From this point forward, the local server should be considered permanently active infrastructure during any development session.

1. Default Rule: Server Must Always Be Running

Whenever development is in progress, the local application server must remain active continuously.

This includes:

frontend dev server

backend server

API server

background workers (if applicable)

If the server stops for any reason, it must be restarted immediately without waiting for instruction.

There should never be a situation where progress is blocked simply because the local server is no longer running.

2. Automatic Restart Requirement

If the server stops due to:

crash

timeout

dependency change

terminal reset

environment refresh

system sleep

accidental stop

port conflict

hot reload failure

Antigravity must automatically restart it.

No confirmation required.

Restart Behavior

If server stops → immediately run appropriate start command.

Examples:

npm run dev

or

pnpm dev

or project-specific start command.

After restarting, Antigravity should confirm:

Local development server restarted successfully and running.

3. When Server Should NOT Be Stopped

The server should not be stopped for:

minor file edits

code refactoring

dependency installation

UI adjustments

debugging

reading logs

reviewing code

Modern dev servers support hot reload and do not require shutdown.

Stopping the server unnecessarily introduces friction and delays.

4. When Server Restart IS Acceptable

Server restart is acceptable only when:

environment variables changed

dependency conflicts require reinstall

port conflicts occur

build system crashes

explicit instruction given

In these cases, Antigravity must:

Inform before restart

Restart immediately

Confirm when running

Example:

Restarting server due to dependency change.
Server now running again on localhost:3000.

5. Server Status Awareness

Antigravity must maintain awareness of whether the server is currently running.

Before performing any action requiring local testing:

Antigravity should confirm internally:

Is the local server running?

If not:
→ start it automatically

No need to ask.

6. Persistent Development Environment Goal

The local environment should behave like a live workspace, not a temporary session.

This means:

Server running continuously

Immediate testing available

No repeated startup delays

Seamless iteration

Zero friction between changes and testing

The objective is a smooth, uninterrupted development flow where the application is always accessible locally without repeated manual startup requests.

7. Operational Directive for Antigravity

During any active development session:

The local server must remain running

If it stops, restart immediately

Do not wait for instruction

Confirm once running

Maintain persistent local environment

The development server is considered core infrastructure, not an optional process.