# HIGH SPEED CAMERA WITH MOBILE MANIPULATOR

Mobile manipulator simulation using ROS, Gazebo and RViz 

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

Download the package folder mobile_manipulator and put it into a catkin_ws in order to make it run.

```bash
cd <your catkin workspace directory>
```
To run and build the package, type the command mentioned below in a new terminal after choosing the catkin_ws directory.

```bash
catkin_make clean && catkin_make
```

### To set up environment variables used by ROS and the Gazebo simulator, run the command below everytime you open a new terminal :

```bash
source devel/setup.bash
```

### Open a new terminal to run each command below.
### To launch the mobile manipulator in Gazebo :

```bash
roslaunch mobile_manipulator template_launch.launch
```
### To Visualise the mobile_manipulator and camera in RViz :
Open a new terminal 

```bash
source devel/setup.bash
```

```bash
rosrun rviz rviz
``` 
Open the rviz config file in the directory “<your catkin workspace directory>/src/mobile_manipulator/config”


### To move the mobile manipulator :

Open a new terminal 

```bash
source devel/setup.bash
```

```bash
rosrun mobile_manipulator move.py
``` 
