FROM  ubuntu:18.04

RUN apt-get update && apt-get -y install python3.6  curl python3-pip vim

WORKDIR /app
RUN python3 --version
# install pip
RUN pip3 install --upgrade pip
COPY requirements.txt /app
RUN pip3 install --no-cache-dir  -r requirements.txt
COPY . /app
CMD /usr/local/bin/gunicorn -c gunicorn_config.py manage:app
