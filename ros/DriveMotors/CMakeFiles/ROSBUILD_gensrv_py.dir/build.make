# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canoncical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /opt/planetxrobots/ros/DriveMotors

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /opt/planetxrobots/ros/DriveMotors

# Utility rule file for ROSBUILD_gensrv_py.

CMakeFiles/ROSBUILD_gensrv_py: src/DriveMotors/srv/__init__.py

src/DriveMotors/srv/__init__.py: src/DriveMotors/srv/_Move.py
	$(CMAKE_COMMAND) -E cmake_progress_report /opt/planetxrobots/ros/DriveMotors/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating src/DriveMotors/srv/__init__.py"
	/opt/ros/diamondback/stacks/ros_comm/clients/rospy/scripts/gensrv_py.py --initpy /opt/planetxrobots/ros/DriveMotors/srv/Move.srv

src/DriveMotors/srv/_Move.py: srv/Move.srv
src/DriveMotors/srv/_Move.py: /opt/ros/diamondback/stacks/ros_comm/clients/rospy/scripts/gensrv_py.py
src/DriveMotors/srv/_Move.py: /opt/ros/diamondback/ros/core/roslib/scripts/gendeps
src/DriveMotors/srv/_Move.py: manifest.xml
src/DriveMotors/srv/_Move.py: /opt/ros/diamondback/ros/tools/rospack/manifest.xml
src/DriveMotors/srv/_Move.py: /opt/ros/diamondback/ros/core/roslib/manifest.xml
src/DriveMotors/srv/_Move.py: /opt/ros/diamondback/stacks/ros_comm/messages/std_msgs/manifest.xml
src/DriveMotors/srv/_Move.py: /opt/ros/diamondback/stacks/ros_comm/messages/rosgraph_msgs/manifest.xml
src/DriveMotors/srv/_Move.py: /opt/ros/diamondback/ros/core/rosbuild/manifest.xml
src/DriveMotors/srv/_Move.py: /opt/ros/diamondback/ros/core/roslang/manifest.xml
src/DriveMotors/srv/_Move.py: /opt/ros/diamondback/stacks/ros_comm/clients/rospy/manifest.xml
src/DriveMotors/srv/_Move.py: /opt/ros/diamondback/stacks/ros_comm/messages/std_msgs/msg_gen/generated
src/DriveMotors/srv/_Move.py: /opt/ros/diamondback/stacks/ros_comm/messages/rosgraph_msgs/msg_gen/generated
	$(CMAKE_COMMAND) -E cmake_progress_report /opt/planetxrobots/ros/DriveMotors/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating src/DriveMotors/srv/_Move.py"
	/opt/ros/diamondback/stacks/ros_comm/clients/rospy/scripts/gensrv_py.py --noinitpy /opt/planetxrobots/ros/DriveMotors/srv/Move.srv

ROSBUILD_gensrv_py: CMakeFiles/ROSBUILD_gensrv_py
ROSBUILD_gensrv_py: src/DriveMotors/srv/__init__.py
ROSBUILD_gensrv_py: src/DriveMotors/srv/_Move.py
ROSBUILD_gensrv_py: CMakeFiles/ROSBUILD_gensrv_py.dir/build.make
.PHONY : ROSBUILD_gensrv_py

# Rule to build all files generated by this target.
CMakeFiles/ROSBUILD_gensrv_py.dir/build: ROSBUILD_gensrv_py
.PHONY : CMakeFiles/ROSBUILD_gensrv_py.dir/build

CMakeFiles/ROSBUILD_gensrv_py.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean.cmake
.PHONY : CMakeFiles/ROSBUILD_gensrv_py.dir/clean

CMakeFiles/ROSBUILD_gensrv_py.dir/depend:
	cd /opt/planetxrobots/ros/DriveMotors && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /opt/planetxrobots/ros/DriveMotors /opt/planetxrobots/ros/DriveMotors /opt/planetxrobots/ros/DriveMotors /opt/planetxrobots/ros/DriveMotors /opt/planetxrobots/ros/DriveMotors/CMakeFiles/ROSBUILD_gensrv_py.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/ROSBUILD_gensrv_py.dir/depend
