#!/usr/bin/env python3

#Garrett Bowman Senior Design Project
#UF ECE 2023

import sys

from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
#from interbotix_perception_modules.pointcloud import InterbotixPointCloudInterface
import numpy as np
import time

"""
This script takes a tray containing a PCB, moves it under a scanning microscope, and then moves 
it to a different location.

To get started, open a terminal and type:

    ros2 launch interbotix_xsarm_control xsarm_control.launch.py robot_model:=vx300

Then open another terminal, change to this directory and type:

    python3 main.py
"""
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():

    bot = InterbotixManipulatorXS(
        robot_model='vx300',
        group_name='arm',
        moving_time= 2.0,
        #accel_time= 0.3,
        gripper_name='gripper')
        
    #
    if (bot.arm.group_info.num_joints < 5):
        bot.core.get_logger().fatal('This script requires the robot to have at least 5 joints!')
        bot.shutdown()
        sys.exit()



    while(1):

        mode = input("Menu: 1)Pickup 1, 2)Dropoff 1, 3)Pickup 2, 4)Dropoff 2, or 5)SLEEP")

        #MODE 1 PICKUP 1
        if mode == '1':
            
            #start of the pickup, open gripper and proceed safely to location 1
            bot.arm.go_to_sleep_pose()
            bot.gripper.release()
            joint_positions = [-0.33, 0.44, 1.43, -1.83, 1.57]
            bot.arm.set_joint_positions(joint_positions)


            #slide under and grasp
            joint_positions = [-0.33, 0.44, 1.25, -1.70, 1.57]
            bot.arm.set_joint_positions(joint_positions)
            bot.gripper.grasp()
            time.sleep(3)


            #pick up and rotate
            bot.arm.set_ee_cartesian_trajectory(z=0.15)
            bot.arm.set_ee_cartesian_trajectory(x=-0.1)
            bot.arm.set_single_joint_position(joint_name='waist', position=1.28)


            #dropoff location
            bot.moving_time= 4.0
            joint_positions = [1.28, 0.104, 0.969, -1.04, 1.57]
            bot.arm.set_joint_positions(joint_positions)

            #communication with microscope

            #slide out
            bot.gripper.release()
            bot.moving_time= 2.0
            bot.arm.set_ee_cartesian_trajectory(x=-0.1)
            bot.arm.go_to_sleep_pose()


        #MODE 2 Dropoff at Location 1
        elif mode == '2':

            #start of the pickup, go to safe distance from microscope platform
            joint_positions = [1.28, -0.127, 1.32, -1.13, 1.57]
            bot.arm.set_joint_positions(joint_positions)


            #slide under, grasp, then lift up to avoid damage
            bot.arm.set_ee_cartesian_trajectory(x=0.1)
            bot.gripper.grasp()
            bot.arm.set_ee_cartesian_trajectory(z=0.05)
            bot.arm.set_ee_cartesian_trajectory(x=-0.1)
            bot.arm.set_ee_cartesian_trajectory(z=0.1)


            #rotate to position 1, place then release
            bot.arm.set_single_joint_position(joint_name='waist', position=-0.33)
            joint_positions = [-0.33, 0.44, 1.25, -1.70, 1.57]
            bot.arm.set_joint_positions(joint_positions)
            bot.gripper.release()


            #pull back then go sleep
            bot.arm.set_ee_cartesian_trajectory(x=-0.03)
            bot.arm.set_single_joint_position(joint_name='waist', position=0.0)
            bot.arm.go_to_sleep_pose()
            
            
        #MODE 3 PICKUP 2
        if mode == '3':

            #start of the pickup, open gripper and proceed safely to location 2
            bot.arm.go_to_sleep_pose()
            bot.gripper.release()
            joint_positions = [0.403, 0.44, 1.43, -1.83, 1.57]
            bot.arm.set_joint_positions(joint_positions)


            #slide under and grasp
            joint_positions = [0.403, 0.44, 1.25, -1.70, 1.57]
            bot.arm.set_joint_positions(joint_positions)
            bot.gripper.grasp()
            time.sleep(3)


            #pick up and rotate
            bot.arm.set_ee_cartesian_trajectory(z=0.15)
            bot.arm.set_ee_cartesian_trajectory(x=-0.1)
            bot.arm.set_single_joint_position(joint_name='waist', position=1.28)


            #dropoff location
            bot.moving_time= 4.0
            joint_positions = [1.28, 0.104, 0.969, -1.04, 1.57]
            bot.arm.set_joint_positions(joint_positions)

            #communication with microscope

            #slide out
            bot.gripper.release()
            bot.moving_time= 2.0
            bot.arm.set_ee_cartesian_trajectory(x=-0.1)
            bot.arm.go_to_sleep_pose()


        #MODE 4 Dropoff at Location 2
        elif mode == '4':

            #start of the pickup, go to safe distance from microscope platform
            joint_positions = [1.28, -0.127, 1.32, -1.13, 1.57]
            bot.arm.set_joint_positions(joint_positions)


            #slide under, grasp, then lift up to avoid damage
            bot.arm.set_ee_cartesian_trajectory(x=0.1)
            bot.gripper.grasp()
            bot.arm.set_ee_cartesian_trajectory(z=0.05)
            bot.arm.set_ee_cartesian_trajectory(x=-0.15)
            bot.arm.set_ee_cartesian_trajectory(z=0.03)


            #rotate to position 2, place then release
            bot.arm.set_single_joint_position(joint_name='waist', position=0.403)
            joint_positions = [0.403, 0.44, 1.25, -1.70, 1.57]
            bot.arm.set_joint_positions(joint_positions)
            bot.gripper.release()


            #pull back then go sleep
            bot.arm.set_ee_cartesian_trajectory(x=-0.03)
            bot.arm.set_single_joint_position(joint_name='waist', position=0.0)
            bot.arm.go_to_sleep_pose()
            

        #MODE 5 SLEEP
        elif mode == '5':

            bot.arm.go_to_sleep_pose()


        #MODE 6 Gripper test
        elif mode == '6':
            bot.gripper.grasp()
            bot.gripper.release()            
            bot.arm.go_to_sleep_pose()


        else:

            print(bcolors.WARNING + "Invalid Entry" + bcolors.ENDC)



if __name__ == '__main__':
    main()