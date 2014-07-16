#! /bin/sh

rm -rf local.virtualenv

virtualenv -p python2 local.virtualenv
./local.virtualenv/bin/pip install -r requirements.txt
mkdir -p local.persistent/logs 

