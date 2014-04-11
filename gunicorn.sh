#!/bin/bash
# This script starts the gunicorn process which runs the website

BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Kill bash if any processes fail
set -e

# Setup the local bash environment, and start the virtualenv
source "$BASE_DIR/env.sh"

# Get the base project directory and cd into it
#BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$BASE_DIR"

# Settings
LOG_DIR="$BASE_DIR/log"
LOG_FILE="$LOG_DIR/gunicorn.log"

# Activate virtual environment
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
test -d $LOG_DIR || mkdir -p $LOG_DIR

# Start the Gunicorn
echo "Starting Gunicorn: $GUNICORN_PROCESS_NAME (as user $GUNICORN_USER)"
exec env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application\
    --name $GUNICORN_PROCESS_NAME   \
    --workers=$GUNICORN_WORKERS     \
    --user=$GUNICORN_USER           \
    --group=$GUNICORN_GROUP         \
    --log-file=$LOG_FILE            \
    --log-level=$GUNICORN_LOG_LEVEL \
    --bind=127.0.0.1:$GUNICORN_PORT
