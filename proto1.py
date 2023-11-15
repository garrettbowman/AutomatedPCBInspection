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

    mode = input("Press 1, 2 or 3:")

    while(1):
        #MODE 1
        if mode == '1':
            bot.arm.go_to_home_pose()
            #bot.gripper.release()
            joint_positions = [0, 0.34, 0.81, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)


            #slide under?
            joint_positions = [0.28, 0.34, 0.81, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)


            #at the tray
            joint_positions = [0.28, 0.57, 0.32, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)
            bot.gripper.grasp()

            #Pick up and rotate
            bot.arm.set_ee_cartesian_trajectory(z=0.3)
            bot.arm.set_single_joint_position(joint_name='waist', position=-1.5)


            #dropoff location
            joint_positions = [-1.6, 0.57, 0.32, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)

            #serial communication with microscope


            #slide out
            bot.gripper.release()
            joint_positions = [-1.6, 0.34, 0.81, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)
            


            bot.arm.go_to_home_pose()

            mode = input("Press 1, 2 or 3:")

        #MODE 2    
        elif mode == '2':

            bot.arm.go_to_home_pose()
            #bot.gripper.release()
            joint_positions = [0, 0.34, 0.81, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)


            #slide under?
            joint_positions = [-0.28, 0.34, 0.81, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)


            #at the tray
            joint_positions = [-0.28, 0.57, 0.32, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)
            bot.gripper.grasp()

            #Pick up and rotate
            bot.arm.set_ee_cartesian_trajectory(z=0.3)
            bot.arm.set_single_joint_position(joint_name='waist', position=-1.5)


            #dropoff location
            joint_positions = [-1.5, 0.57, 0.32, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)

            #serial communication with microscope


            #slide out
            bot.gripper.release()
            joint_positions = [-1.5, 0.34, 0.81, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)
            


            
            bot.arm.go_to_home_pose()
            
        

            mode = input("Press 1, 2 or 3:")


        #MODE 3
        elif mode == '3':
            bot.arm.go_to_home_pose()

            
            bot.arm.go_to_sleep_pose()

            mode = input("Press 1, 2 or 3:")


        #MODE 4
        if mode == '4':
            bot.arm.go_to_home_pose()
            #bot.gripper.release()
            joint_positions = [0, 0.34, 0.81, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)


            #slide under?
            joint_positions = [0.28, 0.34, 0.81, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)


            #at the tray
            joint_positions = [0.28, 0.57, 0.32, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)
            bot.gripper.grasp()

            #Pick up and rotate
            bot.arm.set_ee_cartesian_trajectory(z=0.3)
            bot.arm.set_single_joint_position(joint_name='waist', position=-1.5)


            #dropoff location
            joint_positions = [-1.6, 0.57, 0.32, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)

            #serial communication with microscope
            time.sleep(3)

            #slide out
            #bot.gripper.release()
            #joint_positions = [-1.6, 0.34, 0.81, -1.03, -1.57]
            #bot.arm.set_joint_positions(joint_positions)
            
            #Pick up and rotate
            bot.arm.set_ee_cartesian_trajectory(z=0.3)
            bot.arm.set_single_joint_position(joint_name='waist', position=0.28)

            #at the original location
            joint_positions = [0.28, 0.57, 0.32, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)
            bot.gripper.release()

            #slide out?
            joint_positions = [0.28, 0.34, 0.81, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)

            joint_positions = [0, 0.34, 0.81, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)


            bot.arm.go_to_home_pose()

            mode = input("Press 1, 2 or 3:")
        
        #MODE 5
        if mode == '5':
            bot.arm.go_to_home_pose()
            #bot.gripper.release()
            joint_positions = [0, 0.34, 0.81, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)


            #slide under?
            joint_positions = [-0.28, 0.34, 0.81, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)


            #at the tray
            joint_positions = [-0.28, 0.57, 0.32, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)
            bot.gripper.grasp()

            #Pick up and rotate
            bot.arm.set_ee_cartesian_trajectory(z=0.3)
            bot.arm.set_single_joint_position(joint_name='waist', position=-1.5)


            #dropoff location
            joint_positions = [-1.6, 0.57, 0.32, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)

            #serial communication with microscope
            time.sleep(3)

            #slide out
            #bot.gripper.release()
            #joint_positions = [-1.6, 0.34, 0.81, -1.03, -1.57]
            #bot.arm.set_joint_positions(joint_positions)
            
            #Pick up and rotate
            bot.arm.set_ee_cartesian_trajectory(z=0.3)
            bot.arm.set_single_joint_position(joint_name='waist', position=-0.28)

            #at the original location
            joint_positions = [-0.28, 0.57, 0.32, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)
            bot.gripper.release()

            #slide out?
            joint_positions = [-0.28, 0.34, 0.81, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)

            joint_positions = [0, 0.34, 0.81, -1.03, -1.57]
            bot.arm.set_joint_positions(joint_positions)


            bot.arm.go_to_home_pose()

            mode = input("Press 1, 2 or 3:")

        else:

            mode = input("Not a valid entry. Press 1, 2 or 3:")

            if mode != '1' | '2' | '3':

                print("Shutting down.")
                bot.arm.go_to_home_pose()
                bot.arm.go_to_sleep_pose()
                bot.shutdown()



if __name__ == '__main__':
    main()