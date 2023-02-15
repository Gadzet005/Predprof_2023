FROM python:3.9-alpine
RUN apk add --no-cache mariadb-connector-c-dev
RUN apk update && apk add python3 python3-dev mariadb-dev build-base netcat-openbsd
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN apk del python3-dev mariadb-dev build-base
COPY ./site /app
WORKDIR /app
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]