cmake_minimum_required(VERSION 2.8.3)
project(services_quiz)


## Here go all the packages needed to COMPILE the messages of topic, services and actions.
## Its only geting its paths, and not really importing them to be used in the compilation.
## Its only for further functions in CMakeLists.txt to be able to find those packages.
## In package.xml you have to state them as build
find_package(catkin REQUIRED COMPONENTS
  std_msgs
  message_generation
)

## Generate services in the 'srv' folder
## In this function will be all the action messages of this package ( in the action folder ) to be compiled.
## You can state that it gets all the actions inside the action directory: DIRECTORY action
## Or just the action messages stated explicitly: FILES my_custom_action.action
## In your case you only need to do one of two things, as you wish.
add_service_files(
  FILES
  BB8CustomServiceMessage.srv
)

## Here is where the packages needed for the action messages compilation are imported.
generate_messages(
  DEPENDENCIES
  std_msgs
)

## State here all the packages that will be needed by someone that executes something from your package.
## All the packages stated here must be in the package.xml as exec_depend
catkin_package(
  CATKIN_DEPENDS rospy
)


include_directories(
  ${catkin_INCLUDE_DIRS}
)