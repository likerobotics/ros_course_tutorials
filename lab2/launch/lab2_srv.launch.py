from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='lab2',
            executable='lab2_srv_server.py',
            name='lab2_srv_server',
            output='screen'
        ),

        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim_node',
            output='screen'
        ),
    ])
