#!/usr/bin/env python
import rospy
import numpy
from std_msgs.msg import Float32

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    pub = rospy.Publisher('random_float_log', Float32, queue_size=10)
    
    rate = rospy.Rate(20) # 20hz
    while not rospy.is_shutdown():
        random_float_log = numpy.log(data.data)
        rospy.loginfo(random_float_log)
        pub.publish(random_float_log)
        rate.sleep()
def simple_subscriber():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('simple_subscriber', anonymous=True)

    rospy.Subscriber("my_random_float", Float32, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
     simple_subscriber()
