#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import serial
from multi_parrot_red.srv import *
import serial.tools.list_ports
import time

def parrot_client(command):
    rospy.wait_for_service('serial_handler/parrot')
    try:
        parrot_connection = rospy.ServiceProxy('serial_handler/redparrot', RedParrot)
        result = parrot_connection(command)
        return result.result
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e




def full_turn():
    parrot_client("180")
    time.sleep(0.7)
    parrot_client("0")

def movment(data):
    parrot_client(data.data)

def audio_movement(data):
    full_turn()

def parrot_handler():
    rospy.init_node('Red_parrot')
    rospy.Subscriber("red_parrot_movment", String, movment, queue_size=10)
    rospy.Subscriber("audio_commands", String, audio_movement, queue_size=10)
    rospy.spin()

if __name__ == "__main__":
    parrot_handler()