#!/bin/bash
# dev.sh

# Activate poetry environment and run flask
cd app && poetry run flask run --port 3000 --debug