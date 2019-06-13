#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.


def my_callback(request):
    print "My_callback has been called"
    return EmptyResponse() # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split()))

rospy.init_node('service_server')
my_service = rospy.Service('/my_service', Empty , my_callback) # create the Service called my_service with the defined callback
rospy.spin() # maintain the service open.