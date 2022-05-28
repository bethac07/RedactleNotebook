FROM ubuntu:20.04

RUN apt-get update
RUN apt-get -y remove pandoc
RUN apt-get -y autoremove
RUN apt-get -y clean
RUN apt-get -y install git
RUN apt-get -y autoremove
RUN apt-get -y clean
RUN apt-get -y install python3-pip
RUN apt-get -y autoremove
RUN apt-get -y clean
RUN apt-get -y install wget
RUN apt-get -y autoremove
RUN apt-get -y clean

RUN wget https://github.com/jgm/pandoc/releases/download/2.18/pandoc-2.18-1-amd64.deb
RUN dpkg -i  pandoc-2.18-1-amd64.deb

RUN git clone https://github.com/bethac07/redactle-notebook.git
RUN pip3 install -r redactle-notebook/requirements.txt
