FROM centos:centos8.3.2011
ARG DEVELOPER_UID

RUN useradd -u $DEVELOPER_UID fez

RUN usermod -u $DEVELOPER_UID fez
RUN groupmod -g $DEVELOPER_UID fez

WORKDIR /tmp
RUN dnf -y groupinstall "Development Tools"
RUN dnf -y install openssl-devel libffi-devel bzip2-devel
RUN curl -O https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz
RUN tar xvf Python-3.9.5.tgz

WORKDIR /tmp/Python-3.9.5
RUN ./configure --enable-optimizations
RUN make altinstall

WORKDIR /home/fez

ADD requirements.txt /home/fez

RUN dnf -y install python3-devel
RUN dnf -y install mysql-devel

RUN pip3.9 install -r requirements.txt

ADD . /home/fez/

RUN chown -R fez:fez /home/fez/

CMD ["uwsgi", "--ini", "fez_uwsgi.ini"]
