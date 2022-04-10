FROM python:3.9.12-slim

RUN mkdir /app

WORKDIR /app

COPY zuman zuman
COPY main.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]
