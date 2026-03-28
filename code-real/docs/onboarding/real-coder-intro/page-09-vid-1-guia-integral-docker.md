# Guía Integral de Docker: Fundamentos, Orquestación y Mejores Prácticas

## Resumen Ejecutivo

Docker es una plataforma de software diseñada para despliegear y ejecutar aplicaciones mediante el uso de contenedores. Su función principal es resolver el problema de la inconsistencia entre entornos de desarrollo y producción (el fenómeno conocido como "funciona en mi máquina"). A diferencia de las máquinas virtuales, los contenedores de Docker son ligeros, se inician en segundos y utilizan el kernel del sistema operativo host para ofrecer un rendimiento cercano al nativo.

---

## 1. Fundamentos de Docker

### ¿Qué es Docker y qué problemas resuelve?
Docker utiliza contenedores, que son grupos aislados de procesos con su propio sistema de archivos, dependencias y paquetes. Esto elimina conflictos entre dependencias ocultas y asegura que la aplicación se ejecute de manera idéntica en cualquier sistema.

**Problemas que soluciona:**
* Inconsistencias de código al transferirlo entre computadoras.
* Fallas en producción a pesar de pasar pruebas locales.
* Dificultades en la instalación de dependencias y actualizaciones del sistema host que rompen aplicaciones existentes.
* Conflictos entre aplicaciones instaladas en un mismo sistema.

### Contenedores vs. Máquinas Virtuales (VMs)

| Característica | Máquinas Virtuales | Contenedores Docker |
| :--- | :--- | :--- |
| **Arquitectura** | Emulan hardware, kernel y drivers completos. | Utilizan el kernel, hardware y red del host. |
| **Rendimiento** | Significativamente más lentas por el "overhead". | Rendimiento cercano al nativo. |
| **Tamaño** | Gigabytes. | Megabytes. |
| **Inicio** | Minutos. | Menos de un segundo. |

---

## 2. Conceptos Clave y Operaciones Básicas

### Imágenes vs. Contenedores
* **Imágenes:** Son plantillas o "recetas" inmutables. Especifican el sistema de archivos, aplicaciones, variables de entorno y el comando por defecto.
* **Contenedores:** Son las instancias de ejecución de las imágenes. Se pueden tener múltiples contenedores ejecutándose simultáneamente basados en una sola imagen.

### Comandos Esenciales
* `docker pull [imagen]`: Descarga una imagen del registro.
* `docker run [imagen]`: Crea y arranca un contenedor. Flags comunes: `-p` (mapeo de puertos), `-d` (segundo plano/detached), `--name` (nombre personalizado), `--rm` (borrar al detener).
* `docker ps`: Lista contenedores en ejecución (`-a` para incluir detenidos).
* `docker logs [id/nombre]`: Muestra la salida de consola del contenedor.
* `docker stop [id/nombre]`: Detiene el contenedor.
* `docker exec -it [id/nombre] [comando]`: Ejecuta un proceso (como un shell) dentro de un contenedor activo.

---

## 3. Gestión y Optimización de Imágenes

### Etiquetado y Seguridad
Docker permite identificar versiones mediante etiquetas (tags) y firmas digitales (digests).
* **Tags:** Funcionan como enlaces simbólicos (ej. `enginex:1.27`). Son legibles pero pueden actualizarse, lo que introduce riesgos de inestabilidad en producción.
* **Digests:** Utilizan un hash SHA256 (ej. `image@sha256:...`). Es la única forma de garantizar que el entorno sea idéntico. **Recomendación:** Usar digests en producción.

### Tipos de Imágenes (Tamaño y Eficiencia)
* **Default:** Basadas en distribuciones completas (ej. Debian), suelen ser pesadas (>1 GB).
* **Slim:** Basadas en versiones minimalistas de Debian.
* **Alpine:** Basadas en Alpine Linux. Son extremadamente pequeñas (~55 MB), pero requieren precaución ya que usan `musl libc` en lugar de `glibc`.

---

## 4. Persistencia de Datos y Redes

### Tipos de Montajes (Mounts)
* **Volumes:** Gestionados por Docker. Ideales para producción y entornos de nube, ya que abstraen el sistema de archivos del host.
* **Bind Mounts:** Mapean un directorio o archivo específico del host al contenedor. Preferibles en desarrollo para ver cambios en tiempo real.

### Mapeo de Puertos
Los contenedores están aislados de la red del host por defecto. El flag `-p [puerto_host]:[puerto_contenedor]` permite publicar servicios.

---

## 5. Construcción de Imágenes Personalizadas (Dockerfile)

* **FROM:** Imagen base.
* **WORKDIR:** Define el directorio de trabajo interno.
* **COPY:** Transfiere archivos del host a la imagen.
* **RUN:** Ejecuta comandos durante la construcción.
* **CMD:** Comando que se ejecuta al iniciar el contenedor.

### Capas (Layers) y Caché
Cada comando en un Dockerfile crea una capa. Las capas se almacenan en caché para acelerar futuras construcciones. **Importancia del orden:** Si una capa cambia, todas las capas posteriores deben reconstruirse.

### Construcciones Multi-etapa (Multi-stage Builds)
Permiten separar el entorno de compilación del entorno de ejecución, reduciendo drásticamente el tamaño de la imagen final y mejorando la seguridad.

---

## 6. Orquestación con Docker Compose

Docker Compose gestiona aplicaciones compuestas por múltiples contenedores.
* **Archivo docker-compose.yml:** Define servicios, redes y volúmenes.
* **Redes aisladas:** Compose crea automáticamente una red donde los contenedores pueden comunicarse entre sí usando sus nombres de servicio como nombres de host.

**Comandos:**
* `docker compose up`: Construye e inicia todos los servicios.
* `docker compose down`: Detiene y elimina los contenedores creados.

---

## 7. Gestión de Secretos y Despliegue

* **Variables de Entorno:** Utilizar archivos `.env` (añadidos al `.gitignore`) para almacenar variables sensibles.
* **Registros de Imágenes:** Para compartir imágenes se utilizan registros como Docker Hub (`docker tag`, `docker login`, `docker push`).
* **Despliegue:** Docker puede usarse para desarrollo local o en producción mediante servicios gestionados.
