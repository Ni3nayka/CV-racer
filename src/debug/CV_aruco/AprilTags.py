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
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        tags = self.at_detector.detect(gray)
        try: 
            print(tags[0])
            print(tags[0].center)
            print(tags[0].homography)
        except IndexError: pass
        for tag in tags:
            cv2.circle(frame, tuple(tag.corners[0].astype(int)), 4, (255, 0, 0), 2) # left-top
            cv2.circle(frame, tuple(tag.corners[1].astype(int)), 4, (0, 255, 0), 2) # right-top
            cv2.circle(frame, tuple(tag.corners[2].astype(int)), 4, (0, 0, 255), 2) # right-bottom
            cv2.circle(frame, tuple(tag.corners[3].astype(int)), 4, (255, 0, 255), 2) # left-bottom


if __name__=='__main__':
    cap = cv2.VideoCapture(1)
    april_tags = AprilTagsReader()

    while(1):
        ret, frame = cap.read()
        k=cv2.waitKey(1)
        if k==27:
            break
        april_tags.test(frame)
        cv2.imshow('capture', frame)

    cap.release()
    cv2.destroyAllWindows()