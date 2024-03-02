# https://russianblogs.com/article/79843527921/
# https://github.com/pupil-labs/apriltags

# pip3 install opencv-python
# pip3 install pupil-apriltags

import cv2
import numpy as np
from pupil_apriltags import Detector

class AprilTagsReader:

    def __init__(self):
        self.at_detector = Detector(
            families="tag36h11",
            nthreads=1, # 4
            quad_decimate=1.0,
            quad_sigma=0.0,
            refine_edges=1,
            decode_sharpening=0.25,
            debug=0
        )
    
    def test(self, frame):
        try:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            tags = self.at_detector.detect(gray)
            try: 
                tag = tags[0]
                print(tag.tag_id)
                print(tag.center)
                for i in range(4): print(tuple(tags[0].corners[i].astype(int)))
                left_top = tuple(tag.corners[0].astype(int))
                right_top = tuple(tag.corners[1].astype(int))
                right_bottom = tuple(tag.corners[2].astype(int))
                left_bottom = tuple(tag.corners[3].astype(int))
                # left_size = ((left_top[0]-left_bottom[0])**2+(left_top[1]-left_bottom[1])**2)**(1/2)
                # right_size = ((right_top[0]-right_bottom[0])**2+(right_top[1]-right_bottom[1])**2)**(1/2)
                left_size = left_top[1]-left_bottom[1]
                right_size = right_top[1]-right_bottom[1]
                gorizontal_size = left_top[0]-right_top[0]
                print(left_size,right_size,gorizontal_size)
                angle = int((gorizontal_size/(left_size+right_size)+0.5)*400)
                print(angle)
            except IndexError: pass
            for tag in tags:
                cv2.circle(frame, tuple(tag.corners[0].astype(int)), 4, (255, 0, 0), 2) # left-top
                cv2.circle(frame, tuple(tag.corners[1].astype(int)), 4, (0, 255, 0), 2) # right-top
                cv2.circle(frame, tuple(tag.corners[2].astype(int)), 4, (0, 0, 255), 2) # right-bottom
                cv2.circle(frame, tuple(tag.corners[3].astype(int)), 4, (255, 0, 255), 2) # left-bottom
        except cv2.error: print("camera error")



if __name__=='__main__':

    DEBUG = False

    cap = 0
    if not DEBUG: cap = cv2.VideoCapture(0)

    april_tags = AprilTagsReader()

    ret, frame = None,None
    if DEBUG: 
        frame = cv2.imread("1.png")
        april_tags.test(frame)

    while(1):
        if not DEBUG: 
            ret, frame = cap.read()
            april_tags.test(frame)
        k=cv2.waitKey(1)
        if k==27:
            break
        cv2.imshow('capture', frame)

    if not DEBUG: cap.release()
    cv2.destroyAllWindows()