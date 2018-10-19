from ubuntu:14.04

# RUN apt-get install -y cron
WORKDIR /ime
COPY ./ /ime

ENTRYPOINT ["cron", "-f"]
