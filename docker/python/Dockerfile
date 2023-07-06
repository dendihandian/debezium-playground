FROM python:3.9.16-alpine3.17

COPY ./src /python/src

RUN pip install pymysql

WORKDIR /python/src
RUN touch /python/service.log
CMD tail -f /python/service.log