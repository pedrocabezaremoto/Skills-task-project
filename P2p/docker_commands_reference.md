# Docker Commands Reference — Skills Task Project

## CONSTRUCCION DE IMAGENES

| Comando | Qué hace |
|---|---|
| `docker build -t <nombre> .` | Construye una imagen Docker desde el Dockerfile en la carpeta actual |
| `docker build -t <nombre> <ruta>` | Lo mismo pero apuntando a una carpeta específica |
| `docker build --no-cache -t <nombre> .` | Construye ignorando el caché, fuerza reinstalar todo desde cero |

---

## EJECUCION DE CONTENEDORES

| Comando | Qué hace |
|---|---|
| `docker run <imagen>` | Crea y ejecuta un contenedor |
| `docker run -it <imagen>` | Lo ejecuta de forma interactiva (puedes escribir comandos adentro) |
| `docker run --rm <imagen>` | El contenedor se elimina automáticamente al terminar |
| `docker run -v $(pwd):/app <imagen>` | Conecta tu carpeta local a `/app` dentro del contenedor (volumen) |
| `docker run -w /app <imagen>` | Define el directorio de trabajo dentro del contenedor |
| `docker run --name <nombre> <imagen>` | Le pone un nombre personalizado al contenedor |
| `docker run -d <imagen>` | Lo ejecuta en segundo plano (background) |
| `docker run -p 8080:80 <imagen>` | Mapea un puerto del contenedor a tu máquina |

---

## INSPECCION Y DEPURACION

| Comando | Qué hace |
|---|---|
| `docker ps` | Lista los contenedores que están corriendo ahora mismo |
| `docker ps -a` | Lista todos los contenedores, incluyendo los detenidos |
| `docker logs <id>` | Muestra lo que el contenedor imprimió en consola |
| `docker exec -it <id> /bin/bash` | Abre una terminal dentro de un contenedor que ya está corriendo |
| `docker history <imagen>` | Muestra las capas que componen una imagen |

---

## DETENCION

| Comando | Qué hace |
|---|---|
| `docker stop <id>` | Detiene un contenedor en ejecución |

---

## LIMPIEZA

| Comando | Qué hace |
|---|---|
| `docker container prune` | Elimina todos los contenedores que están detenidos |
| `docker image prune` | Elimina imágenes que no están siendo usadas |
| `docker system prune -a` | Limpieza total: elimina contenedores, imágenes y caché sin usar |

---

## REGISTRO DE IMAGENES (Docker Hub)

| Comando | Qué hace |
|---|---|
| `docker pull <imagen>` | Descarga una imagen desde Docker Hub |
| `docker push <imagen>` | Sube tu imagen a Docker Hub |
| `docker tag <imagen> <nuevo-nombre>` | Le pone una etiqueta/nombre alternativo a una imagen |
| `docker login` | Te autentica en Docker Hub |

---

## FLUJO TIPICO EN PROYECTOS F2P Y P2p

Estos son los comandos que aparecen constantemente en los scripts y workflows del proyecto:

```bash
# 1. Construir la imagen
docker build -t hawkins-task:v1 .

# 2. Ejecutar pruebas antes del parche (Evidence A)
docker run --rm -v $(pwd):/app hawkins-task:v1 bash -c "./run.sh"

# 3. Aplicar parche y volver a probar (Evidence B)
docker run --rm -v $(pwd):/app hawkins-task:v1 bash -c "patch -p1 < golden.patch && ./run.sh"

# 4. Si algo falla, inspeccionar
docker ps -a
docker logs <id>
docker exec -it <id> /bin/bash
```
