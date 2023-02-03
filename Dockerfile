FROM debian:latest

RUN apt update && apt upgrade -y
RUN apt install python3-pip -y
RUN apt install ffmpeg -y

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs

RUN pip3 install --upgrade pip
RUN pip3 install -U -r requirement.txt
CMD python3 -m Mark
