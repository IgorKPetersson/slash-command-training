# Agent Instructions

## Project sources of truth

Use these files and repository state when evaluating project direction:

* Overall goal: `README.md`
* Requirements and acceptance criteria: `SPEC.md`
* Development process: `PROCESS.md`
* Implementation: relevant source files
* Tests: relevant test files
* Change scope: current Git status and diff

Do not claim compliance with the specification without reading the relevant
specification.

Do not claim tests pass without running them.

Do not claim process compliance without inspecting the current change scope.

Do not claim progress without checking the actual implementation and diff.

---

## Trigger: /reorient

When the user writes `/reorient`, stop implementation work temporarily.

Do not make further implementation changes until this review is complete.

---

## Required pre-check

Before answering `/reorient`, inspect:

* the overall project goal
* relevant specification files
* relevant acceptance criteria
* relevant process rules
* current implementation
* relevant tests
* relevant recent test results
* the full test suite when appropriate
* current Git repository state
* the proposed next action

When Git is available, `/reorient` MUST execute and inspect:

* `git status --short`
* `git diff --stat`
* `git diff`

At least one answer in sections 3-5 MUST cite repository-state evidence.

If the working tree is clean, say so explicitly.

Example:

`Evidence: git status --short returned no changes`

If Git is unavailable or the directory is not a Git repository, do not invent
repository-state evidence.

Use:

`Evidence: MISSING`

where Git evidence would otherwise be required.

---

## Evidence rules

Every answer must include:

`Evidence: <max 80 characters>`

Evidence must be concrete and verifiable.

Valid evidence includes:

* file paths
* requirement IDs
* acceptance criteria
* test results
* command output
* diff observations
* Git status observations
* concrete implementation state

Prefer evidence such as:

`Evidence: REQ-003 matches premium branch in app.py`

over vague statements such as:

`Evidence: Implementation looks correct`

Never invent evidence.

If evidence is unavailable, write:

`Evidence: MISSING`

Treat missing evidence as something that may require verification before more
implementation work.

Do not use test success alone as proof of specification compliance.

Do not use implementation activity alone as proof of progress.

Do not claim process compliance without repository-state evidence when Git is
available.

---

## 1. Goal alignment

Is the current work still directly connected to the overall project goal?

`Status: YES / PARTIAL / NO`

`Evidence: <max 80 chars>`

---

## 2. Specification alignment

Does the current implementation match the relevant specification and
acceptance criteria?

Inspect both the specification and the implementation.

Passing tests alone are not sufficient evidence.

`Status: YES / PARTIAL / NO`

`Evidence: <max 80 chars>`

---

## 3. Process compliance

Does the work follow the project's development process and process rules?

Check:

* whether required process steps were followed
* whether the current diff is limited to necessary changes

When Git is available, inspect:

* `git status --short`
* `git diff --stat`
* `git diff`

When evaluating process compliance, distinguish between:

* implementation changes
* test changes
* specification/process documentation changes
* agent-instruction changes

Changes to agent-instruction files such as `AGENTS.md` do not by themselves
count as implementation-scope violations.

Do not downgrade process compliance solely because `AGENTS.md` is modified.

A specification violation or failing test does not by itself mean the
development process was violated.

Evaluate process compliance separately from implementation correctness.

Examples of process violations include:

* required tests were not run
* specification was not consulted
* unrelated files were modified
* change scope expanded without justification
* required verification was skipped
* known failing tests were ignored

A failing test discovered by following the required process is evidence that
verification worked, not automatically evidence of process non-compliance.

Do not claim process compliance without repository-state evidence.

If the working tree is clean, say so explicitly.

A wrong implementation change is not automatically a process violation.

Do not downgrade process compliance only because:

* the implementation violates a requirement
* a test fails
* the current diff contains a regression

Those belong to specification alignment and verifiable progress.

Only downgrade process compliance when a process rule itself was violated.

Examples:

`Status: YES`
`Evidence: Change is scoped; spec checked; full test suite was run`

`Status: PARTIAL`
`Evidence: Relevant tests ran, but full required suite was skipped`

`Status: NO`
`Evidence: Unrelated files changed despite PROCESS.md scope rule`

`Status: YES / PARTIAL / NO`

`Evidence: <max 80 chars>`

---

## 4. Verifiable progress

Have recent actions measurably reduced the distance to completion?

Determine progress from the current implementation diff.

Apply these rules in order:

1. If the implementation diff is empty:
   `Status: NO`

2. If the implementation diff introduces a regression or failing requirement:
   `Status: NO`

3. If the implementation diff contains useful changes but the task remains
   incomplete:
   `Status: PARTIAL`

4. Only use:
   `Status: YES`

   when the current implementation diff contains changes that measurably move
   the project toward completion.

Important:

* A correct implementation is not automatically progress.
* Passing tests are verification, not progress.
* Restoring the repository to its committed baseline is not current diff
  progress once the implementation diff is empty.
* Do not infer past progress from conversation history when the current
  implementation diff is empty.
* An empty implementation diff MUST result in `Status: NO`.

Examples:

Empty implementation diff:

`Status: NO`
`Evidence: app.py diff is empty; no current implementation progress`

Useful implementation change:

`Status: YES`
`Evidence: git diff adds REQ-004 implementation; VIP test passes`

Regression:

`Status: NO`
`Evidence: git diff changes VIP to 0.85; REQ-004 test fails`

Partial implementation:

`Status: PARTIAL`
`Evidence: REQ-004 added; REQ-005 remains unimplemented`

`Evidence: <max 80 chars>`


---

## 5. Stuck detection

Are there signs that the current work is stuck?

Use repository and current-task evidence.

Examples of being stuck:

* repeated failing edits visible in the current task
* repeated retries without new evidence
* looping between the same approaches
* speculative refactoring without measurable progress
* repeated changes that do not reduce the distance to completion

Do not mark the work as stuck merely because one incorrect change exists.

Do not infer stuck status only from earlier experiments or unrelated
conversation history.

Use:

`Status: YES`

only when there is concrete evidence of repeated or looping ineffective work.

Otherwise use:

`Status: NO`

Examples:

`Status: NO`
`Evidence: One isolated regression is present; no retry loop is visible`

`Status: YES`
`Evidence: Three retries produced the same failing VIP test`

`Evidence: <max 80 chars>`


---

## 6. Best next action

Identify the single smallest next action that creates real, verifiable value.

The next action must contain exactly one concrete action.

Do not combine implementation and verification in the same next action.

Examples:

Good:
`Next: Restore the VIP multiplier to 0.80`

Bad:
`Next: Restore the VIP multiplier to 0.80 and rerun the tests`

After the next action is completed, verification can become the following step.

Prefer actions that:

* satisfy an unmet requirement
* fix a verified defect
* reduce a concrete risk
* produce missing evidence
* verify completion

If all requirements are already verified, stopping can be the correct next action.

`Next: <one concrete action>`

`Evidence: <max 80 chars>`

---

## 7. Value test

Does the proposed next action directly do at least one of the following?

* satisfy an unmet requirement
* close an acceptance criterion
* reduce a concrete risk
* fix a verified defect
* produce necessary evidence
* verify completion

If none apply, the next action does not have sufficient demonstrated value.

Stopping may pass the value test if continued implementation would create
unnecessary or unrelated work.

`Status: YES / NO`

`Evidence: <max 80 chars>`

---

## 8. Decision

Choose exactly one:

### CONTINUE

Use when:

* the current direction is correct
* useful required work remains
* the proposed next action has verified value

### CORRECT COURSE

Use when:

* useful work remains
* but the current approach, scope, or direction should change

### STOP AND VERIFY

Use only when:

* important evidence is missing
* evidence is contradictory
* root cause is unknown
* specification compliance cannot yet be verified
* process compliance cannot yet be verified
* required tests or validation have not yet been completed

Do not continue implementation until the missing evidence is obtained.

### STOP

Use when:

* no unmet requirement is known
* relevant requirements are satisfied
* acceptance criteria are satisfied
* required verification has passed
* no further implementation adds required value

---

## Decision precedence

Use `STOP` when ALL of these are true:

* no unmet requirement is known
* acceptance criteria are verified
* required tests pass
* no further implementation change has demonstrated value

Do NOT use `STOP AND VERIFY` if the required verification has already completed.

`STOP AND VERIFY` is only for missing, conflicting, or insufficient evidence.

If verification is complete and the task is complete, use `STOP`.

`Decision: CONTINUE / CORRECT COURSE / STOP AND VERIFY / STOP`

`Evidence: <max 80 chars>`

---

## Final line

End the response with exactly this format:

`Direction: <OK|CORRECT> | Next: <short action> | Value: <concrete effect>`

Use:

* `OK` when the current direction is valid
* `CORRECT` when the direction or next action must change

The final line must be the last line of the `/reorient` response.

---

## General reorientation rules

* Activity is not progress.
* Verification is not automatically progress.
* More code is not automatically more value.
* Passing tests do not automatically prove specification compliance.
* Refactoring is not progress unless it supports a verified requirement.
* Cleanup is not required work unless the specification or process requires it.
* Prefer closing requirements over creating abstractions.
* Prefer fixing verified failures over speculative improvements.
* Prefer evidence over assumptions.
* Prefer the smallest useful change.
* Do not optimize code that already satisfies the relevant requirement.
* Do not expand scope without a verified reason.
* Do not continue merely because additional improvements are possible.
* If the next action has no clear value, choose another action or stop.
* If goal alignment is unclear, verify before coding.
* If specification alignment is unclear, verify before coding.
* If process compliance is unclear, verify before coding.
* If the work is complete and verified, stop implementation.
