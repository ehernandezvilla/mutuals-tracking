#!/bin/bash

# Navigate to the directory containing your .env file
cd /home

# Path to your virtual environment's Python interpreter
VENV_PATH="/home/myenv/bin/python"

# Run your Docker container
docker run -p 80:8000 --env-file .env registry.digitalocean.com/bakslash/mu>exit_code=$?

# Check the exit code to determine success or failure
if [ $exit_code -ne 0 ]; then
    # If Docker run failed, notify failure
    $VENV_PATH /home/send_email.py notify_failure
else
    # If Docker run succeeded, notify success
    $VENV_PATH /home/send_email.py notify_success
fi