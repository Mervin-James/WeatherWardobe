from imutils.video import VideoStream
from imutils.video import WebcamVideoStream
from scipy.spatial import distance as dist
from imutils import face_utils
from threading import Thread
#from twilio.rest import Client
#import RPi.GPIO as GPIO
import numpy as np
import imutils
import cv2
import argparse
import dlib
import os
import time


ap = argparse.ArgumentParser()
ap.add_argument("-w", "--webcam", type=int, default=0,
    help="index of webcam on system")
args = vars(ap.parse_args())

# start video stream
print("[INFO] starting video stream thread...")

vs = VideoStream()

vs.Stream = WebcamVideoStream(src=args["webcam"])
vs.start()
print("WORKING FINE")
counter = 0
path = '/home/pi/Desktop/Project'

while True:
    counter = counter + 10
    frame = vs.read()

    #cv2.putText(frame, "STAY STILL!", (10, 30),
    #cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Frame", frame)
    if ((counter % 10000) == 0):
        cv2.imwrite(os.path.join(path,'\frame{}.jpg'.format(counter/10)), frame)
        cv2.putText(frame, "PICTURE TAKEN!", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        frame = vs.read()
        cv2.imshow("Frame", frame)
        cv2.waitKey(500)


    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()


