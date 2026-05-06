# dsa

A structured system for mastering algorithms and data structures.

## Philosophy

This repository documents the continuous refinement of problem-solving ability.

Every solution is versioned.  
Every problem is a unit of deliberate practice.  
Selected solutions are elevated when they demonstrate reusable techniques or non-trivial insight.

The objective is not volume — it is technical maturity.

## Structure

- `core/` - Fundamental data structures and algorithms
- `docs/` - Structured documentation and references
- `foundations/` - Fundamental concept training
- `problems/` - All solved problems, organized by source
- `showcase/` - Solutions that demonstrate strong techniques or patterns

## Rules

- One problem per commit
- No mass commits
- Explicit over clever
- Refactor only when insight improves
- Showcase only when justified

## Workflow

For foundations:

- Implement concept-focused modules
- Commit with: `feat: implement <concept> <approach>`

For each problem:

- Implement problem-focused folders
- Commit with: `feat: add solution to <problem-id>`

If the solution reveals a reusable technique, promote it to `showcase/`.

## Languages

- C
- Haskell
- Python

## Purpose

To build durable reasoning skill through:

- Algorithmic rigor
- Pattern extraction
- Controlled iteration
- Technical clarity
- Conceptual mastery through structured foundational training

This is a long-term repository.

## Run

### On Linux

```bash
# clone repository
git clone https://github.com/geldois/dsa.git && cd dsa

# create virtual environment and install dependencies
python3 -m venv .venv && source .venv/bin/activate && pip install -e ".[dev]"
```

### On Windows

```bash
# clone repository
git clone https://github.com/geldois/dsa.git
cd dsa

# create virtual environment and install dependencies
python -m venv .venv
.venv\Scripts\Activate
pip install -e ".[dev]"
```
