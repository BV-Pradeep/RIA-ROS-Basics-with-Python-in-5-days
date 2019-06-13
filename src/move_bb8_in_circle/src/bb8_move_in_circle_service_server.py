#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist

def my_callback(request):
    rospy.loginfo("BB8 will start moving in circle")
    move_bb8.linear.x = 0.1
    move_bb8.angular.z = 0.5
    pub1.publish(move_bb8)
    rospy.loginfo("BB8 finished moving in circle")
    return EmptyResponse() # the service Response class, in this case EmptyResponse

rospy.init_node('service_move_bb8_in_circle_server')
my_service = rospy.Service('/move_bb8_in_circle', Empty , my_callback) # create the Service called my_service with the defined callback
pub1=rospy.Publisher('/cmd_vel',Twist,queue_size = 1)
move_bb8 = Twist()
rospy.loginfo("Service /move_bb8_in_circle Ready")
rospy.spin()