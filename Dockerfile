FROM python:3.9

WORKDIR /usr/src/codraw

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/codraw
RUN pip install -r /usr/src/codraw/requirements.txt
