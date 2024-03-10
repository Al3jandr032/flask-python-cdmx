# Flask Api REST

Este repositorio contiene el codigo


## Install flask

```bash
$ pip install Flask
```

### Extensions

Used extensions:
* [flask-cors](https://flask-cors.readthedocs.io/en/latest/)
* [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)
* [flask-marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
* [flask-migrate](https://flask-migrate.readthedocs.io/en/latest/)


#### Flask_cors
```bash
$ pip install flask_cors
```

#### Flask-SQLAlchemy
```bash
$ pip install Flask-SQLAlchemy
```

#### flask-marshmallow
```bash
$ pip install flask-marshmallow marshmallow-sqlalchemy
```

#### Flask-Migrate
```bash
$ pip install Flask-Migrate
```

## Pre-commit

install [precommit](https://pre-commit.com/) and configure

```bash
$ pip install pre-commit
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
