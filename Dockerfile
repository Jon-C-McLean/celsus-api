FROM python:3.9

WORKDIR /code

COPY . .

RUN pip install .

CMD ["uvicorn", "src.api.api:app", "--host", "0.0.0.0", "--port", "8000"]