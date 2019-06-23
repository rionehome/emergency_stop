#!/usr/bin/env python
# coding: UTF-8
import os
import subprocess

import rospy
from kobuki_msgs.msg import WheelDropEvent


def emergency_callback(message):
    print message.state
    if int(message.state) == 1:
        os.system('kill `ps aux | grep ros | awk \'{print $2}\'`')

def main():
    rospy.init_node('emergency_node')
    rospy.Subscriber('/mobile_base/events/wheel_drop', WheelDropEvent, emergency_callback)
    rospy.spin()


if __name__ == '__main__':
    main()
