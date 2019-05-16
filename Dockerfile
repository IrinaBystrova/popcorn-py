FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=popcorn_site.settings
RUN mkdir /project
WORKDIR /project
COPY . /project
RUN pip install pipenv && pipenv install --system
