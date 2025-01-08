FROM python:3.12-alpine

MAINTAINER Some Dev

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.2 \
    POETRY_NO_INTERACTION=1 \
    DEBIAN_FRONTEND=noninteractive \
    COLUMNS=80

RUN apk update
RUN apk add --no-cache gcc musl-dev mariadb-dev curl

RUN mkdir /app
WORKDIR /app

ENV POETRY_HOME=/usr/local/poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$POETRY_HOME/bin:$PATH

COPY pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry lock
RUN poetry install

#RUN apk update # (оновить весь репозиторій Linux)
#RUN apk add --no-cache gcc musl-dev mariadb-dev curl # встановлює бібліотеку с++(gcc), mariadb-dev(в якості конектора до sql баз даних і curl(для встановлення poetry)
#
#RUN mkdir /app # створюєм директорію в корні проекту образу Python-alpine
#WORKDIR /app #робимо цю директорію директорією по замовчуванні###
#ENV POETRY_HOME=/usr/local/poetry # вставляєм додатковий енвайрнмент де буде розташований poetry
#RUN curl -sSL https://install.python-poetry.org | python3 - # запускаємо команду встановлення poetry
#ENV PATH=$POETRY_HOME/bin:$PATH # ще один енвайрмент щоб бачити цей poetry
#
#COPY pyproject.toml /app/ # копіюєм наш pyproject.toml в /app
#
#RUN poetry config virtualenvs.create false # Щоб він не створював віртуальне середовище а просто працював з poetry
#
#RUN poetry lock # щоб він створив lock файл
#
#RUN poetry install # встановить залежності які будуть скопійовані з pyproject.toml
