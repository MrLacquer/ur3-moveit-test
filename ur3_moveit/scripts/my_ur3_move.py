#!/usr/bin/env python

# Author: Hyeonjun Park, Ph.D. candidate
# Affiliation: Human-Robot Interaction LAB, Kyung Hee University, South Korea
# koreaphj91@gmail.com
# init: 9 Apr 2019
# revision: 17 Feb 2020

import sys
import rospy
import tf
import moveit_commander  # https://answers.ros.org/question/285216/importerror-no-module-named-moveit_commander/
import random
from geometry_msgs.msg import Pose, Point, Quaternion
from math import pi

## my lib
import moveit_msgs.msg

group_name = "manipulator"
pose_goal = Pose()
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('ur3_move',anonymous=True)
group = [moveit_commander.MoveGroupCommander(group_name)]  # ur3 moveit group name: manipulator


### my Test
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                               moveit_msgs.msg.DisplayTrajectory,
                                               queue_size=20)
'''
planning_frame = group.get_planning_frame()
print("=============== Reference frame: %s", planning_frame)

eef_link = group.get_end_effector_link()                    
print("=============== end effector frame: %s", eef_link)    
####
'''
xx = 0.01

pose_goal.orientation.w = 0.0
pose_goal.position.x = 0.2   # red line      0.2   0.2
pose_goal.position.y = 0.0 # green line  0.15   0.15
pose_goal.position.z = 0.2 # blue line   # 0.35   0.6
  
group[0].set_pose_target(pose_goal)
group[0].go(True)

rospy.sleep(1)

while not rospy.is_shutdown():
  xx = xx + 0.01    
  pose_goal.orientation.w = 0.0
  pose_goal.position.x = 0.2 + xx   # red line      0.2   0.2
  pose_goal.position.y = 0.0 # green line  0.15   0.15
  pose_goal.position.z = 0.2 # blue line   # 0.35   0.6
  group[0].set_pose_target(pose_goal)
  group[0].go(True)

  print("prePos: ", pose_goal.position.x, pose_goal.position.y,pose_goal.position.z )
  rospy.sleep(0.5)

moveit_commander.roscpp_shutdown()