#!/bin/sh

export ROS_IP=192.168.0.105
export ROS_MASTER_URI=http://192.168.0.104:11311
export ROSLAUNCH_SSH_UNKNOWN=1
. /home/lenovo/catkin_ws/devel/setup.sh
exec "$@"
