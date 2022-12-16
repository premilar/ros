#!/usr/bin/env python
# license removed for brevity
import rospy
import yaml
import random
import math
from sensor_msgs.msg import LaserScan

def fake_scan_publisher():
    scan = LaserScan()
    scan.header.frame_id = 'base_link'

    rospy.init_node('fake_scan_publisher')

    scan.angle_min = (-2.0/3)*math.pi
    # scan.angle_min = rospy.get_param("~angle_min")
    
    scan.angle_max = (2.0/3)*math.pi
    # scan.angle_max = rospy.get_param("~angle_max")
    
    scan.angle_increment = (1.0/300)*math.pi
    # scan.angle_increment = rospy.get_param("~angle_increment")

    print(scan.angle_min, scan.angle_max, scan.angle_increment)
    
    scan.range_min = 1.0
    # scan.range_min = rospy.get_param("~range_min")

    scan.range_max = 10.0
    # scan.range_max = rospy.get_param("~range_max")


    pub = rospy.Publisher('fake_scan', LaserScan, queue_size=10)
    # pub = rospy.Publisher(rospy.get_param("~publisher_topic"),
    #     LaserScan,queue_size=20)
    
    
    
    rate = rospy.Rate(20) # 20hz
    # rate = rospy.Rate(rospy.get_param("~rate"))
    time_seconds = rospy.get_time()
    # scan.scan_time = 0.0
    while not rospy.is_shutdown():
        scan.scan_time = abs(time_seconds- rospy.get_time())
        time_seconds = rospy.get_time() # stores current time of scan
        scan.header.stamp = rospy.get_rostime()
        scan.ranges = []
        #scan.time_increment
        ranges_length =int((scan.angle_max-scan.angle_min)/scan.angle_increment)
        for num in range(ranges_length):
            scan.ranges.append(random.uniform(scan.range_min,scan.range_max))
        rospy.loginfo(scan)
        pub.publish(scan)
        rate.sleep()

if __name__ == '__main__':
    try:
        fake_scan_publisher()
    except rospy.ROSInterruptException:
        pass

