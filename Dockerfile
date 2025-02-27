FROM ubuntu:latest
LABEL authors="sebastien"

ENTRYPOINT ["top", "-b"]