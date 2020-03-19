# UR3 manipulator with moveit test code

## Overview

This pacakge is for [UR3, UR5 and UR10](http://wiki.ros.org/universal_robot/Tutorials/Getting%20Started%20with%20a%20Universal%20Robot%20and%20ROS-Industrial) manipulator with [Moveit!](http://docs.ros.org/kinetic/api/moveit_tutorials/html/index.html) test code. 
[Move Group Python Interface](http://docs.ros.org/kinetic/api/moveit_tutorials/html/doc/move_group_python_interface/move_group_python_interface_tutorial.html)  
And there is no launch files, only contain node files. The source code written by Python 2.7.  

It is working on Gazebo simulation and real robot.  


**Author: [Hyeonjun Park](https://www.linkedin.com/in/hyeonjun-park-41bb59125), koreaphj91@gmail.com**

**Affiliation: [Human-Robot Interaction LAB](https://khu-hri.weebly.com), Kyung Hee Unviersity, South Korea**



## Installation
- Before do this, please backup important files.

### Dependencies

This software is built on the Robotic Operating System ([ROS](http://wiki.ros.org/ROS/Installation)).

One line install: https://cafe.naver.com/openrt/14575 
```
for Desktop

wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros_kinetic.sh && chmod 755 ./install_ros_kinetic.sh && bash ./install_ros_kinetic.sh
```

- Moveit! pacakge
Moveit! ROS depends on following web pages: ([Moveit! installation](http://docs.ros.org/kinetic/api/moveit_tutorials/html/doc/getting_started/getting_started.html))
In my case, the Kinetic version.  
```
rosdep update
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install ros-kinetic-catkin python-catkin-tools
sudo apt install ros-kinetic-moveit

rospack profile && rosstack profile
```

## How to start?

```
$ cd ~/catkin_ws/src && git clone https://github.com/MrLacquer/ur3-moveit-test.git
$ cd ~/catkin_ws && catkin_make
$ rospack profile && rosstack profile

- Bring up Gazebo and the URx manipulator:
$ roslaunch ur_gazebo ur3.launch
$ roslaunch ur3_moveit_config ur3_moveit_planning_execution.launch sim:=true
$ roslaunch ur3_moveit_config moveit_rviz.launch config:=true

- Bring up Real URx manipulator:
$ roslaunch ur_modern_driver ur3_bringup.launch robot_ip:=IP_OF_THE_ROBOT 
$ roslaunch ur3_moveit_config ur3_moveit_planning_execution.launch

- Registration
$ cd ~/catkin_ws/src/ur3-moveit-test/ur3_moveit/script
$ chmod +x ur3_move.py
$ chmod +x ur3_demo.py 

- Controlling the URx manipulator:
$ rosrun ur3_moveit ur3_move.py 
or
$ rosrun ur3_moveit ur3_demo.py 
```
## Demo




