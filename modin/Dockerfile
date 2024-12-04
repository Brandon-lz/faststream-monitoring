FROM python:3.11

ENV SRC_DIR /app

WORKDIR ${SRC_DIR}

COPY ./pyproject.toml .
COPY ./pdm.lock .

ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache pdm  && pdm install --check --prod --no-editable && pdm cache clear

