#!/bin/bash

source $(rospack find multi_parrot_web)/startup/ROS_param.sh

gnome-terminal -e "bash -c \"python3 $(rospack find multi_parrot_web)/manage.py runserver 0.0.0.0:8000 --noreload ; exec bash\""

sleep 2

roscore