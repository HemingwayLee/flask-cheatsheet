FROM python:3.8

RUN mkdir -p /home/app
COPY . /home/app
WORKDIR /home/app

RUN pip3 install -r requirements.txt

# CMD celery -A hello worker --loglevel=INFO && python3 /home/app/app.py
CMD celery -A hello worker --loglevel=INFO 
