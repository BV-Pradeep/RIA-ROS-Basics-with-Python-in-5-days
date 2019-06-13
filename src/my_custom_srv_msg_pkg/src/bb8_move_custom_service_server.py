#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
from time import sleep
from geometry_msgs.msg import Twist

def my_callback(request):
    my_response = MyCustomServiceMessageResponse()
    time = my_response.duration
    rospy.loginfo("BB8 will start moving in circle")
    while time > 0:
        move_bb8.linear.x = 0.1
        move_bb8.angular.z = 0.5
        pub1.publish(move_bb8)
        time-=1
        sleep(1)
    move_bb8.linear.x = 0.0
    move_bb8.angular.z = 0.0
    pub1.publish(move_bb8)
    rospy.loginfo("BB8 finished moving in circle")
    my_response.success = True
    return  my_response# the service Response class, in this case EmptyResponse

rospy.init_node('service_move_bb8_in_custom_circle_server')
my_service = rospy.Service('/move_bb8_in_circle_custom',MyCustomServiceMessage , my_callback) # create the Service called my_service with the defined callback
pub1=rospy.Publisher('/cmd_vel',Twist,queue_size = 1)
move_bb8 = Twist()
rospy.loginfo("Service /move_bb8_in_circle Ready")
rospy.spin()