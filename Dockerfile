FROM python

RUN mkdir /app

WORKDIR /app

COPY zuman .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]
