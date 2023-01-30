#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def pub():
    rospy.init_node('circle_pub')
    move_forward1 = rospy.Publisher('/skateboard/rear_motor_left/command', Float64, queue_size=10)
    move_forward2 = rospy.Publisher('/skateboard/rear_motor_right/command', Float64, queue_size=10)
    move_left_castor = rospy.Publisher('/skateboard/left_castor_motor/command', Float64, queue_size=10)
    move_right_castor = rospy.Publisher('/skateboard/right_castor_motor/command', Float64, queue_size=10)

    rate = rospy.Rate(1)
    for i in range(30):
        move_forward1.publish(5.0)
        move_forward2.publish(5.0)
        move_left_castor.publish(0.3)
        move_right_castor.publish(0.3)
        print("Publishing velocity - 5 ; position - 0.3")
        rate.sleep()
    
    move_forward1.publish(0.0)
    move_forward2.publish(0.0)
    print("Stopped")

if __name__ == '__main__':
    try:
        pub()
    except rospy.ROSInterruptException:
        pass