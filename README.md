# Ejecución Secuencial en Python

Script en Python que simula la preparación de un desayuno. Las tareas se ejecutan **una tras otra**: cada una espera a que termine la anterior (ejecución secuencial).

## Tareas del ejemplo

| Orden | Tarea                    | Duración |
|-------|--------------------------|----------|
| 1     | Hervir agua para el café | 3 s      |
| 2     | Tostar el pan            | 2 s      |
| 3     | Freír los huevos         | 3 s      |

Tiempo total esperado: **~8 segundos** (la suma de todas las tareas).

## Requisitos

- [Docker](https://docs.docker.com/get-docker/) instalado y en ejecución
- Docker Compose (incluido en Docker Desktop)

Para verificar la instalación:

docker --version
docker compose version

## Cómo ejecutar el script

### 1. Clonar el repositorio

git clone https://github.com/GabrielBaezJ/Baez-Gabriel-Secuencial-Python-Tarea-1.git

### 2. Entrar a la carpeta del proyecto

cd TU_REPOSITORIO

### 3. Ejecutar con Docker Compose

docker compose run --rm python-app python 01_secuencial.py  

Docker descargará la imagen `python:3.11-alpine` (solo la primera vez) y ejecutará el script automáticamente.

## Salida esperada

Iniciando: Hervir agua para el café...
Terminado: Hervir agua para el café (3 s).
Iniciando: Tostar el pan...
Terminado: Tostar el pan (2 s).
Iniciando: Freír los huevos...
Terminado: Freír los huevos (3 s).
Tiempo total del desayuno: 8.00 segundos.