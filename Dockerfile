FROM python:3.5.2-alpine
MAINTAINER Jay Thomas <jay@gfax.ch>

RUN pip install pylint

## App setup
RUN mkdir /usr/app
WORKDIR /usr/app
COPY . /usr/app
