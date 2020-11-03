#!/bin/bash

source $(rospack find multi_parrot_red)/startup/ROS_param.sh

gnome-terminal -e "bash -c \"roslaunch multi_parrot_red main.launch; exec bash\""
