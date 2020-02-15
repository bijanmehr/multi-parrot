#!/usr/bin/env python
import serial
import os
import rospy
from time import sleep
from std_msgs.msg import String

def SerialCommandGet ( command ) :
   # os.popen("sudo adduser qazal dialout") if you were getting errors like can't access port or Serial not found
   port = SerialPortDetect()
   ser = serial.Serial(port,115200)
   while port is not None:
      if (ser.read()) :
         data = ser.readline()
         print(data)
      try :
         # command = str(raw_input("enter the command \n"))
         if (command.data != 'stop') :
            ser.write('c'+command.data)
            sleep(0.5)
         else :
            break
      except :
         print ("sth wrong")
   ser.close()



def SerialPortDetect () :
   try :
      stream = os.popen('ls /dev/ttyUSB*')
      output = stream.read()
      port = output.split("\n")
      port = port[0]
      return port
   except :
      print ('no port detected')


def callback (data) :
    SerialCommandGet(data)
    rospy.loginfo(rospy.get_caller_id()+"i sent : %s" , data.data)

def listener () :
   rospy.init_node("commute",anonymous=True)
   rospy.Subscriber("chatter",String,callback)
   rospy.spin()

if __name__ == '__main__' :
      listener()