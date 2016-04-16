#!/bin/bash

# Check if server is running
if [ `pgrep -f climber.py` ]; then
      echo "Server Running"
else
      echo "Starting Server"
      cmd="python ./climber.py"
      $cmd &
fi
