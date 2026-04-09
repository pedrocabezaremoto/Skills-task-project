# Real Coder – Expected Interface, Evaluation Scripts & Rubrics
> **Project:** Real Coder | **Platform:** Outlier  
> **Scope:** Task design contracts — interface specification, test case authoring, and rubric definition  
> **Audience:** Senior developers creating or reviewing Real Coder tasks

---

## Table of Contents

1. [Core Philosophy](#1-core-philosophy)
2. [Expected Interface](#2-expected-interface)
3. [Evaluation Scripts (Test Cases)](#3-evaluation-scripts-test-cases)
4. [Rubrics](#4-rubrics)
5. [Domain Reference Table](#5-domain-reference-table)
6. [Decision Framework](#6-decision-framework)
7. [Anti-Patterns to Avoid](#7-anti-patterns-to-avoid)

---

## 1. Core Philosophy

The Real Coder evaluation system is built around a **black-box contract**: the expected interface defines *what* the solution must expose, while the implementation details remain entirely free. This design prevents two critical failure modes:

| Failure Mode | Description | Impact |
|---|---|---|
| **Over-specification** | Enforcing internal function names, helper methods, or file structures | Leaks the intended solution; penalizes valid alternative implementations |
| **Under-specification** | Leaving input/output types ambiguous | Causes evaluation scripts to fail on trivial type mismatches |

The evaluation system uses **two complementary verification mechanisms**:

```
┌──────────────────────────────────────────────────────────┐
│                   Verification Layer                     │
│                                                          │
│  ┌─────────────────────┐    ┌────────────────────────┐  │
│  │  Evaluation Scripts  │    │        Rubrics         │  │
│  │  (Black-box tests)   │    │   (White-box review)   │  │
│  │                      │    │                        │  │
│  │  • Objective         │    │  • Qualitative         │  │
│  │  • Programmatic      │    │  • Architectural       │  │
│  │  • I/O assertions    │    │  • Side-effect checks│  │
│  │  • Side-effect checks│    │  • Design pattern audit│  │
│  └─────────────────────┘    └────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

---

## 2. Expected Interface

### 2.1 Definition

The Expected Interface is the **minimal public contract** between the evaluator and the solution. It defines the natural entry point that a real user or dependent system would interact with.

### 2.2 Design Rules

**Rule 1 — Minimal Surface Area**

Specify only the primary entry point. Nothing more.

```python
# ✅ Correct — only the required public function
def find_shortest_path(grid: list[list[int]]) -> int:
    ...

# ❌ Wrong — exposes internal helpers
def find_shortest_path(grid: list[list[int]]) -> int: ...
def _build_adjacency_matrix(grid): ...         # internal
def _reconstruct_path(came_from, end): ...     # internal
```

**Rule 2 — Strict Typing**

Always define explicit input types and return types. Ambiguity causes evaluation failures.

```python
# ✅ Correct — unambiguous types
def train_and_predict(train_csv: str, test_csv: str) -> list[float]:
    ...

# ❌ Wrong — no types, return type unclear
def train_and_predict(train_csv, test_csv):
    ...  # could return tuple, dict, numpy array
```

**Rule 3 — Implementation Agnostic**

The interface must not hint at or constrain the internal architecture.

```python
# ✅ Correct — says nothing about implementation
def compress_image(path: str, quality: int) -> bytes:
    ...

# ❌ Wrong — prescribes internal structure
# "Use a DCT-based approach with a ZigZag encoder helper class"
def compress_image(path: str, quality: int) -> bytes:
    ...
```

### 2.3 Interface by Entry Point Type

| Entry Point Type | Specification Format |
|---|---|
| Function | Signature with typed args and return type |
| Class | Class name + required public methods with types |
| CLI | Exact command, flags, arguments, and stdout/exit code format |
| REST API | HTTP method + route + request body schema + response schema |

### 2.4 Examples by Domain

```python
# Algorithm
def find_shortest_path(grid: list[list[int]]) -> int: ...

# Data Science
def train_and_predict(train_csv: str, test_csv: str) -> list[float]: ...

# CLI
# Command: python cli.py --input data.csv --output result.json
# Exit code 0 on success, 1 on error

# Web Backend
# POST /api/checkout
# Request:  { "user_id": int, "cart_items": list[dict] }
# Response: { "order_id": str, "status": str }  — HTTP 200

# Frontend
# Component: UserProfile
# Props: { user: { id: int, name: str, email: str } }
```

---

## 3. Evaluation Scripts (Test Cases)

### 3.1 Role

Evaluation scripts are **purely objective, programmatic assertions**. They interact with the solution exclusively through the Expected Interface — treating the implementation as a complete black box.

> **Critical rule:** Scripts must never mock or patch internal components. If testing internal logic directly seems necessary, the Expected Interface is poorly designed, or a rubric should be used instead.

### 3.2 What Test Cases Verify

**Category 1 — Input/Output Assertions**

```python
# Standard case
assert find_shortest_path(grid_1) == 14

# Edge case
assert find_shortest_path(empty_grid) == -1

# Invalid input
assert find_shortest_path(None) raises ValueError

# Type contract
result = train_and_predict("train.csv", "test.csv")
assert isinstance(result, list)
assert all(isinstance(v, float) for v in result)
```

**Category 2 — Side-Effect Verification**

For tasks involving databases, file systems, or network calls — verify the **resulting system state**, not how it was reached.

```python
# Database side-effect
response = client.post("/api/checkout", json=payload)
assert response.status_code == 200

order = db.query("SELECT * FROM orders WHERE user_id = ?", user_id)
assert order is not None                     # record was inserted
assert order["status"] == "pending"          # state is correct

# File system side-effect
compress_image("input.png", quality=80)
assert os.path.exists("output.png")          # file was created
assert os.path.getsize("output.png") < os.path.getsize("input.png")  # was compressed

# API side-effect (mock server)
send_notification(user_id=42, message="Hello")
assert mock_smtp.call_count == 1             # email was sent
assert mock_smtp.call_args[1]["to"] == "user@example.com"
```

### 3.3 Test Coverage Requirements

| Category | Coverage |
|---|---|
| Standard/happy-path cases | Required |
| Edge cases (empty, zero, boundary values) | Required |
| Invalid inputs (wrong type, out of range, None) | Required |
| Large inputs / performance bounds | When task-relevant |
| Concurrency / race conditions | When task-relevant |

---

## 4. Rubrics

### 4.1 Role

Rubrics provide **qualitative and structural verification** for constraints that cannot be captured by programmatic assertions. Unlike test cases, rubrics have full access to the codebase (white-box evaluation).

### 4.2 When to Use Rubrics vs. Test Cases

| Verification Need | Use Test Case | Use Rubric |
|---|---|---|
| Output value correctness | ✅ | — |
| Database record inserted | ✅ | — |
| Algorithm choice (BFS vs brute-force) | — | ✅ |
| Banned library not used | — | ✅ |
| Password hashed before storage | — | ✅ |
| React Hooks vs Class components | — | ✅ |
| Code readability / documentation | — | ✅ |
| CSS responsive layout | — | ✅ |

### 4.3 Rubric Types

**Type 1 — Constraint Adherence**

Verifies the solution did not use prohibited approaches or libraries.

```
✅ Rubric: "The solution implements linear regression from scratch using
   numpy without importing sklearn or scipy."

✅ Rubric: "The sorting algorithm does not use Python's built-in sort()
   or sorted() functions."
```

**Type 2 — Architectural Checks**

Verifies design patterns, security practices, and structural decisions.

```
✅ Rubric: "The API hashes the user password using bcrypt (or equivalent
   secure algorithm) before inserting it into the database."

✅ Rubric: "The React component manages state using Hooks (useState,
   useReducer) rather than Class component lifecycle methods."

✅ Rubric: "The database insertion and payment processing are wrapped in
   a single atomic transaction."
```

**Type 3 — Qualitative Assessment**

Evaluates subjective requirements that cannot be reduced to assertions.

```
✅ Rubric: "Functions and variables are named clearly and
   descriptively; complex logic is accompanied by inline comments."

✅ Rubric: "The UI layout uses CSS flexbox or grid to adapt
   responsively to mobile screen sizes."

✅ Rubric: "The API returns consistent, well-structured error
   responses with appropriate HTTP status codes."
```

### 4.4 Rubric Writing Guidelines

- **Atomic:** Each rubric checks exactly one constraint.
- **Verifiable:** Must be deterministically assessable by reading the code.
- **Non-overlapping:** Rubrics should not duplicate what test cases already verify.
- **Specific:** Reference concrete techniques, libraries, or patterns — avoid vague language.

```
# ❌ Bad rubric — vague and non-atomic
"The code is well-written and follows best practices."

# ✅ Good rubric — specific and atomic
"The solution uses a context manager (with statement) to handle
 file I/O, ensuring the file handle is closed even on exceptions."
```

---

## 5. Domain Reference Table

| Domain | Expected Interface | Test Case Focus | Rubric Focus |
|---|---|---|---|
| **Algorithms** | `def find_shortest_path(grid: list[list[int]]) -> int` | Assert output equals known values; unsolvable returns `-1` | Algorithm complexity — BFS/A* vs brute-force |
| **Data Science** | `def train_and_predict(train_csv: str, test_csv: str) -> list[float]` | Output list length matches test rows; RMSE < threshold | Feature scaling applied before training |
| **Web Backend** | `POST /api/checkout` accepting `{user_id, cart_items}` | HTTP 200; query mock DB to confirm order inserted | DB insertion + payment in single atomic transaction |
| **Frontend/UI** | `UserProfile` component accepting `user` prop object | Render in test DOM; assert name/email fields present | Flexbox/grid used for responsive layout |
| **CLI Tools** | `python cli.py --input <file> --output <file>` | Check exit code, stdout, and output file content | Argument validation and user-facing error messages |
| **Security** | `def register_user(username: str, password: str) -> dict` | Assert returned token is valid JWT; user persisted in DB | Password hashed with bcrypt before storage |

---

## 6. Decision Framework

Use this flow when designing a new Real Coder task:

```
START: What needs to be verified?
          │
          ▼
Is it an objective input/output or system state assertion?
   YES ──► Write an Evaluation Script (test case)
   NO  ──► Continue
          │
          ▼
Is it about architectural choice, banned libraries, or qualitative quality?
   YES ──► Write a Rubric
   NO  ──► Continue
          │
          ▼
Are you testing an internal function or helper?
   YES ──► Redesign the Expected Interface (it is over-specified)
          or convert to a Rubric
```

---

## 7. Anti-Patterns to Avoid

| Anti-Pattern | Why It's Wrong | Correct Approach |
|---|---|---|
| Specifying internal helper function names in the interface | Leaks solution; penalizes valid alternatives | Define only the primary public entry point |
| Leaving return types unspecified | Causes type mismatch failures during evaluation | Always use strict typing in the interface signature |
| Test case that patches/mocks an internal method | Couples test to implementation internals | Test only through the Expected Interface |
| Rubric that duplicates a test case assertion | Redundant verification; creates conflicting signals | Use rubrics only for what tests cannot cover |
| Vague rubric language | Non-deterministic assessment | Reference specific libraries, patterns, or techniques |
| Interface that specifies file/module structure | Over-constrains architecture | Interface = entry point only; no structural hints |
| Testing concurrency without specifying it in the prompt | Unfair surprise constraint | Make concurrent requirements explicit in the task prompt |

---

> **Summary:** The Real Coder evaluation contract has two layers. The Expected Interface defines the minimal, strictly-typed public entry point — nothing about internals. Evaluation scripts test objective input/output and side-effects through that interface as a black box. Rubrics cover everything that tests cannot: algorithm choices, security patterns, banned libraries, and qualitative quality. Mastering the boundary between these three components is essential to authoring well-formed Real Coder tasks.
