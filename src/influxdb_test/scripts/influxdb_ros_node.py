#!/usr/bin/env python3

import rospy
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS, PointSettings

def listener():
    rospy.init_node('influxdb_node', anonymous=True)
    print("ROS node successfully started.")
    rospy.spin()

if __name__ == '__main__':
    listener()