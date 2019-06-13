#! /usr/bin/env python

import rospy
import random
import time

# Options: DEBUG, INFO, WARN, ERROR, FATAL
rospy.init_node('log_demo', log_level=rospy.DEBUG)
rate = rospy.Rate(0.5)

#rospy.loginfo_throttle(120, "DeathStars Minute info: "+str(time.time()))

while not rospy.is_shutdown():
    rospy.logdebug("There is a missing droid")
    rospy.loginfo("The Emperors Capuchino is done")
    rospy.logwarn("The Revels are coming time "+str(time.time()))
    exhaust_number = random.randint(1,100)
    port_number = random.randint(1,100)
    rospy.logerr(" The thermal exhaust port %s, right below the main port %s", exhaust_number, port_number)
    rospy.logfatal("The DeathStar Is EXPLODING")
    rate.sleep()
    rospy.logfatal("END")