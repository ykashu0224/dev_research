FROM centos:centos8.3.2011

RUN rpm -ivh https://dev.mysql.com/get/mysql80-community-release-el8-1.noarch.rpm

RUN dnf -y module disable mysql
RUN dnf -y install mysql-community-server

COPY ./conf/settings.conf /root/settings.conf

COPY entrypoint.sh /root/entrypoint.sh
RUN chmod 777 /root/entrypoint.sh

ENTRYPOINT ["/root/entrypoint.sh"]