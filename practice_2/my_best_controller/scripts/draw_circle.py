#!/usr/bin/env python3

import rospy

from geometry_msgs.msg import Twist # geometry_msgs must be in package.xml also!!!

if __name__ == '__main__':
    rospy.init_node("draw_circle")
    rospy.loginfo("Node started...")
    rate = rospy.Rate(2)

    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    msg = Twist()
    while not rospy.is_shutdown():
        #publish cmd vel
        
        msg.linear.x = 3.1
        msg.angular.z = 1.2
        pub.publish(msg)
        rospy.loginfo("CMD upd...")
        rate.sleep()