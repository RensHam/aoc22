FROM python:3.11 as base

WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends gcc curl


RUN pip install pdm

FROM base as packaged

COPY ./pyproject.toml /app
COPY ./pdm.lock /app


RUN pdm export -o requirements.txt
RUN pip install -r requirements.txt

FROM base as production

COPY ./pyproject.toml /app
COPY ./pdm.lock /app


RUN pdm export -o requirements.txt --prod
RUN pip install -r requirements.txt

COPY . /app
