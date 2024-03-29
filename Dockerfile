FROM debian:latest

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN pip3 install -U pip
COPY . /app
WORKDIR /app
RUN pip3 install -U -r requirement.txt
CMD bash start
