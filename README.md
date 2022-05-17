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
    catkin_create_pkg move_cmds geometry_msgs rospy
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
4. Put the "move_around.py" file in the directory
    ```
    cd ~/create_ws/src/move_cmds/src
    # put the file there
    ```
5. Make the node executable:
    ```
    chmod u+x ~/create_ws/src/move_cmds/src/move_around.py
    ```
Once you have the file placed there, you can run it with
    ```
    rosrun move_cmds move_around.py
    ```
When the file prompts for input, you can type a series of number from 0 to 2 to give the Roomba a series of instructions to move around.

For instance: With the input of "021", the robot will do the following: turn left by 15&deg;, move forward by 0.25m, turn right by 15&deg;.
