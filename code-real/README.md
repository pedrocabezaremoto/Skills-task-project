# 🔴 Code-Real — Módulo F2P para Outlier Real Coder

**Módulo independiente dentro de `container-env-manager`.**
Implementa la metodología Fail-to-Pass (F2P) para proyectos de Outlier Real Coder.

---

## 📚 Base de Conocimiento (Onboarding)
- [Informe Completo Onboarding (26/03/2026)](./onboarding_report.md) — Resumen de respuestas, conceptos F2P, reglas de Docker y anti-patrones QC.

---

## 📐 Arquitectura del Módulo

```
code-real/
├── README.md        ← Este archivo (punto de entrada del módulo)
├── Dockerfile       ← Entorno Ubuntu 22.04 + pytest (sin COPY de proyecto)
├── run.sh           ← Ejecutor de pytest → genera report.json
└── parsing.py       ← Traductor report.json → output.json (formato Outlier)
```

---

## 🔄 Flujo de Trabajo F2P (Fail-to-Pass)

```
┌─────────────────────────────────────────────────────────┐
│  FASE 1 — Evidence A (Estado: FALLO CONTROLADO)         │
│                                                         │
│  1. solution.py está VACÍO                              │
│  2. bash run.sh → pytest falla → report.json            │
│  3. python3 parsing.py → output.json { "status": "FAILED" } │
│  4. bash validation.sh → genera before.json ✅          │
└─────────────────────────────────────────────────────────┘
                          ↓  Inyectar Golden Patch
┌─────────────────────────────────────────────────────────┐
│  FASE 2 — Evidence B (Estado: 100% PASS)                │
│                                                         │
│  1. solution.py tiene el Golden Patch completo          │
│  2. bash run.sh → pytest pasa al 100% → report.json     │
│  3. python3 parsing.py → output.json { "status": "PASSED" } │
│  4. bash validation.sh → genera after.json ✅           │
└─────────────────────────────────────────────────────────┘
```

---

## ⚙️ Comandos de Ejecución (En el VPS)

### 1. Construir la imagen Docker

```bash
cd /ruta/a/tu/proyecto
docker build -t outlier-f2p-env /ruta/a/code-real/
```

### 2. Ejecutar el contenedor (montando el proyecto por volumen)

```bash
# $(pwd) debe ser la carpeta raíz de tu proyecto Real Coder
docker run -it --rm -v $(pwd):/workspace outlier-f2p-env bash
```

### 3. Dentro del contenedor — Ciclo F2P completo

```bash
# Descargar el validador oficial de Outlier
wget "https://static.remotasks.com/uploads/687ec73b0098caae064ded24/real_coder_validation_03_03.sh" -O validation.sh
chmod +x validation.sh

# --- EVIDENCE A (antes del Golden Patch) ---
# Asegúrate de que solution.py está vacío, luego:
bash run.sh          # pytest falla → genera report.json
python3 parsing.py   # traduce → genera output.json { "status": "FAILED" }
bash validation.sh   # genera before.json ✅

# --- (Pegar el Golden Patch en solution.py) ---

# --- EVIDENCE B (después del Golden Patch) ---
bash run.sh          # pytest pasa al 100% → genera report.json
python3 parsing.py   # traduce → genera output.json { "status": "PASSED" }
bash validation.sh   # genera after.json ✅
```

---

## 📄 Formato de output.json (Contrato con Outlier)

```json
{
  "status": "PASSED",
  "tests": [
    {
      "name": "test_nombre_de_funcion",
      "status": "passed",
      "message": ""
    },
    {
      "name": "test_otro_caso",
      "status": "failed",
      "message": "AssertionError: expected 5 got 3"
    }
  ]
}
```

**Regla**: `status` global es `PASSED` **solo si el 100%** de los tests tienen `status: passed`.

---

## 🚫 Reglas Obligatorias (Outlier Compliance)

| Regla | Descripción |
|---|---|
| ❌ No `COPY` | El Dockerfile no copia archivos del proyecto. Se usa `-v` (volumen). |
| ❌ No Solution Leaking | Los tests evalúan comportamiento (qué), no implementación (cómo). |
| ✅ Ubuntu 22.04 | Imagen base obligatoria. |
| ✅ pytest + pytest-json-report | Instalado por `RUN pip3 install` en el Dockerfile. |
| ✅ Escala 1-3-5 | Calificación Aether: prohibido usar 2 o 4. |
| ✅ Evidence A/B | `before.json` (fallo) y `after.json` (100% pass) son obligatorios para Submit. |

---

## 🔗 Dependencias del Módulo Padre

Este módulo es activado desde:
- `container-env-manager/SKILL.md` → Sección de Módulos
- `container-env-manager/scripts/ssh-remote-runtime.md` → Conectividad VPS (requerida)

**Paso [5] del Session Startup Protocol** del padre apunta a este módulo para proyectos Real Coder.
