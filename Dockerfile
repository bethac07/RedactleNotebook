FROM ubuntu:20.04

RUN apt-get update
RUN apt-get -y upgrade pandoc
RUN apt-get -y install git python3-pip

RUN git clone https://github.com/bethac07/redactle-notebook.git
RUN pip3 install -r redactle-notebook/requirements.txt
