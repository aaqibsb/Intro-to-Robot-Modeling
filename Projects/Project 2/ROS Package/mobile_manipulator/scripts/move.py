#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
import time

rospy.init_node('arm_control')
link_1 = rospy.Publisher('/mobile_manipulator/first_link_motor/command', Float64, queue_size=10)
link_2 = rospy.Publisher('/mobile_manipulator/second_link_motor/command', Float64, queue_size=10)
link_3 = rospy.Publisher('/mobile_manipulator/third_link_motor/command', Float64, queue_size=10)
link_4 = rospy.Publisher('/mobile_manipulator/fourth_link_motor/command', Float64, queue_size=10)
link_5 = rospy.Publisher('/mobile_manipulator/fifth_link_motor/command', Float64, queue_size=10)
link_6 = rospy.Publisher('/mobile_manipulator/sixth_link_motor/command', Float64, queue_size=10)

move1 = rospy.Publisher('/mobile_manipulator/rear_motor_right/command', Float64, queue_size=10)
move2 = rospy.Publisher('/mobile_manipulator/rear_motor_left/command', Float64, queue_size=10)
right = rospy.Publisher('/mobile_manipulator/right_castor_motor/command', Float64, queue_size=10)
left = rospy.Publisher('/mobile_manipulator/left_castor_motor/command', Float64, queue_size=10)

def arm_pose(theta1, theta2, theta3, theta4, theta5, theta6):
    print("Arm velocity received")
    link_1.publish(theta1)
    link_2.publish(theta2)
    link_3.publish(theta3)
    link_4.publish(theta4)
    link_5.publish(theta5)
    link_6.publish(theta6)

def platform():
    rate = rospy.Rate(10)
    print("Received velocity")
    for i in range(50):
        move1.publish(1)
        move2.publish(1)
        right.publish(0.0)
        left.publish(0.0)
        rate.sleep()
    print("End velocity") 
    move1.publish(0.0)
    move2.publish(0.0)
    right.publish(0.0)
    left.publish(0.0)    

def platform_1():
    rate = rospy.Rate(10)
    print("Received velocity")
    for i in range(50):
        move1.publish(-1)
        move2.publish(-1)
        right.publish(0.0)
        left.publish(0.0)
        rate.sleep()
    print("End velocity") 
    move1.publish(0.0)
    move2.publish(0.0)
    right.publish(0.0)
    left.publish(0.0)   



platform()
time.sleep(2)
arm_pose(0.65,-0.1,0.05,0,-0.2,-4.71)
time.sleep(2)
arm_pose(0.5,-2,-0.5,0,-0.2,-6.28)
time.sleep(2)
arm_pose(0.65,-0.1,0.05,0,-0.2,-4.71)
time.sleep(2)
arm_pose(0.85,1.8,0.8,0,-0.2,-3.5)
time.sleep(2)
arm_pose(0.65,-0.1,0.05,0,-0.2,-4.71)
platform_1()
