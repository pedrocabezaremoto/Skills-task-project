---
name: P2p
description: "Asistente para el proyecto P2P de Outlier (Hawkins Experiments). Proyecto enfocado en Code-Refactoring y Performance Optimization desde repositorios GitHub. Depende del skill container-env-manager para infraestructura Docker/VPS."
---

# Skill: P2P — Hawkins Experiments (Proyecto Outlier)

> **Estado:** ✅ Operativo — Skill completo con guías, plantillas, checklists y workflows.

Esta skill guía y estructura el trabajo en el proyecto **P2P (Hawkins Experiments)** de Outlier, enfocado en construir entornos de evaluación de modelos de IA que modifican código en repositorios GitHub.

---

## 🔗 Regla 0 — Dependencia de Infraestructura (OBLIGATORIA)

> **Este skill DEBE apoyarse obligatoriamente en el skill `container-env-manager` para manejar toda la conexión al VPS y la ejecución de Docker.**

```
🔗 INFRASTRUCTURE DEPENDENCY — AUTOMATIC

Cuando P2P necesite ejecutar código en Docker:
  1. Invocar container-env-manager → Rule 1 (SSH Health Check)
  2. Invocar container-env-manager → Rule 2 (Docker Daemon Verification)
  3. Solo después → Proceder con las fases del proyecto P2P

Skill de infraestructura: container-env-manager
  Ubicación: .agent/skills/container-env-manager/SKILL.md
  Script SSH: .agent/skills/container-env-manager/scripts/ssh-remote-runtime.md
```

---

## 📌 Información del Proyecto

| Campo | Valor |
|---|---|
| **Proyecto** | P2P (Hawkins Experiments) |
| **Plataforma** | Outlier AI |
| **Enfoque** | Code Refactoring & Performance Optimization |
| **Tipos de Tarea** | R/M (Refactoring/Maintainability) · PO (Performance Optimization) |
| **Fuente de código** | Pull Requests de repositorios GitHub |
| **Tarifa** | $27.00 / hr |
| **Estado** | Onboarding Completado ✅ |

---

## 📂 Estructura del Skill

```
P2p/
├── SKILL.md                              ← Este archivo (reglas maestras)
├── informe_onboarding_hawkins.md         ← Informe completo del onboarding (10 páginas + anexos)
│
├── guides/                               ← Guías de referencia rápida
│   ├── g1_especificaciones_completas.md  ← Reglas maestras del proyecto
│   ├── g2_parsing_guide.md              ← Cómo implementar parsing.py
│   ├── g3_docker_reference.md           ← Docker: imágenes, comandos, Dockerfile
│   └── g4_rubric_guidelines.md          ← Cómo crear rúbricas (R/M tasks)
│
├── templates/                            ← Plantillas listas para copiar y usar
│   ├── Dockerfile.template              ← Plantilla base del Dockerfile
│   ├── parsing_template.py              ← Parser (solo modificar parse_test_output)
│   ├── run_script.sh                    ← Plantilla del run script
│   ├── reproduction_script.sh           ← Plantilla del script de reproducción (PO)
│   └── prompt_template.md               ← Estructura del prompt
│
├── checklists/                           ← Listas de verificación pre-entrega
│   ├── checklist_rm_task.md             ← Checklist para tareas R/M
│   ├── checklist_po_task.md             ← Checklist para tareas PO
│   └── checklist_e2e_validation.md      ← Checklist para validación E2E
│
└── workflows/                            ← Flujos de trabajo paso a paso
    ├── workflow_rm_task.md              ← Flujo completo: PR → Entrega (R/M)
    └── workflow_po_task.md              ← Flujo completo: PR → Entrega (PO)
```

---

## ⚡ 4 Reglas de Enforcement (OBLIGATORIAS en cada tarea)

### Regla 1 — Artefactos Core 6
Toda tarea DEBE entregar estos 6 archivos:
1. `Dockerfile` — SHA del commit padre, sin COPY de scripts, agnóstico a arquitectura
2. `golden.patch` — Formato unified diff, se aplica limpiamente, pasa e2e.sh
3. `parsing.py` — Solo modificar `parse_test_output()`, usar plantilla oficial
4. `run_script.sh` — Solo pruebas que ya pasaban antes del parche
5. Prompt — Plantilla: Context → Problem → Requirements → Success Criteria → Files → Notes
6. User-Facing Problem Description

### Regla 2 — Entregables por Tipo
- **R/M Tasks:** Core 6 + Rúbrica (15-20 criterios, pesos 1/3/5 solamente, PROHIBIDO 2 o 4)
- **PO Tasks:** Core 6 + Target Functions + Reproduction Script (formato: `METRIC_VALUE: <número>`)

### Regla 3 — Prohibiciones Absolutas (Fallo Automático)
- ❌ Usar branch name en Dockerfile (debe ser SHA)
- ❌ Usar COPY para scripts de evaluación en Dockerfile
- ❌ Dar pistas o soluciones en el prompt
- ❌ Crear benchmarks simulados/dummies en PO
- ❌ Modificar el script `e2e.sh`
- ❌ Usar pesos 2 o 4 en rúbricas
- ❌ Dejar rúbricas generadas por LLM sin editar exhaustivamente

### Regla 4 — Validación Final
- El script `e2e.sh` DEBE correr sin errores ni intervención manual
- Debe generar `before.json` y `after.json` (ambos con todos los tests en PASSED)
- Para PO: también genera `reproduction_before_stdout.txt` y `reproduction_after_stdout.txt`
- Estructura obligatoria: `e2e.sh` en raíz, todos los archivos en carpeta `app/`

---

## 📝 Flujo Rápido de Trabajo

```
1. Recibir source_url (PR de GitHub)
2. Analizar el PR → Entender qué problema resuelve
3. Escribir User-Facing Problem Description
4. Crear Dockerfile (SHA commit padre, dependencias, sin COPY)
5. Escribir Prompt (plantilla, sin pistas, autocontenido)
6. Identificar tipo de tarea (R/M o PO)
7. Crear Golden Patch (solución perfecta)
8. Crear run_script.sh (solo tests que ya pasaban)
9. Implementar parse_test_output() en parsing.py
10. [R/M] Crear Rúbrica (15-20 criterios) | [PO] Crear reproduction_script.sh + Target Functions
11. Correr e2e.sh → Verificar before.json/after.json
12. Entregar
```

---

**Nota al Asistente:** Al ser invocado bajo esta skill, actúa como asistente especializado en Hawkins Experiments. Consulta las guías en `guides/`, usa las plantillas de `templates/`, y SIEMPRE valida con los checklists de `checklists/` antes de entregar. Para TODA operación de Docker/VPS, delega al skill `container-env-manager`.
