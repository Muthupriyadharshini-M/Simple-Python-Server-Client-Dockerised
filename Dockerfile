FROM ubuntu as stage1
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install sudo
RUN apt-get install -y python3
RUN apt-get -y install python3-pip
RUN pip3 install requests


FROM ubuntu as stage2
RUN apt-get update && apt-get install -y ffmpeg
RUN apt-get -y install sudo
COPY --from=stage1 /usr/bin/python3.8-config /usr/bin/python3.8-config 
COPY --from=stage1 /usr/bin/python3.8 /usr/bin/python3.8
COPY --from=stage1 /usr/bin/python3 /usr/bin/python3
COPY --from=stage1 /usr/lib/python3.9 /usr/lib/python3.9
COPY --from=stage1 /usr/lib/python3.8 /usr/lib/python3.8
COPY --from=stage1 /usr/lib/python3 /usr/lib/python3
COPY --from=stage1 /etc/python3.8 /etc/python3.8
COPY --from=stage1 /etc/python3 /etc/python3
COPY --from=stage1 /usr/local/lib/python3.8 /usr/local/lib/python3.8
COPY --from=stage1 /usr/include/python3.8 /usr/include/python3.8
COPY --from=stage1 /usr/share/python3 /usr/share/python3
COPY --from=stage1 /usr/bin/pip3 /usr/bin/pip3
COPY --from=stage1 /usr/lib/python3/dist-packages /usr/lib/python3/dist-packages

COPY data.json ./data.json
COPY server.py ./server.py
COPY clientnew.py ./clientnew.py


CMD ["sleep"]
