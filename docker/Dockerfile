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
ARG simulate_removal
RUN apk add --no-cache --virtual .build-dependencies \
    gcc \
    git \
    linux-headers \
    musl-dev \
    && \
    poetry install ${dev} && \
    apk del ${simulate_removal} .build-dependencies

COPY search/ search/

CMD ["uwsgi", "--ini=uwsgi.ini"]
HEALTHCHECK --interval=5s CMD sh -c 'nc -z localhost 9000'
