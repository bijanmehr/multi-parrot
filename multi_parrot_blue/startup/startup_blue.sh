#!/bin/bash

source $(rospack find multi_parrot_blue)/startup/ROS_param.sh

gnome-terminal -e "bash -c \"roslaunch multi_parrot_blue main.launch; exec bash\""
