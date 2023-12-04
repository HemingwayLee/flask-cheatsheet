FROM python:3.8@sha256:7264a50439679c2868a99f71a5c9b9831cc082b1d3f05c8643788e1d7914afeb

RUN mkdir -p /home/app
COPY . /home/app
WORKDIR /home/app

RUN pip3 install -r requirements.txt

CMD python3 flask_svr.py

