FROM python:3.8
ENV PYTHONUNBUFFERED 1
ADD . /code/
WORKDIR /code
RUN apt-get update && apt-get install -y gettext libgettextpo-dev
RUN pip install -r requirements.txt