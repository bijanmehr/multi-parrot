#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import pygame
import time
import math



def play_sound(data):
    text = data.data
    if text.find("shutup") == -1:
        pygame.mixer.Sound.play(pygame.mixer.Sound(data.data))
    elif text.find("shutup") != -1:
        stop_sound()


def stop_sound():
    pygame.mixer.stop()



def ros_init():
    rospy.init_node('audio_player', log_level=rospy.DEBUG)
    rospy.Subscriber("audio_commands", String, play_sound, queue_size=10)


def pygame_init():
    pygame.mixer.init()
    if pygame.mixer.get_init() is None:
        print("mixer initialization is NOT successful")



if __name__ == "__main__":
    ros_init()
    pygame_init()
    rospy.spin()