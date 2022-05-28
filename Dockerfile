FROM ubuntu:20.04

RUN apt-get update
RUN apt-get -y install python3-pip
RUN apt-get -y install git
RUN apt-get -y install wget
RUN apt-get -y autoremove
RUN apt-get -y clean

RUN wget https://github.com/jgm/pandoc/releases/download/2.18/pandoc-2.18-1-amd64.deb
RUN dpkg -i  pandoc-2.18-1-amd64.deb

ARG NB_USER=redactler
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}

USER root
WORKDIR ${HOME}
RUN git clone https://github.com/bethac07/redactle-notebook.git
RUN pip3 install -r redactle-notebook/requirements.txt
RUN python3 -m pip install --no-cache-dir notebook jupyterlab

WORKDIR ${HOME}/redactle-notebook
COPY . ${HOME}
WORKDIR ${HOME}
RUN rm -rf redactle-notebook
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}

ENTRYPOINT [""]
CMD ["jupyter notebook --NotebookApp.default_url=/lab/ --ip=0.0.0.0 --port=8888"]
