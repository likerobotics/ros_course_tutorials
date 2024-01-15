#!/usr/bin/env python3

import time

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class SimpleController():

    def __init__(self):
        rospy.init_node('simple_controller', anonymous=True)
        rospy.on_shutdown(self.shutdown)

        self.cmd_vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
        subscriber = rospy.Subscriber("/turtle1/pose", Pose, self.pose_callback)
        subscriber_target = rospy.Subscriber("/targets_topic", Pose, self.target_callback)
        self.rate = rospy.Rate(30)

        self.target_x = 0
        self.target_y = 0

        self.x = 0
        self.y = 0
    
    def target_callback(self, msg:Pose):
        rospy.loginfo("target updared with: {0} {1}".format(msg.x, msg.y))
        self.target_x, self.target_y =  msg.x, msg.y

    def pose_callback(self, msg:Pose):
        # rospy.loginfo("cur pose: {0} {1}".format(msg.x, msg.y))
        self.update_control(msg.x, msg.y)

    def update_control(self, x, y):
        self.x, self.y = x, y

    def spin(self):
        while not rospy.is_shutdown():
            twist_msg = Twist()
            diff = self.x - self.target_x
            if diff > 0.1:
                twist_msg.linear.x  = -0.5
            elif self.x - self.target_x < -0.1:
                twist_msg.linear.x  = 0.5
            else:
                twist_msg.linear.x  = 0.0
            self.cmd_vel_pub.publish(twist_msg)
            self.rate.sleep()

    def shutdown(self):
        self.cmd_vel_pub.publish(Twist())
        rospy.sleep(1)


simple_mover = SimpleController()
simple_mover.spin()