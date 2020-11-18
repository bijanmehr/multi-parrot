#!/bin/sh

export ROS_IP=192.168.0.102
export ROS_MASTER_URI=http://192.168.0.104:11311
export ROSLAUNCH_SSH_UNKNOWN=1
. /home/pi/catkin_ws/devel/setup.sh
exec "$@"
