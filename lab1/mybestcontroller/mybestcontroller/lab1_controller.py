"""Controller entry point for laboratory work 1."""

import rclpy
from rclpy.node import Node


class Lab1Controller(Node):
    """Backbone for the student controller implementation."""

    def __init__(self):
        super().__init__('lab1_controller')
        # TODO(student): implement namespace-dependent controller behavior.


def main(args=None):
    """Run the laboratory controller node."""
    rclpy.init(args=args)
    node = Lab1Controller()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

