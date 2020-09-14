FROM python:3.6-alpine
MAINTAINER Juan Suarez

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp_build_ps \
        gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev libjpeg-turbo-dev zlib-dev

#RUN apk add --update  zlibg-dev
#RUN apk install pillow
RUN pip install -r /requirements.txt
RUN apk del .tmp_build_ps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user