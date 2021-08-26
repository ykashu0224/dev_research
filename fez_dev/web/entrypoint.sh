#!/bin/bash

# /usr/sbin/nginx -g 'daemon off;' -c /etc/nginx/nginx.conf
cd /home/fez/
npm install
/usr/sbin/nginx -g 'daemon off;' -c /etc/nginx/nginx.conf & npm run dev 
