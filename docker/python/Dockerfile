FROM python:3.10.12-alpine3.18

COPY ./src /python/src

RUN pip install cryptography pymysql Faker

WORKDIR /python/src
RUN touch /python/service.log
CMD tail -f /python/service.log