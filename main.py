#!/usr/bin/env python3

#Garrett Bowman Senior Design Project
#UF ECE 2023

import sys

from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
from interbotix_perception_modules.pointcloud import InterbotixPointCloudInterface
import numpy as np

"""
This script takes a tray containing a PCB, moves it under a scanning microscope, and then moves 
it to a different location.

To get started, open a terminal and type:

    ros2 launch interbotix_xsarm_control xsarm_control.launch.py robot_model:=vx300

Then change to this directory and type:

    python3 main.py
"""


def main():


    bot = InterbotixManipulatorXS(
        robot_model='vx300',
        group_name='arm',
        gripper_name='gripper'

    if (bot.arm.group_info.num_joints < 5):
        bot.core.get_logger().fatal('This script requires the robot to have at least 5 joints!')
        bot.shutdown()
        sys.exit()

    while(1):
        input

        




        joint_positions = [-1.0, 0.5, 0.5, 0, -0.5, 1.57]


        bot.arm.set_ee_pose_components(x=0.3, z=0.2)
        bot.arm.set_single_joint_position(joint_name='waist', position=np.pi/2.0)
        bot.gripper.release()
        bot.arm.set_ee_cartesian_trajectory(x=0.1, z=-0.16)
        bot.gripper.grasp()
        bot.arm.set_ee_cartesian_trajectory(x=-0.1, z=0.16)
        bot.arm.set_single_joint_position(joint_name='waist', position=-np.pi/2.0)
        bot.arm.set_ee_cartesian_trajectory(pitch=1.5)
        bot.arm.set_ee_cartesian_trajectory(pitch=-1.5)
        bot.arm.set_single_joint_position(joint_name='waist', position=np.pi/2.0)
        bot.arm.set_ee_cartesian_trajectory(x=0.1, z=-0.16)
        bot.gripper.release()
        bot.arm.set_ee_cartesian_trajectory(x=-0.1, z=0.16)
        bot.arm.go_to_home_pose()
        bot.arm.go_to_sleep_pose()

        bot.shutdown()


if __name__ == '__main__':
    main()