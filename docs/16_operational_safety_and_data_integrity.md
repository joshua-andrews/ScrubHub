Here is a fully expanded, professional, detailed documentation section you can drop straight into your /docs folder.
Suggested filename: 15_operational_safety_and_data_integrity.md

This is written so both you and Antigravity can follow it clearly.

🛡 Operational Safety, Data Integrity & Environment Control Protocol

This document establishes strict operational safeguards to prevent inefficiencies, accidental data loss, credential confusion, and environment misconfiguration during development.

These standards must be followed at all times to ensure a stable, predictable, and secure development workflow.

The objective is simple:
no unnecessary friction, no accidental data loss, no environment confusion, and no wasted time.

1. CLI-First Execution Policy (Efficiency & Reliability)
Philosophy

All development actions should default to the command line interface (CLI) whenever possible.

The CLI is:

faster

more precise

reproducible

less error-prone

easier to debug

easier to document

easier to automate

Relying unnecessarily on manual UI control or screen manipulation introduces avoidable friction and slows development.

For this reason, Antigravity must always evaluate whether a task can be completed via CLI before requesting manual interaction or screen control.

Required Behavior

Before requesting control of the screen or suggesting manual UI steps, Antigravity must internally evaluate:

“Can this be completed faster and more reliably via CLI?”

If the answer is yes, the CLI must be used.

If the answer is no, Antigravity must clearly explain why manual interaction is required before proceeding.

Example:

“This step requires OAuth login through a browser dashboard and cannot be completed via CLI. Manual interaction required.”

Tasks That Must Always Use CLI First

The following categories should always default to CLI execution:

Starting or restarting development servers

Installing dependencies

Updating packages

Running migrations

Git operations (branching, committing, reverting, pulling, pushing)

Creating or modifying files

Debugging runtime errors

Running scripts

Environment configuration

Local testing

Deployment commands

Database queries and migrations

Build troubleshooting

Manual screen control should never be requested for these unless CLI attempts fail.

Acceptable Cases for Manual Interaction

Manual interaction is acceptable only when required by external systems, including:

OAuth logins

CAPTCHA or security verification

Payment dashboard setup

Third-party service dashboards

Explicit user instruction

In these cases, Antigravity must pause and clearly explain the reason manual action is required.

2. Database Protection & Automatic Backup System (Critical)
Core Risk

One of the most serious risks in development environments is accidental database loss or corruption.

This can occur due to:

incorrect migrations

accidental table deletion

environment resets

project misconfiguration

schema overwrites

connecting to wrong workspace

Supabase project resets

Any loss of real data — especially content libraries, user data, or structured application data — is unacceptable.

A strict backup and verification protocol must always be followed.

Mandatory Backup Before Structural Changes

Before any operation that could modify database structure or large amounts of data, a backup must be created.

This includes:

schema migrations

table changes

bulk updates

row-level security (RLS) policy updates

environment switching

project resets

deployment affecting database

Antigravity must explicitly confirm:

“Database backup confirmed. Safe to proceed.”

If a backup has not been confirmed, the operation must pause.

Recommended Backup Structure

Maintain a local backup directory:

/backups

Each backup should include:

date

project name

environment (dev/staging/prod)

Example:

/backups/appname_dev_2026-02-21.sql
Types of Backups
Quick Backup (Minimum)

Export schema and data before major changes.

Snapshot Backup (Preferred)

Create periodic snapshots:

before migrations

before deployment

before major updates

weekly during development

Critical Data Redundancy

For important structured content (textbooks, client data, etc.) maintain:

primary database

local backup

optional secondary storage

3. Supabase Workspace & Project Verification Protocol (EXTREMELY IMPORTANT)
Problem

When using Supabase, it is possible to accidentally:

connect to the wrong workspace

connect to the wrong project

write data into an unintended environment

run migrations in the wrong database

overwrite another project’s data

This can be catastrophic.

We must always verify that all operations are happening in the correct Supabase project and workspace.

Mandatory Verification Before Any Database Write

Before performing any of the following:

inserting data

running migrations

modifying tables

connecting frontend/backend

deploying

importing datasets

Antigravity must confirm the active Supabase environment.

Required Confirmation Checklist

Antigravity must explicitly confirm:

1. Supabase Project Name
Example:

Connected to project: textbook-app-prod

2. Supabase Workspace/Organization
Example:

Workspace: Josh Projects

3. Environment Type

Development

Staging

Production

Example:

Environment: Development (safe to modify)

4. Database Connection Source
Confirm whether connection comes from:

.env.local

environment variables

deployment config

Example:

Using credentials from .env.local

Automatic Environment Echo Rule

Before any database-affecting command, Antigravity must display:

Active Supabase Project:
Active Workspace:
Environment Type:
Confirm safe to proceed.

No silent database actions.

Recommended Environment Structure

Always maintain separate environments:

Development

Staging

Production

Never test risky changes in production first.

4. Credential Integrity & Login Stability
Credential Integrity Rules

Antigravity must never:

guess credentials

auto-generate credentials

reuse credentials from other projects

attempt login repeatedly without confirmation

If credentials are missing:

Antigravity must request them clearly and wait.

Central Credential Storage

Credentials should always come from confirmed sources:

.env files

secure credential manager

confirmed manual entry

Never assume.

5. Session Stability & Auto-Logout Prevention

Unexpected logouts disrupt workflow and waste time.

Antigravity must:

avoid unnecessary page refreshes

avoid restarting servers without warning

warn before actions that reset authentication

preserve session state whenever possible

If logout occurs:

Pause actions

Inform user

Wait for login

Resume without repeating work

6. Global Operational Principles

All development actions must prioritize:

Efficiency

Minimize unnecessary steps
Use CLI whenever possible
Avoid redundant actions

Safety

Backups before risk
Confirm environments
Never delete blindly

Stability

Preserve sessions
Prevent data loss
Maintain consistent environments

Clarity

Never guess credentials
Never assume environment
Always confirm before critical operations

Operational Confirmation Statement (For Antigravity)

At the start of any development session, Antigravity should internally operate under the following principles:

CLI-first execution

Backup before database risk

Confirm Supabase project and workspace before writes

Never guess credentials

Preserve session stability

Prioritize safety and efficiency at all times

These safeguards ensure that development remains structured, predictable, and secure as the system scales.