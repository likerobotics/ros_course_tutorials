#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from lab2.action import GoToPose

class TurtlePoseActionClient(Node):
    def __init__(self):
        super().__init__('turtle_pose_action_client')
        self.client = ActionClient(self, GoToPose, 'go_to_pose')

    def send_goal(self, x, y):
        self.client.wait_for_server()
        goal = GoToPose.Goal()
        goal.x = x
        goal.y = y
        self.get_logger().info(f"Sending goal to x={x}, y={y}")
        self._send_goal_future = self.client.send_goal_async(goal, feedback_callback=self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal rejected")
            return
        self.get_logger().info("Goal accepted")
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f"Distance remaining: {feedback.distance_remaining:.2f}")

    def get_result_callback(self, future):
        result = future.result().result
        if result.success:
            self.get_logger().info("Turtle reached the goal!")
        else:
            self.get_logger().info("Failed to reach goal")
        rclpy.shutdown()

if __name__ == '__main__':
    rclpy.init()
    client = TurtlePoseActionClient()
    client.send_goal(6.0, 4.0)
    rclpy.spin(client)