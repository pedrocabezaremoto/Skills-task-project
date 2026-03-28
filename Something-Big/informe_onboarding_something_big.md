# Informe de Onboarding — Something Big
**Proyecto:** Something Big | Outlier AI | **Fecha:** 26/03/2026 | **Pedro Cabeza**

---

## Part 1: Prompt Writing Screening

### Pregunta 1
**PREGUNTA:**
Explain the difference between an implementation-agnostic prompt and an implementation-specific prompt. In your answer, include why implementation-specific details are discouraged in this project.

**RESPUESTA:**
An agnostic prompt tells **WHAT** a function should do: its name, inputs, and outputs. A specific prompt tells **HOW** to do it internally, like which loop or data structure to use. Specific details are discouraged because we want the model to show its own solution, not just follow a recipe.

### Pregunta 2
**PREGUNTA:**
Read the prompt snippet below and determine whether it is Implementation-Agnostic or Implementation-Specific. Make sure to justify your answer by being specific given the project guidelines.
*Snippet:* "Implement a PriorityQueue class that manages tasks by urgency. The constructor accepts no arguments. Expose an insert method that accepts a string for the task name and an integer for the priority level, adding a task with the given priority level, and a pop method that removes and returns the task with the highest priority. If the queue is empty, pop() must raise a ValueError."

**RESPUESTA:**
This prompt is **implementation-agnostic**. It only defines the class name, method names, inputs, outputs, and expected behavior. It does not say which data structure to use internally or how to sort the tasks.

### Pregunta 3
**PREGUNTA:**
Given this list, provide only the numbers of the elements that are considered implementation-agnostic:
1. helper functions
2. interface name
3. private internal fields of classes
4. function inputs
5. function outputs
6. name of classes/functions
7. detailing HOW a function works
8. detailing WHAT a function does
9. path of the interface

**RESPUESTA:**
- **Agnostic:** 2, 4, 5, 6, 8, 9
- **NOT agnostic:** 1 (helper functions = interno), 3 (private internal fields = interno), 7 (detailing HOW = implementacion interna).

### Pregunta 4
**PREGUNTA:**
Given the definition of Implementation-Agnostic and Implementation-Specific provided in the guidelines, transform the following Implementation-Specific prompt into an Implementation-Agnostic one.
*Snippet específico:* "Implement a TokenBucket class for rate limiting. The class must initialize self._capacity and self._refill_rate; internally, maintain a self._tokens counter and a self._last_refill_timestamp. Expose a consume(tokens: int) -> bool method helper to update self._tokens based on elapsed time..."

**RESPUESTA (versión agnóstica):**
Implement a TokenBucket class for rate limiting. It should accept `capacity` and `refill_rate` on initialization. Expose a `consume` method that accepts a number of tokens and returns `True` if the request is allowed, or `False` otherwise.

---

## Part 2: Rubric Validation + Test Categorization

### Pregunta: Is the following rubric valid or not?
**Rubric analizada:**
"In django/core/validators.py, the EmailValidator.__call__ method rejects email addresses whose total length exceeds 320 characters even when the local part and domain part are otherwise syntactically valid."

**RESPUESTA:**
Yes, it is **valid**. The rubric tests observable public behavior explicitly stated in the prompt: that EmailValidator rejects emails longer than 320 characters. The reference to `__call__` is also mentioned in the prompt as the public interface. It does not expose internal implementation details.

### Pregunta: Categorize tests as Agnostic or Specific
**Los 6 tests listados:**
1. test_decimal_validator_max_whole_digits_error_code
2. test_email_validator_accepts_bracketed_ipv6_literal
3. test_email_validator_rejects_invalid_length
4. test_url_validator_rejects_unsafe_characters
5. test_domain_validator_idna_disabled_rejects_non_ascii
6. test_url_validator_configurable_schemes

**RESPUESTA:**
**All six tests are implementation-agnostic**. Each one tests behavior explicitly described in the prompt:
1. Checks the public error code `max_whole_digits`, which the prompt names directly.
2. Checks bracketed IPv6 acceptance, stated in the prompt.
3. Checks length rejection limits (shorter than 21, longer than 320), stated in the prompt.
4. Checks unsafe character rejection, stated in the prompt.
5. Checks non-ASCII rejection when IDNA is disabled, stated in the prompt.
6. Checks configurable schemes behavior, stated in the prompt.
None of them inspect internal variables, file paths, or algorithm logic.

---

## Mision Asignada: Something Big Incentive

**Detalles de la misión:**
- **Recompensa:** $124.20 USD
- **Fecha límite:** 4/2/2026 (Milestone 1)
- **Horas requeridas:** 17 horas
- **Milestone 1:** Completar 2 tareas — $54 reward (**Vence en 3 días**)

**NOTA:**
La misión está **ACTIVA**. Requiere completar 17 horas de trabajo en el proyecto Something Big. El Milestone 1 ($54) vence en 3 días — **prioridad alta**. Las tareas se trabajan con la skill `task-big` usando el skill `container-env-manager` para Docker/VPS.

---
*Generado por Antigravity (Claude) — Perfil Peterhead — 26/03/2026*
