# Flask Api REST

Este repositorio contiene el codigo


## Install flask

```bash
$ pip install Flask
```

### Extensiones

Used extensions:
* [flask-cors](https://flask-cors.readthedocs.io/en/latest/)
* [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)
* [flask-marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
* [flask-migrate](https://flask-migrate.readthedocs.io/en/latest/)


**Flask_cors**
```bash
$ pip install flask_cors
```

**Flask-SQLAlchemy**
```bash
$ pip install Flask-SQLAlchemy
```

**flask-marshmallow**
```bash
$ pip install flask-marshmallow marshmallow-sqlalchemy
```

**Flask-Migrate**
```bash
$ pip install Flask-Migrate
```

## Pre-commit

Instala  [precommit](https://pre-commit.com/), para configurar crea un archivo **.pre-commit-config.yaml**
```bash
$ pip install pre-commit
```

El archivo deberia tener el sig. contenido
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.0.1
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black
        language_version: python3.10
  - repo: https://github.com/astral-sh/ruff-pre-commit
    # Ruff version.
    rev: v0.3.1
    hooks:
      # Run the linter.
      - id: ruff
      # Run the formatter.
      - id: ruff-format
```
Ejecuta la instalación y estas listo para usarlo

```bash
$ pre-commit install
```

Puedes ejecutar los hooks para validar la instalación de la sig. manera
```bash
$ pre-commit run --all-files
```

## Migrations

Se requiere inicializar Flask-Migrate con el sig. comando:
```bash
$ flask db init
```
Crea la migracion inicial
```bash
$ flask db migrate -m "Initial migration."
```
Ejecuta la migracion
```bash
$ flask db upgrade
```

se genera la carpeta migrations, con archivos de configuracion,
deberias ver algo muy similar a esto:

```bash
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       ├── 81f06d2c7c17_initial_migration.py
│       └── __pycache__
│           └── 81f06d2c7c17_initial_migration.cpython-310.pyc
```

## Minio

Minio es una aplicacion que permite almacenar archivos con una interfaz
compatible con AWS S3. Por lo que es ideal para integraciones de prueba.

Para utilizarlo en docker es necesario seguir los sog. pasos.

1. Descarga la imagen de MinIO

```bash
docker pull minio/minio
```

2. Crea la carpeta para almacenar o montar el contenedor
```bash
$ export MINIO_DIR=$(pwd)/minio
$ mkdir -p $MINIO_DIR
```

3. Genera la llave de acceso y secreto de MinIO
```bash
$ export MINIO_ACCESS_KEY=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
# this one is actually a secret, so careful
$ export MINIO_SECRET_KEY=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
```

4. Levanta el contenedor
```bash
$ docker run -p 9000:9000 \
        -v $MINIO_DIR:/data \
        -e "MINIO_ACCESS_KEY=$MINIO_ACCESS_KEY" \
        -e "MINIO_SECRET_KEY=$MINIO_SECRET_KEY" \
        minio/minio server /data
```

### Minio python

install minio package

```bash
$ pip install minio
```


# Image RESt api
