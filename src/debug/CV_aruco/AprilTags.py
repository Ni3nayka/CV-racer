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
                print(tags[0])
                print(tags[0].center)
                print(tags[0].homography)
                '''
                что определяет "взгляд слева-справа"?
                + - -
                + - -
                + - -
                '''
                print(tags[0].homography[0][2])
            except IndexError: pass
            for tag in tags:
                cv2.circle(frame, tuple(tag.corners[0].astype(int)), 4, (255, 0, 0), 2) # left-top
                cv2.circle(frame, tuple(tag.corners[1].astype(int)), 4, (0, 255, 0), 2) # right-top
                cv2.circle(frame, tuple(tag.corners[2].astype(int)), 4, (0, 0, 255), 2) # right-bottom
                cv2.circle(frame, tuple(tag.corners[3].astype(int)), 4, (255, 0, 255), 2) # left-bottom
        except cv2.error: print("img error")

    def get_first_homography(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        tags = self.at_detector.detect(gray)
        try: 
            print(tags[0])
            print(tags[0].center)
            a = tags[0].homography #tuple(tags[0].homography.astype(float))
            # for i in range(len(a)):
            #     a[i] = tuple(a[i])
            b = [(0, 0, 0)]
            for d in a: b.append(tuple([x/1 for x in d]))
            b = tuple(b)
            print(b)
            # print(a)
            return b
            # return ((86, 25, 177), (-7, 78, 219), (0, 0., 1))
            # return ((0, 0, 0),(0.86, 0.25, 1.77), (-0.07, 0.78, 2.19), (0, 0, 1))
            # return ((0, 0, 0),(1, 0, 0),(0, 1, 0),(0, 0, 1),)
        except IndexError: return ((0, 0, 0),(0, 0, 0),(0, 0, 0),(0, 0, 0),)



if __name__=='__main__':

    DEBUG = False

    cap = 0
    if not DEBUG: cap = cv2.VideoCapture(0)

    april_tags = AprilTagsReader()

    while(1):
        ret, frame = None,None
        if DEBUG: frame = cv2.imread("1.png")
        else: ret, frame = cap.read()
        k=cv2.waitKey(1)
        if k==27:
            break
        april_tags.test(frame)
        cv2.imshow('capture', frame)

    if not DEBUG: cap.release()
    cv2.destroyAllWindows()

'''
что определяет "взгляд слева-справа"?
? - +
+ - -
+ - -

слева
[[ 8.48094672e+01  5.33483259e-01  1.56832360e+02]
 [ 3.77108407e+01  7.89696354e+01  2.76276063e+02]
 [ 1.49926296e-01 -4.94512437e-03  1.00000000e+00]]

 спереди
[[ 1.05094148e+02 -1.23523969e+00  3.26280164e+02]
 [ 1.19401841e+00  1.05350364e+02  2.97722349e+02]
 [-1.59750387e-03 -8.79452892e-04  1.00000000e+00]]

 справа
[[ 4.90837134e+01  8.22520344e+00  4.98689182e+02]   
 [-2.53858144e+01  1.07545509e+02  2.27618574e+02]
 [-1.19309740e-01  1.80467832e-02  1.00000000e+00]]

 сверху
 [[ 1.58160915e+02  6.83112274e+01  3.58737620e+02]
 [-3.12853030e+00  1.74642617e+02  2.18999901e+02]
 [-8.89516786e-03  2.01039012e-01  1.00000000e+00]]

 снизу
 [[ 1.39615712e+02 -4.94928460e+01  3.64955891e+02]
 [ 4.02515822e+00  8.24064255e+01  2.34239755e+02]
 [ 2.93352569e-03 -1.50347039e-01  1.00000000e+00]]

 повернул телефон на 90 градусов влево
[[ 3.12461785e+00 -1.52105789e+02  3.51661999e+02]
 [ 1.58493048e+02  2.14969072e+00  2.59244941e+02]
 [ 8.42305356e-03  7.97797757e-03  1.00000000e+00]]

 вправо
 [[-3.79614793e+00  1.36104517e+02  4.03857232e+02]
 [-1.37396629e+02  2.62771722e+00  2.00911435e+02]
 [-1.42491548e-02  5.99854011e-03  1.00000000e+00]]
'''