#! /usr/bin/env python

#Author: B V Pradeep @ 03June2019

#Importing all the required Libraries and messages
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

#Defining the Twist values
move_robot = Twist()
move_robot.linear.x = 0.5
move_robot.angular.z = 0


#Defining a call back function for the Subcriber.
def callback(msg):
    Pub1.publish(move_robot)
    if(msg.ranges[360] < 1):
        move_robot.linear.x = 0.0
        move_robot.angular.z = 0.5
    if(msg.ranges[719] < 1 and msg.ranges[400] == float('inf')):
        move_robot.linear.x = 0.5
        move_robot.angular.z = 0.0
    if(msg.ranges[10] == float('inf') and msg.ranges[719] == float('inf') and msg.ranges[400] == float('inf')):
        move_robot.linear.x = 0.0
        move_robot.angular.z = 0.0
        rospy.loginfo('I Stopped........!')

#Initiating the node,publisher and subscriber
rospy.init_node('topics_quiz_node')
Pub1 = rospy.Publisher('/cmd_vel',Twist,queue_size = 1)
Sub1 = rospy.Subscriber('/kobuki/laser/scan',LaserScan,callback)
rospy.spin()
