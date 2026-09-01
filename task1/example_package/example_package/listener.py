#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MinimalListener(Node):
    def __init__(self):
        super().__init__('minimal_listener')
        # Subscribe to the "chatter" topic with String messages
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.callback,
            10  # queue size
        )
        self.subscription  # prevent unused-variable warning

    def callback(self, msg: String):
        self.get_logger().info(f'I heard: "{msg.data}"')


def main():
    rclpy.init()
    node = MinimalListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
