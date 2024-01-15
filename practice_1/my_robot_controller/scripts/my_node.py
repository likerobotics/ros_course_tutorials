#!/usr/bin/env python3

import rospy


if __name__ == '__main__':
    rospy.init_node("test_node_1")
    rospy.loginfo("Node started...")
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("Hello...")
        rate.sleep()

    # rospy.logwarn("Hello world worn")
    # rospy.logerr("Hello world err")

