#!/bin/sh

printf "%s\n" ".::Start API::."

cd /ag/api && . ./venv_api/bin/activate
gunicorn -b :5000 --access-logfile - --error-logfile - api:app
