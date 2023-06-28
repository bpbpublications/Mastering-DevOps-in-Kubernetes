FROM alpine

LABEL description="This is a test Dockerfile."

RUN apk add --update nodejs npm
RUN npm install -g http-server

COPY . /src
WORKDIR /src

EXPOSE 80
ENTRYPOINT ["http-server", "-p", "8080"]

