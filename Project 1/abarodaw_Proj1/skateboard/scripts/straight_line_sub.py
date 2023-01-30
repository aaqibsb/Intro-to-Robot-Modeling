#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def callback1(data):
    print("Received velocity for rear left motor - ", data.data)

def callback2(data):
    print("Received velocity for rear right motor - ", data.data)
    print("------------------------------------------------------------------------")

def sub():
    rospy.init_node('straight_line_sub')
    sub1 = rospy.Subscriber("/skateboard/rear_motor_left/command", Float64, callback1, queue_size=10)
    sub2 = rospy.Subscriber("/skateboard/rear_motor_right/command", Float64, callback2, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    try:
        sub()
    except rospy.ROSInterruptException:
        pass