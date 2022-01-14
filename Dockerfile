FROM python:3

WORKDIR /code
RUN mkdir -p /postgres_data
#prevent python from creating pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#install psycopg2
RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean

# This section is borrowed from the official Django image but adds GDAL and others
RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin  python3-gdal python3-gdal


RUN pip install pip --upgrade pip

COPY ./product_seller/requirements.txt /code/
Run pip uninstall environ
RUN pip install psycopg2
RUN pip install pip --upgrade
RUN pip install --upgrade --no-cache-dir --src /usr/src -r requirements.txt
COPY ./product_seller /code/
