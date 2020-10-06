#!/usr/bin/env python
import rospy
import serial
import time
from multi_parrot_blue.srv import *
from std_msgs.msg import String



def parrot_queue_handler():
    global parrot_funcs , parrot_funcs_params ,parrot_funcs_delay
    try:
        if parrot_funcs:
            rospy.logerr(parrot_funcs)
            if parrot_funcs_delay[0] != -1:
                time.sleep(parrot_funcs_delay[0])

            if parrot_funcs_params[0] != -1:
                parrot_funcs[0](parrot_funcs_params[0])
            else:
                parrot_funcs[0]()

            parrot_funcs.pop(0)
            parrot_funcs_params.pop(0)
            parrot_funcs_delay.pop(0)

    except Exception as e :
        rospy.logerr('error in parrot_queue_handler ! : %s'%e)
        # print('error in parrot_queue_handler !',e)



def parrot_client(command):
    rospy.wait_for_service('serial_handler/parrot')
    try:
        parrot_connection = rospy.ServiceProxy('serial_handler/blueparrot', BlueParrot)
        result = parrot_connection(command)
        return result.result
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def dance(number = 1):
    res = parrot_client('G1 S%d'%number)
    if(res.find("DONE") != 1):
        print ("done")
    else:
        print("not done")

def blink(pwm = 180):
    res = parrot_client('G2 S%d'%pwm)
    if(res.find("DONE") != 1):
        print ("done")
    else:
        print("not done")

def mouth(pwm = 0): # open and close the mouth 255 -> open mouth      0 -> close mouth
    res = parrot_client('G3 S%d'%pwm)
    if(res.find("DONE") != 1):
        print ("done")
    else:
        print("not done")

def open_eye(pwm = 130):
    res = parrot_client('G4 S%d'%pwm)
    if(res.find("DONE") != 1):
        print ("done")
    else:
        print("not done")

def close_eye(pwm = 105):
    res = parrot_client('G5 S%d'%pwm)
    if(res.find("DONE") != 1):
        print ("done")
    else:
        print("not done")


def talk():
    pop_all_parrot_funcs()
    append_to_parrot_funcs(mouth,240)
    append_to_parrot_funcs(mouth,0,0.5)
    append_to_parrot_funcs(mouth,240,0.5)
    append_to_parrot_funcs(mouth,0,0.5)



parrot_funcs = []
parrot_funcs_params = []
parrot_funcs_delay = []

def append_to_parrot_funcs(functions,param = -1,delay = -1):
    global parrot_funcs , parrot_funcs_params ,parrot_funcs_delay
    parrot_funcs.append(functions)
    parrot_funcs_params.append(param)
    parrot_funcs_delay.append(delay)

def pop_all_parrot_funcs():
    global parrot_funcs , parrot_funcs_params ,parrot_funcs_delay
    parrot_funcs = []
    parrot_funcs_params = []
    parrot_funcs_delay = []



def parrot_commands(data):
    if(int(data.data) == 0 ):   # dance
        append_to_parrot_funcs(dance)
    elif(int(data.data) == 1 ):  # blink
        append_to_parrot_funcs(blink)
    elif(int(data.data) == 2 ): # open mouth
        append_to_parrot_funcs(mouth,240)
    elif(int(data.data) == 3 ): # close mouth
        append_to_parrot_funcs(mouth,0)
    elif(int(data.data) == 4 ): # open eye
        append_to_parrot_funcs(open_eye)
    elif(int(data.data) == 5 ): # close eye
        append_to_parrot_funcs(close_eye)
    elif(int(data.data) == 6): # open and close mouth
        append_to_parrot_funcs(mouth,240)
        append_to_parrot_funcs(mouth,0,0.5)
        append_to_parrot_funcs(mouth,240,0.5)
        append_to_parrot_funcs(mouth,0,0.5)

    
def parrot_voice_commands(data):
    text = data.data
    if text.find("shutup") == -1:
        talk()


def ros_init():
    rospy.init_node('parrot', log_level=rospy.DEBUG)
    rospy.Subscriber('web/blue_parrot_commands', String, parrot_commands, queue_size=10)
    rospy.Subscriber("web/blue_parrot_voice_commands", String, parrot_voice_commands, queue_size=10)
    rospy.spin()


if __name__ == "__main__":
    parrot_queue_handler()
    ros_init()
