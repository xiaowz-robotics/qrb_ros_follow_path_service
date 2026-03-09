# Copyright (c) 2026 Qualcomm Innovation Center, Inc. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause-Clear

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():
    scan_topic_arg = DeclareLaunchArgument(
        'scan_topic',
        default_value='scan_filtered',
        description='LaserScan input topic'
    )

    qti_navigation_node = Node(
        package='qrb_ros_follow_path',
        executable='qrb_ros_follow_path',
        output='screen',
        emulate_tty=True,
        remappings=[
            ('scan', LaunchConfiguration('scan_topic')),
        ],
    )

    return LaunchDescription([
        scan_topic_arg,
        qti_navigation_node
    ])

