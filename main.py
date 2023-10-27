#!/usr/bin/env python3

#Garrett Bowman Senior Design Project
#UF ECE 2023

import sys

from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
#from interbotix_perception_modules.pointcloud import InterbotixPointCloudInterface
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
        gripper_name='gripper')
        
    #
    if (bot.arm.group_info.num_joints < 5):
        bot.core.get_logger().fatal('This script requires the robot to have at least 5 joints!')
        bot.shutdown()
        sys.exit()

    mode = input("Press 1, 2 or 3")

    while(1):
        #MODE 1
        if mode == 1:
            bot.arm.go_to_home_pose()




            mode = input("Press 1, 2 or 3")

        #MODE 2    
        elif mode == 2:
            bot.arm.go_to_home_pose()


            mode = input("Press 1, 2 or 3")


        #MODE 3
        elif mode == 3:
            bot.arm.go_to_home_pose()

            joint_positions = [-1.0, 0.5, 0.5, 0, -0.5, 1.57]


            mode = input("Press 1, 2 or 3")
        else:

            mode = input("Not a valid entry. Press 1, 2 or 3.")

            if mode != 1 | 2 | 3:

                print("Shutting down.")
                bot.arm.go_to_home_pose()
                bot.arm.go_to_sleep_pose()
                bot.shutdown()



if __name__ == '__main__':
    main()