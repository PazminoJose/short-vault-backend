# short-vault-backend

Backend FastAPI con SQLModel y Alembic.

## Requisitos
- Python 3.13
- uv (recomendado) o pip
- PostgreSQL

## Configuración rápida
1. Crear y activar el entorno (ejemplo con uv):
	- `uv venv`
	- `./.venv/Scripts/activate`
2. Instalar dependencias:
	- `uv sync`
3. Copiar `.env.example` a `.env` (o crear `.env`) y definir variables de entorno.

## Desarrollo
- Ejecutar API: `fastapi dev src/main.py` (puerto 8000 por defecto).
- Crear migración: `alembic revision --autogenerate -m "mensaje"`.
- Ver rutas (swagger): `http://localhost:8000/docs`.
- Aplicar migraciones: `alembic upgrade head`.

## Estructura relevante
- src/main.py: App FastAPI.
- src/core: config y database.
- src/modules: routers, modelos y servicios de dominio.
- alembic/: configuración y migraciones.
