FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
ENV FLASK_APP manage.py

EXPOSE 5000

RUN flask db upgrade

CMD ["flask", "run", "--host=0.0.0.0"]