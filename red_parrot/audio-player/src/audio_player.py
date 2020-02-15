#!/usr/bin/env python
import pygame ,time ,rospy 
from std_msgs.msg import String
def audio_player (data) :
    rospy.loginfo("running node ")
    pygame.mixer.init()
    rospy.loginfo("pygame initialized")
    command = data.data.partition('play ') 
    if command[1] != 'play ' :
        print ("didnt found play")
        return -1
# sound_name = str(raw_input("enter the sound's name or stop \n") )
    try :
        pygame.mixer.music.load('/home/pi/Downloads/'+ command[2]+'.mp3')
    except :
        exit() 
    print ("playing "+ command[2])
    pygame.mixer.music.play(0)
    # time.sleep(10)
    while (pygame.mixer.get_busy()) :
        time.sleep(10) 
    print("finished playing audio")
    # sound_name = str(raw_input("enter the sound's name or stop \n") )

def init_node () :
    rospy.init_node('audio_player')
    rospy.Subscriber('chatter',String , audio_player)

if __name__ == '__main__' :
    init_node() 
    rospy.spin()