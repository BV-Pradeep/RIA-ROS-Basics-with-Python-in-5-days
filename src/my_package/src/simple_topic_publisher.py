#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('topic_publisher')
pub1 = rospy.Publisher('\counter',Int32,queue_size=1)
rate = rospy.Rate(2)               # We create a Rate object of 2Hz
var = Int32()
var.data = 0

while not rospy.is_shutdown():     # Endless loop until Ctrl + C
   pub1.publish(var)
   var.data += 1
   rate.sleep()