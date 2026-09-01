#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from lab2.srv import SetVelocity

class TurtleVelocityServer(Node):
    def __init__(self):
        super().__init__('turtle_velocity_service_server')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.srv = self.create_service(SetVelocity, 'set_turtle_velocity', self.set_velocity_callback)
        self.get_logger().info('Turtle velocity service server is ready.')

    def set_velocity_callback(self, request, response):
        twist = Twist()
        twist.linear.x = request.linear
        twist.angular.z = request.angular
        self.publisher.publish(twist)
        self.get_logger().info(f"Published velocity - Linear: {request.linear}, Angular: {request.angular}")
        response.success = True
        return response

if __name__ == '__main__':
    rclpy.init()
    node = TurtleVelocityServer()
    rclpy.spin(node)
    rclpy.shutdown()
