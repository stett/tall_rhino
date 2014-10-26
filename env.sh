#!/bin/bash
unalias -a cd
BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Base settings
echo "Setting base environment variables..."
export PROJECT_NAME="tall_rhino"
export DJANGO_WSGI_MODULE="tall_rhino.wsgi"
export PIP_REQUIREMENTS_FILE="requirements.txt"

# Run environment variable overrides. If no local env
# script has been defined, create one now.
echo "Setting local environment variables..."
LOCAL_ENV="$BASE_DIR/local.sh"
touch "$LOCAL_ENV"
source "$LOCAL_ENV"

# Start up the 
echo "Starting up virtualenv..."
source "$BASE_DIR/env/bin/activate"
