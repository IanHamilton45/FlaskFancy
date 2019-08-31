FROM python:3.6

WORKDIR /app

ENV FLASK_ENV development
ENV FLASK_APP run.py
#UPDATE THESE
ENV EMAIL_USER 
ENV EMAIL_PASS

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["/usr/local/bin/flask", "run", "--host=0.0.0.0"]
