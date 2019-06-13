FROM python:3.7.3-slim as base
ENV PATH="/root/.poetry/bin:$PATH"
ENV FLASK_APP=search
WORKDIR /srv/app
COPY ./pyproject.toml ./poetry.lock ./
RUN set -ex \
    && apt-get update -yq \
    && apt-get install -yq --no-install-recommends curl \
    && curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python \
    && poetry config settings.virtualenvs.create false \
    && apt-get remove --purge --autoremove -yq curl \
    && rm -rf ~/.cache/* \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*
RUN set -ex \
    && apt-get update -yq \
    && apt-get install -yq --no-install-recommends build-essential \
    && poetry install --no-dev \
    && apt-get remove --purge --autoremove -yq curl build-essential \
    && rm -rf ~/.cache/* \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*
COPY search/ search/


FROM base as dev
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
RUN set -ex \
    && apt-get update -yq \
    && apt-get install -yq --no-install-recommends git \
    && poetry install \
    && apt-get remove --purge --autoremove -yq git \
    && rm -rf ~/.cache/* \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*


FROM base as prod
RUN useradd -s /bin/bash uwsgiuser
USER uwsgiuser
CMD ["uwsgi", "--ini=uwsgi.ini"]
HEALTHCHECK --interval=5s CMD sh -c 'nc -z localhost 9000'
