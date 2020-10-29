cmake_minimum_required(VERSION 2.8.3)
project(influxdb_test)

find_package(catkin_simple REQUIRED)
catkin_simple()

add_definitions(-std=c++17 -Wall -Wextra)

cs_install()
cs_install_scripts(scripts/influxdb_ros_node.py)
cs_export()