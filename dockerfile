FROM python:3.11.2

#RUN mkdir -p /turnero/app
#COPY . /turnero/app
#WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

RUN python manage.py makemigrations && \
    python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]