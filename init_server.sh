#!/bin/bash

# Check if server is running
if [pgrep -f "climber.py" > /dev/null]; then
      echo "Server Running"
else
      echo "Starting Server"
fi
