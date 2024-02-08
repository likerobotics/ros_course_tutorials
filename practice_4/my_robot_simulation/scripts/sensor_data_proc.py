#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image

import cv2
from cv_bridge import CvBridge

class sensor_datahandler:

    def __init__(self):
        sub_topic_name ="/diff_drive_robot/camera1/image_raw"
        self.camera_subscriber = rospy.Subscriber(sub_topic_name, Image, self.camera_cb)
        # self.out = cv2.VideoWriter('/home/superuser/output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (640,480))
        self.bridge = CvBridge()
        self.curent_image = None

    def camera_cb(self, data):
        frame = self.bridge.imgmsg_to_cv2(data)
        print(frame.shape)
        # edge_frame = cv2.Canny(frame, 100, 200)
        # self.out.write(frame)
        cv2.imshow("output", frame)
        cv2.waitKey(1)


if __name__ == '__main__':
    rospy.init_node("camera_data_processing")
    sensor_datahandler()
    rospy.spin()