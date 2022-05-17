# Vision-Language-on-Roomba
## Connect to the roomba and move it around with commands
Follow instructions in https://github.com/AutonomyLab/create_robot to install ros and build a workspace.
1. Source the workspace
2. Launch files using roslaunch
3. To move the Roomba with a certain linear and angular velocity:
    ```
    rostopic pub /cmd_vel geometry_msgs/Twist -r 60 '[0.5, 0, 0]' '[0,0,1]'
    ```
    This command publish the Twist msg to the /cmd_vel topic with a rate of 60 Hz.
4. To receive the status of the robot:
    ```
    rostopic echo battery/charge_ratio
    ```
    This command echoes the topic battery/charge_ration, which prints the current charge of the robot in a percent format.
    
## Get the roomba take in a series of discrete actions
To move the Roomba with a series of actions, we need to follow a similar procedure in the Turtlesim movement tutorial: https://wiki.ros.org/turtlesim/Tutorials/Moving%20in%20a%20Straight%20Line

1. Create the package
    ```
    cd ~/create_ws/src
    catkin_create_pkg move_cmds
    ```
2. Build the workspace
    ```
    cd ~/create_ws
    catkin_make
    ```
3. Create a src folder for the scripts
    ```
    cd ~/create_ws/src/move_cmds
    mkdir src
    cd ~/create_ws
    catkin_make
    ```
4. Put the 
