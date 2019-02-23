FROM python:3.7-alpine

RUN apk update && \
    apk add --virtual build-deps gcc musl-dev && \
    apk add postgresql-dev && \
    rm -rf /var/cache/apk/*

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# delete dependencies required to install certain python packages 
# so the docker image size is low enough for Zeit now
RUN apk del build-deps gcc musl-dev  

RUN mkdir /app
WORKDIR /app
COPY . /app
               
ENV FLASK_CONFIG="production"
ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:5000", "--log-level", "INFO", "run:app" ]

EXPOSE 5000