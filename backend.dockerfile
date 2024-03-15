FROM python:3.11.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY pyproject.toml poetry.lock /

RUN pip3 install poetry

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction

WORKDIR /app

COPY backend .

COPY messages.json /app