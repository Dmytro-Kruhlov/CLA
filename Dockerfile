FROM python:3.10

WORKDIR /app

COPY CLA /app/CLA

COPY pyproject.toml /app

COPY CLA/main.py /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install

ENTRYPOINT ["python", "main.py"]