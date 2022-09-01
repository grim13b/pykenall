FROM python:3.10-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/app

RUN pip install pipenv

COPY Pipfile ./
COPY Pipfile.lock ./
COPY src ./src
COPY assets ./assets

RUN pipenv install

ENTRYPOINT ["pipenv", "run", "uvicorn", "--host", "0.0.0.0", "src.main:app", "--reload"]