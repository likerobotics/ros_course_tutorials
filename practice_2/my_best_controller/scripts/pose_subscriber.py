#!/usr/bin/env python3

import rospy

from turtlesim.msg import Pose
#from geometry_msgs.msg import Twist # geometry_msgs must be in package.xml also!!!

def pose_callback(msg):
    rospy.loginfo('('+ str(msg.x) + ", " + str(msg.y) + ")")

if __name__ == '__main__':
    rospy.init_node("turtle_pose_subscr")
    rospy.loginfo("Node started...")
    # rate = rospy.Rate(2)
    subscriber = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
    
    # while not rospy.is_shutdown():
    #     #publish cmd vel
        
    #     msg.linear.x = 3.1
    #     msg.angular.z = 1.2
    #     pub.publish(msg)
    #     rospy.loginfo("CMD upd...")
    #     rate.sleep()
    rospy.spin()