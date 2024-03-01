# https://learnopencv.com/augmented-reality-using-aruco-markers-in-opencv-c-python/
# https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
# pip install opencv-contrib-python==4.6.0.66 <= https://stackoverflow.com/questions/45972357/python-opencv-aruco-no-module-named-cv2-aruco
# https://stackoverflow.com/questions/74964527/attributeerror-module-cv2-aruco-has-no-attribute-dictionary-get

# import numpy as np
# import cv2 as cv

# def aruco(frame):
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_250) 
#     parameters = cv.aruco.DetectorParameters()
#     detector = cv.aruco.ArucoDetector(dictionary, parameters)
#     markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(gray)
#     #print(markerCorners, markerIds, rejectedCandidates)
    
#     frame_markers = cv.aruco.drawDetectedMarkers(frame.copy(), markerCorners, markerIds)

#     # plt.figure()
#     # plt.imshow(frame_markers)
#     print(" ",markerCorners)
#     try:
#         for i in range(len(markerIds)):
#             c = markerCorners[i][0]
#             print(c)
#     except TypeError: pass
#     #     plt.plot([c[:, 0].mean()], [c[:, 1].mean()], "o", label = "id={0}".format(ids[i]))
#     # plt.legend()
#     # cv.imshow('frame1', frame_markers)

# cap = cv.VideoCapture(0)
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
    
#     # Our operations on the frame come here
#     #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#     aruco(frame)

#     # Display the resulting frame
#     cv.imshow('frame', frame)
#     if cv.waitKey(1) == ord('q'):
#         break
# # When everything done, release the capture
# cap.release()
# cv.destroyAllWindows()

import cv2
import cv2.aruco as aruco
import numpy as np
import os

def findArucoMarkers(img, markerSize = 6, totalMarkers=250, draw=True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    
    # dictionary = aruco.getPredefinedDictionary(key) #aruco.DICT_6X6_250) 
    # parameters = aruco.DetectorParameters()
    # detector = aruco.ArucoDetector(dictionary, parameters)
    # markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(gray)
    # print(markerIds)
    
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    bboxs, ids, rejected = aruco.detectMarkers(gray, arucoDict, parameters = arucoParam)
    print(ids)

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    findArucoMarkers(img)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()

