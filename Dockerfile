# pull official base image
FROM python:3.11.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/usr/src/app/src

# copy project metadata and source code
COPY pyproject.toml /usr/src/app/pyproject.toml
COPY src /usr/src/app/src

# install dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
         openssl-dev libffi-dev gcc musl-dev python3-dev \
        postgresql-dev bash \
    && pip install --upgrade pip setuptools wheel \
    && pip install -e . \
    && rm -rf /root/.cache/pip

