#!/usr/bin/env python

import sys
import rospy
import tf
import moveit_commander  # https://answers.ros.org/question/285216/importerror-no-module-named-moveit_commander/
import random
from geometry_msgs.msg import Pose, Point, Quaternion
from math import pi

pose_goal = Pose()
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('ur3_move',anonymous=True)
group = [moveit_commander.MoveGroupCommander("manipulator")]  # ur3 moveit group name: manipulator

while not rospy.is_shutdown():
  pose_goal.orientation.w = 0.0
  pose_goal.position.x = 0.2 # red line      0.2   0.2
  pose_goal.position.y = 0.15  # green line  0.15   0.15
  pose_goal.position.z = 0.2  # blue line   # 0.35   0.6
  group[0].set_pose_target(pose_goal)
  group[0].go(True)

moveit_commander.roscpp_shutdown()