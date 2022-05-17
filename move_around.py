#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

SPEED = 0.2
ANGLE_SPEED = 30 # degree/s

def rotate(angle_speed=ANGLE_SPEED, clockwise=0):
    #Starts a new node
    rospy.init_node('roomba', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    angle = 15 #input("Type your distance (degrees):")
    # clockwise = 1 #input("Clockwise?: ") #True or false

    #Converting from angles to radians
    angular_speed = ANGLE_SPEED*2*PI/360 #speed*2*PI/360
    relative_angle = angle*2*PI/360

    #We wont use linear components
    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    # Checking if our movement is CW or CCW
    if clockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)
    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(abs(current_angle) < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)


    #Forcing our robot to stop
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    # rospy.spin()

def forward(speed=SPEED):
    rospy.init_node('roomba', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x = abs(speed)

    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0


        #Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0

        #Loop to move the turtle in an specified distance
    while(current_distance < 0.25):
            #Publish the velocity
        velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
        current_distance= speed*(t1-t0)
        #After the loop, stops the robot
    vel_msg.linear.x = 0
        #Force the robot to stop
    velocity_publisher.publish(vel_msg)


if __name__ == '__main__':
    try:
        #Testing our function
        # forward()
        # rotate()
        # forward()
        # forward()
        # rotate()
        cmd_list = input("Your cmds:")
        for cmd in cmd_list:
            if cmd == '0':
                print('left')
                rotate(clockwise=1)
            elif cmd == '1':
                print('right')
                rotate(clockwise=0)
            elif cmd == '2':
                print('forward')
                forward()
            else:
                print('nothing happens')
    except rospy.ROSInterruptException: pass