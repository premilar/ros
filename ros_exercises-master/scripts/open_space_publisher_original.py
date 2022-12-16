#!/usr/bin/env python
import rospy
import numpy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
    pub_distance = rospy.Publisher('open_space/distance', Float32, queue_size=10)
    pub_angle = rospy.Publisher('open_space/angle', Float32, queue_size=10)
    rate = rospy.Rate(20) # 20hz
    while not rospy.is_shutdown():
        scan_ranges = data.ranges
        angle_min = data.angle_min
        angle_max = data.angle_max
        angle_increment = data.angle_increment
        max_distance = scan_ranges[0]
        for i, distance in enumerate(scan_ranges):
            if distance > max_distance:
                max_distance = distance
                angle = angle_min + i*angle_increment
        rospy.loginfo(max_distance)
        rospy.loginfo(angle)
        pub_distance.publish(max_distance)
        pub_angle.publish(angle)
        rate.sleep()
def open_space_publisher():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('open_space_publisher', anonymous=True)

    rospy.Subscriber("fake_scan", LaserScan, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
     open_space_publisher()
