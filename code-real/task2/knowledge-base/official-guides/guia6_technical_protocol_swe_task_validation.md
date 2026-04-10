# Technical Protocol for SWE Task Validation and Agentic Evaluation

## 1. Executive Summary of the Evaluation Framework

Current Software Engineering (SWE) evaluation metrics often fail because they conflate simple instruction-following with genuine architectural reasoning. To measure true engineering proficiency in AI agents, we must move away from over-constrained tasks that provide a "blueprint" for the solution. This protocol establishes a rigorous framework that prioritizes implementation flexibility while maintaining strict verification standards. By decoupling the interface from the internal logic, we ensure that agents are evaluated on their ability to architect robust, generalizable systems rather than their ability to follow a path of least resistance paved by over-specified prompts.

The framework is structured around three core pillars:

| Evaluation Type | Primary Objective | Validation Method |
|---|---|---|
| Expected Interface | Establish the interaction contract. | Black-box: Explicit definition of entry points and types. |
| Evaluation Scripts | Verify functional correctness. | Black-box: Programmatic assertions of state and output. |
| Agentic Rubrics | Assess structural and qualitative integrity. | White-box: Deep inspection of codebase and constraints. |

These components function as a unified pipeline. The Expected Interface defines the "what," Evaluation Scripts objectively measure the "result," and Agentic Rubrics validate the "how," ensuring the solution meets professional standards of security and design.

---

## 2. Technical Specification: The Expected Interface

The Expected Interface is the primary contract between the evaluation environment and the agent. It represents the natural entry point—API, CLI, or Class—that a user or dependent system would utilize. High-fidelity evaluation requires avoiding "over-specification." When a task dictates internal function names or helper logic, it causes solution leakage, a procedural failure where the prompt inadvertently guides the model toward a specific architecture. This invalidates the test of the agent’s reasoning, reducing a complex engineering problem to a simple translation task.

To maintain a valid interface, the following three requirements are mandatory:

* **Minimal Surface Area**: Specify only the primary entry point (e.g., a specific API route, a main class, or the primary function signature).
* **Strict Typing**: Explicitly define all data types for inputs and returns. This serves as the primary defense against "flaky" evaluation pipelines where scripts fail due to trivial mismatches, such as a model returning a tuple instead of a list.
* **Implementation Agnosticism**: Forbid any mention of internal state, file structures, or helper logic. The agent must have the autonomy to decide how to modularize the solution.

### Competitive Impact and Benchmarking

Implementation agnosticism is critical for the competitive landscape of AI benchmarking. By allowing the agent to define its own internal modularization, we gain a high-resolution measure of senior-level engineering capability. This prevents models from over-fitting to specific leaderboard tasks and ensures that comparisons between different model architectures are based on generalizable problem-solving rather than their ability to mirror a hidden implementation key.

Once the interface contract is established, objective verification of the agent’s output proceeds via programmatic testing.

---

## 3. Programmatic Assertion Logic: Evaluation Scripts

Evaluation scripts serve as the ultimate, objective arbiters of functional correctness. These scripts operate as black-box tests, interacting with the agent's solution exclusively through the Expected Interface. They verify that the code performs its intended function across a variety of scenarios without interfering with the internal state.

| Category | Description | Example Failure |
|---|---|---|
| Input/Output Assertions | Verifying exact outputs for standard, edge, and invalid cases. | Function returns a float instead of the expected Decimal for currency. |
| Side-Effect Verification | Assessing system state changes (DB, files, network). | Database record is created, but the `created_at` timestamp is missing or in the wrong zone. |

### Best Practices and the "White-Box Hack" Problem

Scripts must never attempt to mock or patch internal components of the solver's solution. Poor interface design—such as failing to define clear return types or providing ambiguous entry points—often necessitates "white-box hacks." In these scenarios, a tester is forced to mock an internal helper function because the main interface's output is non-deterministic. This is a structural failure of the task; if a script cannot verify a requirement through the public interface, that requirement belongs in an agentic rubric, not a test script.

Programmatic scripts are effective for judging outcomes, but they cannot evaluate code quality. Qualitative gaps are filled by the white-box rubric system.

---

## 4. Qualitative and Structural Verification: Agentic Rubrics

Agentic Rubrics provide the necessary white-box evaluation to verify architectural integrity. Unlike scripts, rubrics have full access to the codebase, allowing for the inspection of non-deterministic outcomes and qualitative constraints that escape simple I/O assertions.

Rubrics are deployed for three specific use cases:

1. **Constraint Adherence**: Verifying the agent did not bypass technical constraints (e.g., implementing a neural network "from scratch" using NumPy rather than importing PyTorch).
2. **Architectural & Security Checks**: Validating specific design patterns (e.g., ensuring a React component uses Hooks rather than Classes) or security protocols.
3. **Qualitative Assessment**: Judging subjective but critical factors like code readability, documentation quality, and UI/UX responsiveness.

### Strategic Value: The Production Standard

Architectural checks provide the "So What?" of professional evaluation. In a production environment, a solution that is functionally correct but violates security protocols—such as failing to use bcrypt for password hashing—is a hard fail. Rubrics prevent "hacky" solutions that pass I/O tests but introduce technical debt or security vulnerabilities that would never survive a professional code review.

---

## 5. Domain-Specific Implementation Samples

The following examples demonstrate the interplay between objective scripts and qualitative rubrics across various engineering disciplines.

* **Interface**: `def find_shortest_path(grid: list[list[int]]) -> int:`
  * **Script Assertion**: Confirm the function returns the correct integer (e.g., 14) for a complex grid and handles unsolvable cases by returning -1.
  * **Rubric Requirement**: Verify the implementation uses A* or BFS; a brute-force approach is a fail.
  * **Verification Strategy**: The script performs a stateless logic check, while the rubric evaluates computational efficiency and algorithmic choice.

* **Interface**: `def train_and_predict(train_csv: str, test_csv: str) -> list[float]:`
  * **Script Assertion**: Assert that the RMSE of the output list is below 1.5 when compared against a hidden ground-truth set.
  * **Rubric Requirement**: Confirm that the agent performed feature scaling (normalization or standardization) prior to training.
  * **Verification Strategy**: The script measures predictive accuracy, while the rubric ensures the data preprocessing pipeline adheres to scientific best practices.

* **Interface**: `POST /api/checkout` (JSON payload: user_id, cart_items).
  * **Script Assertion**: Send a valid POST and verify a 200 OK status; query the mock DB to confirm the order table was updated.
  * **Rubric Requirement**: Ensure the entire checkout process (DB insertion and payment) is wrapped in a single, atomic database transaction.
  * **Verification Strategy**: This is a stateful verification challenge; the script checks the final state, while the rubric verifies the integrity of the process that reached that state.

* **Interface**: React component `UserProfile` accepting a `user` prop object.
  * **Script Assertion**: Mount the component and assert the existence of name and email text fields in the DOM.
  * **Rubric Requirement**: Verify that the layout utilizes Flexbox or Grid to ensure mobile responsiveness.
  * **Verification Strategy**: The script checks for the existence of elements, whereas the rubric evaluates the adaptability and quality of the styling logic.

---

**Final Directive**: All SWE task constructions must be objective, strictly typed, and implementation agnostic. Focus evaluation on the interface contract and functional outcomes via scripts, while utilizing rubrics to enforce architectural and security standards.
