FROM python:3.7.4

WORKDIR /app

ENV FLASK_ENV development
ENV FLASK_APP run.py

ENV MAIL_USERNAME 'blog.ianhamilton.noreply'
ENV MAIL_PASSWORD 'pass-007-001'

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["/usr/local/bin/flask", "run", "--host=0.0.0.0"]
