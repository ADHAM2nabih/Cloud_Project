
FROM python:3.9


ENV MYSQL_HOST=3306 \
    MYSQL_USER=root \
    MYSQL_PASSWORD=ADHAMMOHAMED123456789 \
    MYSQL_DATABASE=mysql_db


WORKDIR /app

COPY . /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
