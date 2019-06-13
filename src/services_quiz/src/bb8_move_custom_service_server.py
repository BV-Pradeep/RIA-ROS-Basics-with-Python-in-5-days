#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from move_bb8 import MoveBB8

"""
# BB8CustomServiceMessage
float64 side       # The distance of each side of the square
int32 repetitions    # The number of times BB-8 has to execute the square movement when the service is called
---
bool success         # Did it achieve it?
"""

def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_square_custom has been called")

    movebb8_object = MoveBB8()

    # We need to add because if we ask 0 repetitions means to execute once, not zero times.
    repetitions_of_square = request.repetitions + 1
    new_side = request.side
    for i in range(repetitions_of_square):
        rospy.loginfo("Start Movement with side = "+str(new_side)+"Repetition = "+str(i))
        movebb8_object.move_square(side=new_side)

    rospy.loginfo("Finished service move_bb8_in_square that was called called")
    response = BB8CustomServiceMessageResponse()
    response.success = True
    return response

rospy.init_node('service_move_bb8_in_square_custom_server')
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage , my_callback) # create the Service called move_bb8_in_square with the defined callback
rospy.loginfo("Service /move_bb8_in_square_custom Ready")
rospy.spin() # mantain the service open.