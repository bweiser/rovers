#!/bin/bash

source /opt/ros/kinetic/setup.bash

roverDir=/opt/planetxrobots/ros

export ROS_PACKAGE_PATH=${roverDir}:$ROS_PACKAGE_PATH

roscd Control
roslaunch Control Control.launch

exit 0
