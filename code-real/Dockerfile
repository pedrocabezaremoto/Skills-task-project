# ==============================================================================
# Dockerfile — Outlier Real Coder | F2P Validation Environment
# Módulo: code-real | Imagen: ubuntu:22.04
# REGLA CRÍTICA: Prohibido usar COPY para archivos del proyecto
# ==============================================================================

FROM ubuntu:22.04

# Evitar prompts interactivos durante apt-get (ej. selección de zona horaria)
ENV DEBIAN_FRONTEND=noninteractive

# --- Instalación de dependencias del sistema ---
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-setuptools \
    wget \
    bash \
    curl \
    && rm -rf /var/lib/apt/lists/*

# --- Instalación de dependencias de Python para testing ---
# pytest: framework de pruebas estándar de Outlier
# pytest-json-report: genera el report.json que parsing.py necesita leer
RUN pip3 install --no-cache-dir \
    pytest \
    pytest-json-report

# --- Directorio de trabajo donde se montarán los archivos por volumen ---
# Los archivos se inyectan con: docker run -v $(pwd):/workspace
# Nunca con COPY (regla Outlier)
WORKDIR /workspace

# --- El contenedor permanece en bash para operación interactiva ---
CMD ["/bin/bash"]
