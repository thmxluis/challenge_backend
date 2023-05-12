# Challenge Backend

Este es un proyecto de ejemplo que utiliza el framework FastAPI para construir una API web.

## Descripción del proyecto

El proyecto consiste en una API para gestionar servicios. Proporciona endpoints para crear servicios, obtener una lista de servicios y obtener un servicio por su ID.
Para completar con el challenge backend

## Características

- Crear un nuevo servicio
- Obtener una lista de servicios
- Obtener un servicio por su ID

## Requisitos previos

- Docker
- Docker Compose

## Instalación

```markdown

1. Clona este repositorio en tu máquina local:

git clone <https://github.com/thmxluis/challenge_backend.git>

2. Accede al directorio del proyecto:
```markdown
> docker-compose up -d --build
```

3. Accede a la documentación de la API:

```
- <http://localhost:8000/docs> (Swagger)
- <http://localhost:8000/redoc> (Redoc)

```

## Ejecución de tests

```markdown
> docker-compose exec app pytest
````
