FROM python:3.7.2-alpine3.8

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PATH="/root/.poetry/bin:$PATH"
ENV FLASK_APP=search

WORKDIR /srv/app

RUN rm -rf /var/cache/apk/* && \
    rm -rf /tmp/* && \
    apk update && \
    apk add --no-cache \
    bash \
    grep \
    libxslt-dev

RUN apk add --no-cache --virtual .build-dependencies \
    curl \
    && \
    curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python && \
    poetry config settings.virtualenvs.create false && \
    apk del .build-dependencies

COPY ./pyproject.toml ./poetry.lock ./

ARG dev
RUN apk add --no-cache --virtual .build-dependencies \
    gcc \
    git \
    musl-dev \
    && \
    poetry install ${dev} && \
    apk del .build-dependencies

COPY search/ search/
