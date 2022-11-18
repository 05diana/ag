#!/bin/sh

printf "%s\n" ".::Start API::."

cd /ag/api && . ./venv_api/bin/activate
gunicorn -w $API_WORKERS -u user -g nogroup -b 127.0.0.1:5000 --access-logfile - --error-logfile - api:app --daemon
haproxy -f /etc/haproxy/haproxy.cfg
