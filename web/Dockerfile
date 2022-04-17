FROM python:slim

RUN mkdir /app

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY zuman zuman
COPY main.py .
COPY db-sync .

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]
