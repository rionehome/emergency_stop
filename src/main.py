#!/usr/bin/env python
# coding: UTF-8
import os
import subprocess

import rospy
from kobuki_msgs.msg import WheelDropEvent


def emergency_callback(message):
	print message.state
	if int(message.state) == 1:
		p2=subprocess.Popen(['rosnode','list'], stdout=subprocess.PIPE)
		p2.wait()
		nodelist=p2.communicate()
		#print nodelist
		nd=nodelist[0]
		nd=nd.split("\n")
		print nd
		for i in range(len(nd)):
			subprocess.call(['rosnode','kill',nd[i]]) 
		


def main():
	rospy.init_node('emergency_node')
	rospy.Subscriber('/mobile_base/events/wheel_drop', WheelDropEvent, emergency_callback)
	rospy.spin()


if __name__ == '__main__':
	main()
