cmake_minimum_required(VERSION 2.8.3)
project(commute)
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)
  add_message_files(
   FILES
   S_message.msg
)
 generate_messages(
   DEPENDENCIES
   std_msgs
 )
catkin_package(
  INCLUDE_DIRS include
  LIBRARIES commute
  CATKIN_DEPENDS roscpp rospy std_msgs message_runtime
  DEPENDS system_lib
)