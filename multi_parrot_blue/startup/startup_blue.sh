#!/bin/bash
# sleep 10
source $(rospack find multi_parrot_blue)/startup/ROS_param.sh

roslaunch multi_parrot_blue blue_parrot.launch
