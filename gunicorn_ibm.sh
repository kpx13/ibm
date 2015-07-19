#!/bin/bash
export LANG=ru_RU.UTF-8
set -e
LOGFILE=/home/ibm/Django/ibm/logs/init.log
ERRFILE=/home/ibm/Django/ibm/logs/django-error.log
SOCKFILE=unix:/home/ibm/Django/ibm/gaspiko_ru.sock
NUM_WORKERS=$(grep -c '^processor' /proc/cpuinfo | awk '{ print 1+$1*2}')
NUM_WORKERS=4
USER=ibm
GROUP=ibm 
BIND=127.0.0.1:9999
cd /home/ibm/Django/ibm
source ../env/bin/activate
exec ../env/bin/gunicorn_django --error-logfile=$ERRFILE --timeout 10000 -w $NUM_WORKERS --user=$USER --group=$GROUP --log-level=info --log-file=$LOGFILE --bind=$BIND 2>>$LOGFILE.err

