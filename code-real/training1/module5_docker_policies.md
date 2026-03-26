# Módulo 5: Políticas de Docker — Configuración Obligatoria (Onboarding)

> **Documento de Entrenamiento (training1)**
> Basado en: *Reglas de configuración Docker presentadas en el Real Coder Intro Course (Páginas 8-9) y la documentación interna del proyecto.*

---

## 📌 Propósito de este Módulo

Este módulo establece las **políticas obligatorias e inquebrantables** para la configuración del Dockerfile en cualquier tarea Real Coder. Estas reglas fueron confirmadas durante el onboarding y son aplicadas por el sistema de validación automática de Outlier.

**Principio rector:** La reproducibilidad del entorno no es negociable. El Dockerfile es la garantía de que el código se ejecuta idénticamente en cualquier máquina.

---

## 🚫 REGLA #1: Prohibición Absoluta de COPY

> [!CAUTION]
> ### ❌ ESTÁ ESTRICTAMENTE PROHIBIDO usar el comando `COPY` dentro del Dockerfile
> La plataforma Outlier **inyecta los archivos de prueba dinámicamente** en tiempo de ejecución mediante volúmenes Docker.
> Usar `COPY` causaría conflictos con este mecanismo y resultaría en **fallos de validación automática**.

### ¿Por qué está prohibido?
1. **Inyección dinámica:** La plataforma monta los archivos del proyecto como volúmenes en runtime, no durante el build.
2. **Conflicto de archivos:** Si usas `COPY`, los archivos copiados durante el build podrían colisionar con los inyectados en runtime.
3. **Reproducibilidad:** El Dockerfile debe definir solo el **entorno** (sistema operativo, dependencias), no el **código** del proyecto.

### Ejemplo Prohibido vs. Correcto

```dockerfile
# ❌ PROHIBIDO — NUNCA hacer esto
FROM ubuntu:22.04
COPY . /workspace
RUN pip install -r /workspace/requirements.txt

# ❌ PROHIBIDO — Tampoco esto
FROM ubuntu:22.04
COPY run.sh /workspace/run.sh
COPY parsing.py /workspace/parsing.py

# ❌ PROHIBIDO — Ni con ADD
FROM ubuntu:22.04
ADD . /workspace
```

```dockerfile
# ✅ CORRECTO — Solo definir el entorno
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip \
    python3-setuptools \
    python-is-python3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
```

---

## 🐧 REGLA #2: Base Image Estándar

| Parámetro | Valor Obligatorio |
|---|---|
| Base Image | `FROM ubuntu:22.04` |
| Alternativas | No permitidas salvo justificación técnica excepcional |

### Justificación
- Ubuntu 22.04 LTS es la imagen estándar del proyecto.
- Garantiza compatibilidad con todos los scripts de validación.
- El equipo de QC espera esta base para sus auditorías.

---

## 🐍 REGLA #3: Python 3 es OBLIGATORIO

Independientemente del lenguaje principal del proyecto (Node.js, Go, Rust, Java, etc.), **Python 3 debe estar instalado siempre**.

### ¿Por qué?
Los scripts de infraestructura del proyecto están escritos en Python:
- `run.sh` — Ejecuta pytest y genera `report.json`
- `parsing.py` — Traduce `report.json` a `output.json` (formato Outlier)

### Paquetes Python Obligatorios
```dockerfile
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-setuptools \
    python-is-python3
```

### Dependencias Python vía pip
```dockerfile
RUN pip install pytest
```

> **Nota:** `python-is-python3` crea el symlink `/usr/bin/python → /usr/bin/python3`, necesario para que scripts que llaman `python` (sin el 3) funcionen correctamente.

---

## 📂 REGLA #4: WORKDIR Estándar

| Parámetro | Valor |
|---|---|
| WORKDIR | `/workspace` o `/app` |
| Preferido | `/workspace` |

```dockerfile
WORKDIR /workspace
```

### Justificación
- Los scripts de validación (`validation.sh`) esperan encontrar los archivos en el WORKDIR.
- La plataforma monta los volúmenes en esta ruta.

---

## 🔧 REGLA #5: Dependencias del Sistema

Instalar **todas** las dependencias del sistema que el lenguaje principal requiera. Ejemplos por lenguaje:

### Node.js
```dockerfile
RUN apt-get update && apt-get install -y \
    curl \
    python3 python3-pip python3-setuptools python-is-python3 \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*
```

### Go
```dockerfile
RUN apt-get update && apt-get install -y \
    wget \
    python3 python3-pip python3-setuptools python-is-python3 \
    && wget https://go.dev/dl/go1.21.5.linux-amd64.tar.gz \
    && tar -C /usr/local -xzf go1.21.5.linux-amd64.tar.gz \
    && rm go1.21.5.linux-amd64.tar.gz \
    && rm -rf /var/lib/apt/lists/*

ENV PATH=$PATH:/usr/local/go/bin
```

### Rust
```dockerfile
RUN apt-get update && apt-get install -y \
    curl build-essential \
    python3 python3-pip python3-setuptools python-is-python3 \
    && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
    && rm -rf /var/lib/apt/lists/*

ENV PATH=$PATH:/root/.cargo/bin
```

---

## 📋 REGLA #6: Inicialización de Git

El repositorio Git debe inicializarse dentro del Dockerfile:

```dockerfile
RUN git init
```

### Justificación
- El Golden Patch se aplica como un `git apply` o `git diff`.
- Sin repositorio Git inicializado, la aplicación del parche falla.

---

## 🧹 REGLA #7: Limpieza de Caché

Siempre limpiar la caché de apt después de instalar dependencias:

```dockerfile
RUN apt-get update && apt-get install -y \
    [dependencias] \
    && rm -rf /var/lib/apt/lists/*
```

### Justificación
- Reduce el tamaño de la imagen Docker.
- Evita que archivos temporales interfieran con la validación.

---

## 📄 Dockerfile Template Completo (Referencia)

```dockerfile
# ============================================
# Real Coder — Dockerfile Template
# ============================================
# REGLA CRÍTICA: NO usar COPY ni ADD para archivos del proyecto
# La plataforma inyecta archivos dinámicamente en runtime
# ============================================

FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip \
    python3-setuptools \
    python-is-python3 \
    # Agregar dependencias adicionales del lenguaje principal aquí
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias Python para infraestructura
RUN pip install pytest

# Inicializar repositorio Git (necesario para Golden Patch)
RUN git init

# Establecer directorio de trabajo estándar
WORKDIR /workspace
```

---

## ✅ Checklist de Validación del Dockerfile

Antes de entregar, verificar que el Dockerfile:

- [ ] **NO** contiene `COPY` ni `ADD` para archivos del proyecto
- [ ] Usa `FROM ubuntu:22.04` como base image
- [ ] Instala `python3`, `python3-pip`, `python3-setuptools`, `python-is-python3`
- [ ] Instala `pytest` vía pip
- [ ] Instala todas las dependencias del lenguaje principal
- [ ] Tiene `git init` para soporte del Golden Patch
- [ ] Usa `WORKDIR /workspace` (o `/app`)
- [ ] Limpia caché con `rm -rf /var/lib/apt/lists/*`
- [ ] No tiene instrucciones interactivas (usa `DEBIAN_FRONTEND=noninteractive` si necesario)
