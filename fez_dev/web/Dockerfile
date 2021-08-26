FROM centos:centos8.3.2011

ARG DEVELOPER_UID

RUN curl -L -O https://nginx.org/packages/centos/8/x86_64/RPMS/nginx-1.20.1-1.el8.ngx.x86_64.rpm

RUN rpm -ivh nginx-1.20.1-1.el8.ngx.x86_64.rpm

RUN useradd -u $DEVELOPER_UID fez

RUN usermod -u $DEVELOPER_UID fez
RUN groupmod -g $DEVELOPER_UID fez

COPY ./uwsgi_params /etc/nginx/uwsgi_params

RUN dnf -y module list nodejs
RUN dnf -y module reset nodejs
RUN dnf -y module enable nodejs:14
RUN dnf module -y install nodejs:14
WORKDIR /home/fez/
ADD ./nuxt /home/fez/

RUN chown -R fez:fez /home/fez/

COPY entrypoint.sh /root/entrypoint.sh
RUN chmod 777 /root/entrypoint.sh

EXPOSE 5000

# COPY ./error_log/error.log /var/log/nginx/error.log

ENTRYPOINT ["/root/entrypoint.sh"]
