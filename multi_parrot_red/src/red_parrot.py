#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import serial
from multi_parrot_red.srv import *
import serial.tools.list_ports
import time

def parrot_client(command):
    rospy.wait_for_service('red_serial_handler/redparrot')
    try:
        parrot_connection = rospy.ServiceProxy('red_serial_handler/redparrot', RedParrot)
        result = parrot_connection(command)
        return result.result
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e




def full_turn():
    parrot_client("45")
    time.sleep(0.7)
    parrot_client("0")

def movment(data):
    parrot_client(data.data)

def audio_movement(data):
    full_turn()

def parrot_handler():
    rospy.init_node('red_parrot', log_level=rospy.DEBUG)
    rospy.Subscriber("/parrot/0/parrot_commands", String, movment, queue_size=10)
    rospy.Subscriber("/parrot/0/audio_player", String, audio_movement, queue_size=10)
    rospy.spin()

if __name__ == "__main__":
    parrot_handler()
