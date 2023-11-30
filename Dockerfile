FROM python:3.11.4
LABEL luis122448 <luis122448gmail.com>

WORKDIR /opt

COPY ./requirements.txt /opt/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /opt/requirements.txt

COPY ./app /opt/app/
COPY ./oracle_home /opt/oracle_home/
COPY ./install-instantclient.sh /opt/install-instantclient.sh

ENV LD_LIBRARY_PATH=/opt/oracle_home/instantclient

RUN /bin/bash -c "/opt/install-instantclient.sh"

RUN apt-get update && apt-get install -y libaio1

EXPOSE 8000
CMD [ "python", "app/server.py" ]