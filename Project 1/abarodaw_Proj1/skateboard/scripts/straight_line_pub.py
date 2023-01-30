#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def pub():
    rospy.init_node('straight_line_pub')
    move_forward1 = rospy.Publisher('/skateboard/rear_motor_left/command', Float64, queue_size=10)
    move_forward2 = rospy.Publisher('/skateboard/rear_motor_right/command', Float64, queue_size=10)
    move_left_castor = rospy.Publisher('/skateboard/left_castor_motor/command', Float64, queue_size=10)
    move_right_castor = rospy.Publisher('/skateboard/right_castor_motor/command', Float64, queue_size=10)
    rate = rospy.Rate(1)
    for i in range(15):
        move_left_castor.publish(0)
        move_right_castor.publish(0)
        move_forward1.publish(2.0)
        move_forward2.publish(2.0)
        print("Publishing velocity - 2")
        rate.sleep()
    
    move_forward1.publish(0.0)
    move_forward2.publish(0.0)
    print("Stopped")

if __name__ == '__main__':
    try:
        pub()
    except rospy.ROSInterruptException:
        pass