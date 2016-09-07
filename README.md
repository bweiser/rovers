# rovers
Rover Control Station Code

Formerly worked in Ubuntu 10.04 desktop - last update and dist-upgrades performed. Old ROS version

Current issue: 
core service [/rosout] found
process[DirectionButtons-1]: started with pid [4286]
process[Control-2]: started with pid [4287]
Traceback (most recent call last):
Traceback (most recent call last):
  File "/opt/planetxrobots/ros/DirectionButtons/node/DirectionButtons.py", line 12, in <module>
  File "/opt/planetxrobots/ros/Control/node/Control.py", line 10, in <module>
    from DirectionButtons.msg import *
      File "/opt/planetxrobots/ros/DirectionButtons/src/DirectionButtons/msg/__init__.py", line 1, in <module>
from RfidReader.msg import Rfid
  File "/opt/planetxrobots/ros/RfidReader/src/RfidReader/msg/__init__.py", line 1, in <module>
    from _DirectionButton import *
  File "/opt/planetxrobots/ros/DirectionButtons/src/DirectionButtons/msg/_DirectionButton.py", line 171, in <module>
    from _Rfid import *
  File "/opt/planetxrobots/ros/RfidReader/src/RfidReader/msg/_Rfid.py", line 193, in <module>
    _struct_I = roslib.message.struct_I
AttributeError    _struct_I = roslib.message.struct_I
: 'module' object has no attribute 'struct_I'AttributeError
: 'module' object has no attribute 'struct_I'
[DirectionButtons-1] process has died [pid 4286, exit code 1, cmd /opt/planetxrobots/ros/DirectionButtons/node/DirectionButtons.py __name:=DirectionButtons __log:=/home/exhibits/.ros/log/706f1860-7522-11e6-9350-d43d7e45cdbd/DirectionButtons-1.log].
log file: /home/exhibits/.ros/log/706f1860-7522-11e6-9350-d43d7e45cdbd/DirectionButtons-1*.log
[Control-2] process has died [pid 4287, exit code 1, cmd /opt/planetxrobots/ros/Control/node/Control.py __name:=Control __log:=/home/exhibits/.ros/log/706f1860-7522-11e6-9350-d43d7e45cdbd/Control-2.log].
log file: /home/exhibits/.ros/log/706f1860-7522-11e6-9350-d43d7e45cdbd/Control-2*.log
all processes on machine have died, roslaunch will exit
shutting down processing monitor...
... shutting down processing monitor complete

