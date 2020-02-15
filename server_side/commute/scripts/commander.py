#!/usr/bin/env python
import rospy
from std_msgs.msg import  String

def commander() :
    pub = rospy.Publisher("chatter",String,queue_size=10)
    rospy.init_node("commander",anonymous=False)
    rate = rospy.Rate(7)
    while not rospy.is_shutdown() :
        command = raw_input("enter the command\n")
        # rospy.loginfo(command)
        pub.publish(command)
        rate.sleep()

if __name__ == "__main__" : 
    try : 
        commander()
    except rospy.ROSInterruptException() :
        rospy.loginfo("interupt exception")
        pass