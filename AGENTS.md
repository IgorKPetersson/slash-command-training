# Agent Instructions

## Project sources of truth

Use these files and repository state when evaluating project direction:

* Overall goal: `README.md`
* Requirements and acceptance criteria: `SPEC.md`
* Development process: `PROCESS.md`
* Implementation: relevant source files
* Tests: relevant test files
* Change scope: current `git status` and `git diff`

Do not claim compliance with the specification without reading the relevant
specification.

Do not claim tests pass without running them.

Do not claim process compliance without inspecting the current change scope.

Do not claim progress without checking the actual implementation and diff.

---

## Trigger: /reorient

When the user writes `/reorient`, stop implementation work temporarily.

Do not make further implementation changes until this review is complete.

### Required pre-check

Before answering `/reorient`, inspect:

* the overall project goal
* relevant specification files
* relevant acceptance criteria
* relevant process rules
* current implementation
* relevant tests
* relevant recent test results
* the full test suite when appropriate
* current `git status`
* current `git diff`
* the proposed next action

If Git is unavailable or the directory is not a Git repository, do not invent
diff or status evidence.

Use:

`Evidence: MISSING`

where repository-state evidence would otherwise be required.

### Evidence rules

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
* git status observations
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

Check both:

* whether required process steps were followed
* whether the current diff is limited to necessary changes

Inspect `git status` and `git diff` before answering when Git is available.

`Status: YES / PARTIAL / NO`

`Evidence: <max 80 chars>`

---

## 4. Verifiable progress

Have recent changes measurably reduced the distance to completion?

Base this on:

* the actual diff
* requirement coverage
* implementation state
* test evidence

Activity alone is not progress.

Repeated edits without improved evidence are not progress.

`Status: YES / PARTIAL / NO`

`Evidence: <max 80 chars>`

---

## 5. Stuck detection

Are there signs of:

* looping
* repeated failed edits
* speculative changes
* unnecessary cleanup
* unrelated refactoring
* premature abstraction
* local optimization
* repeated retries without new evidence

that do not materially advance the goal?

`Status: YES / NO`

`Evidence: <max 80 chars>`

---

## 6. Best next action

Identify the smallest next action that creates real, verifiable value.

Prefer actions that:

* satisfy an unmet requirement
* close an acceptance criterion
* fix a verified defect
* reduce a concrete risk
* produce missing evidence
* verify completion

Do not propose work merely because more work is possible.

If all requirements are already verified, stopping can be the correct next
action.

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

Use when:

* important evidence is missing
* evidence is contradictory
* root cause is unknown
* specification or process compliance cannot yet be verified

Do not continue implementation until the missing evidence is obtained.

### STOP

Use when:

* the project goal is satisfied for the current task
* relevant requirements are satisfied
* acceptance criteria are satisfied
* required verification has passed
* no further implementation adds required value

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
