#!/bin/bash -e

if [ -f .venv/bin/activate ]; then
    echo "Loading Python virtual environment from '.venv/bin/activate'"
    source .venv/bin/activate
fi
exec "$0"