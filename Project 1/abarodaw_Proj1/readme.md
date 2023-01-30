# SKATEBOARD 

Robot car simulation using ROS, Gazebo and RViz 

## SOFTWARE FRAMEWORK FOR ROBOT

ROS

## LIBRARIES

sys, select, termios, tty, rospy

## PROGRAMMING LANGUAGE

Python 3

## ENVIRONMENT USED

Visual Studio code (You can also use any python supported IDE)

## USAGE 

### Package initialization and setup :

Download the catkin package "skateboard" and place it in your catkin workspace (catkin_ws/src) directory.
To build the package, type the command mentioned below in a new terminal after choosing the catkin_ws directory.

```bash
cd catkin_ws
```
```bash
catkin_make clean && catkin_make
```

### To set up environment variables used by ROS and the Gazebo simulator, run the command below everytime you open a new terminal :

```bash
source devel/setup.bash
```

### Open a new terminal to run each command below.
### To launch the robot car in competition arena world in Gazebo :

```bash
roslaunch skateboard template_launch.launch
```
### To Visualise the robot car and laser scan in RViz :

```bash
rosrun rviz rviz
``` 
Open the config file rviz.config.rviz after launching RViz. The file is located in the config folder of the skateboard package.

### To operate the robot car using teleop :

```bash
rosrun skateboard teleop_template.py
``` 
### To move the skateboard in a circle by publishing and subscribing the commands :

```bash
rosrun skateboard circle_pub.py
``` 
```bash
rosrun skateboard circle_sub.py
``` 
### To move the skateboard in a straight line by publishing and subscribing the commands :

```bash
rosrun skateboard straight_line_pub.py
``` 
```bash
rosrun skateboard straight_line_sub.py
``` 