FROM golang:1.14-alpine AS build

WORKDIR /src/
COPY main.go go.* /src/
RUN CGO_ENABLED=0 go build -o /bin/goapp

FROM scratch
COPY --from=build /bin/goapp /bin/goapp
ENTRYPOINT ["/bin/goapp"]
