#!/bin/bash
# npm run build
# ssh root@120.78.177.9 "mkdir /usr/local/nginx/time-record"

## old
# scp -r ./pm2.json root@120.78.177.9:/usr/local/nginx/yunser-kq/
scp -r ./index.py root@120.78.177.9:/usr/local/nginx/yunser-python


ssh root@120.78.177.9 << remotessh
pkill -f -9 uwsgi
uwsgi --ini /root/python/config.ini
exit
remotessh 