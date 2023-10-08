FROM python:slim

RUN mkdir /app

WORKDIR /app

RUN apt -y update && apt install -y build-essential libpq-dev git
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY db-sync .
COPY main.py .
COPY zuman zuman

ENTRYPOINT [ "gunicorn" ]

CMD ["-w 9", "-b", "0.0.0.0:8000", "main:app"]