# G3 — Guía de Referencia Rápida de Docker: Hawkins Experiments

> Contenedorización estandarizada para garantizar reproducibilidad y eficiencia.

---

## 1. Estructura del Dockerfile

### Secciones NO Modificables (Obligatorias)
```dockerfile
# Directorio de trabajo fijo
RUN mkdir /app
WORKDIR /app

# Punto de entrada fijo
ENTRYPOINT ["/bin/bash"]
```

### Secciones Configurables (TODO)
```dockerfile
# 1. Imagen base — Elegir según el proyecto
FROM python:3.10-slim

# 2. Dependencias del sistema
RUN apt-get update && apt-get install -y \
    git python3 python3-pip python3-setuptools python-is-python3 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 3. Clonar repositorio y fijar commit
RUN git clone <repo-url> /app/repo
WORKDIR /app/repo
RUN git checkout <commit-sha>
RUN git submodule update --init --recursive  # Si aplica

# 4. Instalar dependencias del proyecto
RUN pip install -r requirements.txt  # O equivalente
```

---

## 2. Imágenes Base Recomendadas

| Imagen | Tag | Caso de Uso |
|--------|-----|-------------|
| **Python** | `python:3.10-slim` | Proyectos basados en Python |
| **Node.js** | `node:20-slim` | Proyectos JavaScript/TypeScript |
| **Ubuntu** | `ubuntu:22.04` | Configuraciones complejas o multi-lenguaje |

---

## 3. Comandos Operativos

### Construcción
| Acción | Comando |
|--------|---------|
| Build estándar | `docker build -t hawkins-task:v1 .` |
| Build sin caché | `docker build --no-cache -t hawkins-task:v1 .` |

### Ejecución
| Acción | Comando |
|--------|---------|
| Run interactivo | `docker run -it --rm hawkins-task:v1` |
| Montar volumen | `docker run -it --rm -v $(pwd)/patch:/patch hawkins-task:v1` |
| Ejecutar script | `docker run --rm hawkins-task:v1 -c "./validation_script.sh"` |

### Depuración
| Acción | Comando |
|--------|---------|
| Listar containers | `docker ps` |
| Shell en container | `docker exec -it <container_id> /bin/bash` |
| Logs del container | `docker logs <container_id>` |
| Inspeccionar capas | `docker history hawkins-task:v1` |

### Limpieza
| Acción | Comando |
|--------|---------|
| Eliminar containers detenidos | `docker container prune` |
| Eliminar imágenes sin usar | `docker image prune` |
| Limpieza total | `docker system prune -a` |

---

## 4. Reglas Específicas de Hawkins

| Regla | Detalle |
|-------|---------|
| ✅ SHA commits | Siempre usar `git checkout <sha>`, nunca branch names |
| ✅ Agnóstico | No especificar arquitecturas de hardware |
| ❌ Sin COPY | Prohibido COPY para scripts de evaluación y parches |
| ✅ Dependencias | Instalar TODO lo necesario para compilar y ejecutar |
| ✅ ENTRYPOINT | Siempre `/bin/bash` |
| ✅ WORKDIR | Siempre `/app` |
