# /reorient Slash-Command Training

A small training project for experimenting with an agent control command in Codex / VS Code.

The project demonstrates how an `AGENTS.md` instruction can make the agent pause, compare its current work with the project goal, specification, process rules, Git state, and tests, then decide whether to continue, correct course, verify, or stop.

> Note: `/reorient` is used here as a trigger phrase defined in `AGENTS.md`. It is not a separately registered VS Code UI command.

## What `/reorient` checks

The review covers eight areas:

1. Goal alignment
2. Specification alignment
3. Process compliance
4. Verifiable progress
5. Stuck detection
6. Best next action
7. Value test
8. Decision

Every answer must include short, concrete evidence (maximum 80 characters).

Possible decisions are:

- `CONTINUE`
- `CORRECT COURSE`
- `STOP AND VERIFY`
- `STOP`

## Project files

- `AGENTS.md` - defines the `/reorient` behavior
- `README.md` - project overview
- `SPEC.md` - requirements and acceptance criteria
- `PROCESS.md` - development-process rules
- `app.py` - example discount calculator
- `test_app.py` - acceptance tests

## Try it

Clone the repository:

```bash
git clone https://github.com/IgorKPetersson/slash-command-training.git
cd slash-command-training
```

Run the tests:

```bash
python -m unittest discover
```

Open the folder in VS Code with Codex, then ask the agent to read `AGENTS.md`.

Run:

```text
/reorient
```

A useful experiment is to deliberately introduce a regression. For example, change the VIP multiplier in `app.py` from:

```python
return total * 0.80
```

to:

```python
return total * 0.75
```

Then run `/reorient` again.

A correct review should detect that:

- the change still concerns the project goal
- the implementation violates REQ-004
- the process can still be compliant if the spec and tests were checked
- the change is not verifiable progress
- one isolated regression does not mean the agent is stuck
- the smallest useful next action is restoring `0.80`
- the decision should be `CORRECT COURSE`

## Why this exists

The exercise shows how an agent can be given an explicit checkpoint that asks:

> Does the next action create real, verifiable value, or are we drifting away from the goal?

This helps separate activity from progress and implementation correctness from process compliance.

## License

MIT License. See `LICENSE`.
