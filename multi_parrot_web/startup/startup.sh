#!/bin/bash

# sleep 5

# gnome-terminal -e  "roslaunch /home/$(whoami)/Desktop/multi-parrot/multi_parrot_web/startup/main.launch"

# sleep 5

# gnome-terminal -e "python3 /home/$(whoami)/Desktop/multi-parrot/multi_parrot_web/manage.py runserver 0.0.0.0:8000 --noreload "


# exec $SHELL


source /opt/ros/kinetic/setup.bash
source /home/$(whoami)/Desktop/multi-parrot/multi_parrot_web/startup/ROS_param.sh
# source /home/cabinet/catkin_ws/devel/setup.bash



gnome-terminal -e "python3 /home/$(whoami)/Desktop/multi-parrot/multi_parrot_web/manage.py runserver 0.0.0.0:8000 --noreload "

sleep 2

roslaunch /home/$(whoami)/Desktop/multi-parrot/multi_parrot_web/startup/main.launch

