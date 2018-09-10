FROM python:3.7-alpine

COPY Requirements/requirements.txt Requirements/

RUN pip install -r Requirements/requirements.txt

COPY . /app

ENV FLASK_APP server.py

EXPOSE 5000

CMD entry.sh