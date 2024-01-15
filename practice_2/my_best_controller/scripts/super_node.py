#!/usr/bin/env python3

import rospy

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist 

#May attention!!! # geometry_msgs and turtlesim must be in package.xml also!!!

def pose_callback(pose):
    # THIS IS NOT RECOMMENDED WAY TO IMPLEMENT CONTROL !!!!!
    cmd = Twist()
    if pose.x > 9.0 or pose.x < 1.0:
        cmd.linear.x = 0.5
        cmd.angular.z = 2.0
    else:
        cmd.linear.x = 2.0
        cmd.angular.z = 0.0
    publisher.publish(cmd)
    #rospy.loginfo('('+ str(msg.x) + ", " + str(msg.y) + ")")

if __name__ == '__main__':
    rospy.init_node("turtle_super_node")
    rospy.loginfo("Node started...")
    # rate = rospy.Rate(2)
    subscriber = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
    publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rospy.spin()