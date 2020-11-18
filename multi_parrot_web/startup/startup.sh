#!/bin/bash

sleep 5

source /home/$(whoami)/Desktop/multi-parrot/multi_parrot_web/startup/ROS_param.sh

gnome-terminal -e "bash -c \"python3 /home/$(whoami)/Desktop/multi-parrot/multi_parrot_web/manage.py runserver 0.0.0.0:8000 --noreload ; exec bash\""

sleep 1

roslaunch main.launch