#! /usr/bin/env python

import rospy
# Import the service message used by the service /gazebo/delete_model
from gazebo_msgs.srv import DeleteModel, DeleteModelRequest
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('service_client')
# Wait for the service client /gazebo/delete_model to be running
rospy.wait_for_service('/gazebo/delete_model')
# Create the connection to the service
delete_model_service = rospy.ServiceProxy('/gazebo/delete_model', DeleteModel)
# Create an object of type DeleteModelRequest
delete_model_object = DeleteModelRequest()
# Fill the variable model_name of this object with the desired value
delete_model_object.model_name = "bowl_1"
# Send through the connection the name of the object to be deleted by the service
result = delete_model_service(delete_model_object)
# Print the result given by the service called
print result