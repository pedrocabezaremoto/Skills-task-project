---
name: task-big
description: "Asistente y auditor para el proyecto 'Something Big' de Outlier. Contiene las reglas estructurales para rúbricas, evaluación de código agnóstico y el flujo de Docker en VPS. Depende del skill container-env-manager para infraestructura."
---

# Skill: Task Big (Proyecto "Something Big" - Outlier)

Esta skill está diseñada para guiar, auditar y estructurar el trabajo en el proyecto "Something Big" de Outlier, integrando las mejores prácticas para evaluación de IA, diseño de prompts, creación de rúbricas agnósticas y el uso del VPS.

---

## 🔗 Regla 0 — Dependencia de Infraestructura (OBLIGATORIA)

> **Cada vez que se inicie una evaluación para el proyecto Something Big, este skill DEBE apoyarse obligatoriamente en el skill `container-env-manager` para manejar toda la conexión al VPS y la ejecución de Docker.**

---

## 📚 Guías y Referencias de Reglas (Knowledge Base)

Para cada fase del proyecto, consulte las guías específicas ubicadas en `/root/skills-task-project/Something-Big/guides/`:

*   **[G1: Diseño de Prompts](guides/g1_prompt_engineering.md)** — Principios agnósticos y estructura obligatoria.
*   **[G2: Diseño de Rúbricas](guides/g2_rubric_design.md)** — Dimensiones, pesos (1/3/5) y criterios atómicos.
*   **[G3: Protocolo de Tests y Golden Loop](guides/g3_testing_protocol.md)** — P2P, F2P y validación en Docker.

---

## 📋 Proceso de Auditoría y Entrega

Antes de entregar una tarea, asegúrese de completar el **[Checklist de Entrega Final](checklists/checklist_delivery.md)** para garantizar la fluidez nativa y la calidad técnica exigida.

---

## 🚀 Monitor de Misión e Incentivos

Consulte la información actualizada de recompensas y plazos en el **[Monitor de Misión](MISSION_MONITOR.md)**.

---

## 📂 Informe de Onboarding (Historico)
El resumen de los cursos de inducción del 26/03/2026 se encuentra en: **[Informe de Onboarding Something Big](informe_onboarding_something_big.md)**.

---
**Nota al Asistente:** Al ser invocado bajo esta skill, actúa como Evaluador y Creador (Task Big). Analiza diffs, diseña prompts y redacta rúbricas ciñéndote ciegamente a estas directivas sin apartarte del enfoque Implementation-Agnostic. Para TODA operación de Docker/VPS, delega al skill `container-env-manager`.
