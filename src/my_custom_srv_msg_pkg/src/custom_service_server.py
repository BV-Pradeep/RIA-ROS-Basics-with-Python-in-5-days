#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse

def my_callback(request):
    print "Request Data Received"
    print "Radians = " + str(request.radians)
    print "Repeatitions = " + str(request.repeatitions)
    my_response = MyCustomServiceMessageResponse()
    if request.radians > 0.5 :
        my_response.success = True
    else:
        my_response.success = False
    return my_response

rospy.init_node('service_client')
my_service = rospy.Service('/my_service', MyCustomServiceMessage , my_callback)
rospy.spin()
