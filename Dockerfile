FROM debian:latest
RUN apt update && apt upgrade -y
RUN apt-get -y install git
RUN git clone https://github.com/desinobita/Mark-40
RUN apt install python3-pip -y
RUN apt install ffmpeg -y
RUN pip3 install pyrogram
RUN pip3 install tgcrypto
RUN pip3 install python-dotenv[cli]
RUN pip3 install python-dotenv
RUN pip3 install gitpython
RUN pip3 install psutil
RUN pip3 install py-cpuinfo 
RUN pip3 install telegraph
RUN pip3 install py-tgcalls
RUN pip3 install python-telegram-bot==13.10
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN cd Mark-40
RUN pip3 install --upgrade pip
CMD python3 -m Mark
