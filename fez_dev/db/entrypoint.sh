#!/bin/bash

original_owner=$(stat --format=%u /var/lib/mysql)
original_group=$(stat --format=%g /var/lib/mysql)

source /root/settings.conf

if [ ! -e /var/lib/mysql/ibdata1 ] ; then
  [[ -e /etc/my.cnf ]] && mv -n /etc/my.cnf /etc/my.cnf.save
  rm -r /var/lib/mysql/*
  mysqld \
    --no-defaults \
    --initialize-insecure \
    --basedir=/usr \
    --datadir=/var/lib/mysql \
    --user=mysql
  chown -R mysql: /var/lib/mysql
  /usr/sbin/mysqld --user=mysql --daemonize
  mysql -e "CREATE USER root@'%'; GRANT ALL ON *.* TO root@'%' WITH GRANT OPTION; "
  mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql mysql
  mysql -e "CREATE DATABASE fezdb CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci; " 
  mysql -e "CREATE USER IF NOT EXISTS 'fez'@'%' IDENTIFIED BY '$FEZ_PW'; " 
  mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'fez'@'%'; " 
  mysql -e "FLUSH PRIVILEGES; " 
  mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED by '$DB_ROOT_PW'; " 
  mysqladmin shutdown

  [[ -e /etc/my.cnf.save ]] && mv /etc/my.cnf.save /etc/my.cnf
fi

chown -R mysql: /var/lib/mysql
/usr/sbin/mysqld --user=mysql "$@"

chown -R $original_owner:$original_group /var/lib/mysql