FROM python:3.9

RUN pip install fastapi uvicorn pytest

EXPOSE 8000

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
