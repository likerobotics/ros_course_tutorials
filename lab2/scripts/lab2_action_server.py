#!/usr/bin/env python3

import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from rclpy.action import ActionServer
from lab2.action import GoToPose

class TurtlePoseActionServer(Node):
    def __init__(self):
        super().__init__('turtle_pose_action_server')

        self.pose = None
        self.goal_handle = None
        self.goal_x = None
        self.goal_y = None

        self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose_sub = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)

        self._action_server = ActionServer(
            self,
            GoToPose,
            'go_to_pose',
            execute_callback=self.execute_callback
        )

        self.timer = self.create_timer(0.1, self.timer_callback)

    def pose_callback(self, msg):
        self.pose = msg

    def execute_callback(self, goal_handle):
        self.get_logger().info(f"Received goal: x={goal_handle.request.x}, y={goal_handle.request.y}")

        self.goal_handle = goal_handle
        self.goal_x = goal_handle.request.x
        self.goal_y = goal_handle.request.y

        while not goal_handle.is_cancel_requested and self.goal_handle is not None:
            rclpy.spin_once(self, timeout_sec=0.1)

        if self.goal_handle is None:
            goal_handle.succeed()
            result = GoToPose.Result()
            result.success = True
            return result
        else:
            goal_handle.abort()
            result = GoToPose.Result()
            result.success = False
            return result

    def timer_callback(self):
        if self.pose is None or self.goal_handle is None:
            return

        dx = self.goal_x - self.pose.x
        dy = self.goal_y - self.pose.y
        distance = math.sqrt(dx**2 + dy**2)

        feedback = GoToPose.Feedback()
        feedback.distance_remaining = distance
        self.goal_handle.publish_feedback(feedback)

        if distance < 0.05:
            self.cmd_pub.publish(Twist())
            self.goal_handle = None
            return

        twist = Twist()
        twist.linear.x = dx
        twist.linear.y = dy
        self.cmd_pub.publish(twist)

if __name__ == '__main__':
    rclpy.init()
    node = TurtlePoseActionServer()
    rclpy.spin(node)
    rclpy.shutdown()
