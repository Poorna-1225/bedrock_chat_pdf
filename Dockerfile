FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt
COPY . ./

CMD ["uvicorn", "fastapi_api:app", "--host", "0.0.0.0", "--port", "8000"] 