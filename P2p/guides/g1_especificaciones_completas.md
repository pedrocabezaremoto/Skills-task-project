# G1 — Especificaciones Completas: Hawkins Experiments

> Guía maestra que consolida todas las reglas del proyecto.

---

## 1. Clasificación de Tareas

| Tipo | Descripción | Método de Calificación |
|------|-------------|------------------------|
| **R/M** (Refactoring/Maintainability) | Mejora de estructura, migraciones, estándares | Rúbrica + Unit Tests |
| **PO** (Performance Optimization) | Velocidad, memoria, latencia, eficiencia I/O | Métricas cuantitativas + Unit Tests |

La elección del tipo depende del PR de GitHub proporcionado y del prompt que se redacte.

---

## 2. Entregables Comunes (Core 6)

Toda tarea, sin importar su tipo, requiere:

1. **Prompt** — Descripción del problema orientada al usuario
2. **Dockerfile** — Entorno de ejecución reproducible
3. **Run Script** (`run_script.sh`) — Ejecuta pruebas unitarias existentes para detectar regresiones
4. **Parsing File** (`parsing.py`) — Procesa resultados y genera JSON formateado
5. **Golden Patch** (`golden.patch`) — La solución "estándar de oro"
6. **User-Facing Problem Description** — Resumen breve del problema

---

## 3. Entregables Específicos por Tipo

### R/M (Refactoring/Maintainability)
- **Rúbrica** de 15-20 criterios objetivos con pesos 1/3/5

### PO (Performance Optimization)
- **Target Functions** — Funciones específicas donde está el cuello de botella
- **Reproduction Script** (`reproduction_script.sh`) — Mide rendimiento con formato `METRIC_VALUE: <número>`

---

## 4. Reglas Críticas del Dockerfile

| Regla | Detalle |
|-------|---------|
| ✅ Commit SHA | Usar el hash del commit padre del PR (PROHIBIDO usar branch names) |
| ✅ Agnóstico | No especificar arquitecturas como x86_64 o AArch64 |
| ❌ Sin COPY | Prohibido COPY para: `run_script.sh`, `reproduction_script.sh`, `golden.patch`, `parsing.py` |
| ✅ Dependencias | Instalar TODAS las librerías necesarias para compilar y ejecutar tests |
| ✅ Submódulos | Inicializar recursivamente si el repo los tiene |

---

## 5. Reglas Críticas del Prompt

- **Autocontenido:** Toda la información necesaria dentro del prompt
- **Sin pistas:** No incluir la solución, algoritmos específicos, ni referencias al PR/Golden Patch
- **Sin segunda persona:** No usar "you"
- **Preservar funcionalidad:** No solicitar cambios que alteren el comportamiento observable

### Plantilla Obligatoria
```
## Context
## Problem Statement
## Requirements
## Success Criteria
## Files to Modify
## Notes
```

---

## 6. Reglas del Golden Patch

- Formato **unified diff** con extensión `.patch`
- Se aplica **limpiamente** sobre el commit configurado en el Dockerfile
- Solo contiene cambios **estrictamente necesarios**
- Pasa TODAS las validaciones del script `e2e.sh`
- [R/M] Debe tener PASS en todos los criterios de la rúbrica
- Sigue mejores prácticas: documentación, nombres lógicos, código limpio

---

## 7. Flujo de Validación (e2e.sh)

```
1. Build Docker image
2. Run container
3. Ejecutar reproduction_script.sh (Pre-parche)
4. Ejecutar run_script.sh (Tests deben pasar)
5. Ejecutar parsing.py → before.json
6. Aplicar golden.patch
7. Ejecutar reproduction_script.sh (Post-parche)
8. Ejecutar run_script.sh (Tests deben SEGUIR pasando)
9. Ejecutar parsing.py → after.json
```

**Regla:** Está PROHIBIDO modificar `e2e.sh`. Si falla, corregir NUESTROS archivos.

---

## 8. Errores Comunes que Invalidan Tareas

| Error | Solución |
|-------|----------|
| Métricas no deterministas | Usar seeds fijas, warm-up runs, mediana de varias ejecuciones |
| Pistas en el prompt | Reescribir sin sugerir algoritmos o soluciones |
| Branch names en Dockerfile | Reemplazar por SHA del commit |
| Benchmarks simulados (PO) | Ejecutar el código REAL del repositorio |
| Rúbricas sin editar del LLM | Editar exhaustivamente cada criterio generado |

---

## 9. Checklist Final de Envío

- [ ] URL fuente pública y accesible
- [ ] Dockerfile construye sin errores vía `e2e.sh`
- [ ] Golden Patch se aplica limpiamente y resuelve el 100%
- [ ] `before.json` y `after.json` idénticos (todas las pruebas PASSED)
- [ ] Script de reproducción (PO) genera `METRIC_VALUE: <número>`
- [ ] Rúbrica (R/M) es objetiva, en presente, sin "The model..."
