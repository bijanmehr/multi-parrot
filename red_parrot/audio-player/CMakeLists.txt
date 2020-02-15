cmake_minimum_required(VERSION 2.8.3)
project(audio_player)
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)
  add_message_files(
   FILES
   audio.msg
)
 generate_messages(
   DEPENDENCIES
   std_msgs
 )
catkin_package(
  INCLUDE_DIRS include
  LIBRARIES audio_player
  CATKIN_DEPENDS rospy std_msgs message_runtime
  DEPENDS system_lib
)