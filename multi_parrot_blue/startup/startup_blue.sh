#!/bin/bash

source /home/$(whoami)/Desktop/ROS_param.sh

gnome-terminal -e "bash -c \"roslaunch multi_parrot_blue main.launch; exec bash\""
