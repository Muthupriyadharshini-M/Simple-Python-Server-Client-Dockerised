FROM ubuntu

RUN apt-get -y update
RUN apt-get -y install sudo
RUN apt-get install -y python3
RUN apt-get -y install python3-pip

COPY data.json /home/data.json
COPY server.py /opt/sourcecode/server.py
