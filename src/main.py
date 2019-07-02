#!/usr/bin/env python
# coding: UTF-8
import os
import subprocess

import rospy
import rospkg
from kobuki_msgs.msg import WheelDropEvent


def emergency_callback(message):
    print message.state
    if int(message.state) == 1:
        os.system('kill `ps aux | grep ros | awk \'{print $2}\'`')

    file = rospkg.RosPack().get_path('emergency_stop') + "/voice.wav"
    create_command = ["pico2wave", "-w=" + file, "All, processes, delete"]
    play_command = ["aplay", file]
    subprocess.call(create_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.call(play_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def main():
    rospy.init_node('emergency_node')
    rospy.Subscriber('/mobile_base/events/wheel_drop', WheelDropEvent, emergency_callback)
    rospy.spin()



if __name__ == '__main__':
    main()
