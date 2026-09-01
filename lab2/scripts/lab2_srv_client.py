#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from  lab2.srv import SetVelocity 

class TurtleVelocityClient(Node):
    def __init__(self):
        super().__init__('turtle_velocity_service_client')
        self.client = self.create_client(SetVelocity, 'set_turtle_velocity')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')
        self.send_request(2.0, 1.0)

    def send_request(self, linear, angular):
        request = SetVelocity.Request()
        request.linear = linear
        request.angular = angular
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None and future.result().success:
            self.get_logger().info('Velocity set successfully!')
        else:
            self.get_logger().error('Failed to set velocity.')

if __name__ == '__main__':
    rclpy.init()
    client = TurtleVelocityClient()
    rclpy.shutdown()
