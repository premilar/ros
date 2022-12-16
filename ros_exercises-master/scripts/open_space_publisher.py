#!/usr/bin/env python
import rospy
import numpy
from ros_exercises.msg import OpenSpace
from sensor_msgs.msg import LaserScan

def callback(data):
    openspace = OpenSpace()
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
    
    pub = rospy.Publisher('open_space', OpenSpace, queue_size=10)
    # pub = rospy.Publisher(rospy.get_param("~publisher_topic"),
    #     OpenSpace,queue_size=20)
    
    # pub_angle = rospy.Publisher('open_space/angle', Float32, queue_size=10)
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

        openspace.distance = max_distance
        openspace.angle = angle
        # rospy.loginfo(max_distance)
        # rospy.loginfo(angle)
        pub.publish(openspace)
        
        # pub_distance.publish(max_distance)
        # pub_angle.publish(angle)
        rate.sleep()
def open_space_publisher():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('open_space_publisher')

    rospy.Subscriber("fake_scan", LaserScan, callback)
    # rospy.Subscriber(rospy.get_param("~subscriber_topic"),
    #     LaserScan,queue_size=20)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
     open_space_publisher()
