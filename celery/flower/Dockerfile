FROM python:3.8

RUN apt-get update && apt-get install -y tmux 

RUN mkdir -p /home/app
COPY . /home/app
WORKDIR /home/app

RUN pip3 install -r requirements.txt
# Celery is installed 
RUN pip3 list
