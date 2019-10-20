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
import io
import os
from google.cloud import vision
from google.cloud.vision import types

def genericClothing():
        generic = ['Raincoat', 'Coat', 'Jacket', 'Shirt', 'T-shirt', 'Trousers', 'Jeans', 'Pants', 'Shorts']
        return generic
    
def detectImage():
    client = vision.ImageAnnotatorClient()
    
    file_name = os.path.join(os.path.dirname(__file__),'clothing1.jpg')

    with io.open(file_name,'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    #response2 = client.image_properties(image=image)
    labels = response.label_annotations

    likelyclothes = ['Raincoat', 'Coat', 'Jacket', 'Shirt', 'T-shirt', 'Trousers', 'Jeans', 'Pants', 'Shorts']
    labelslist = []

    for label in labels:
        labelslist.append(str(label.description))

    

    #string value
    length = len(labelslist)
    for i in likelyclothes:
        for j in labelslist:
            if i == j:    
                return i
                break

def detectImage2():
    client = vision.ImageAnnotatorClient()
    
    file_name = os.path.join(os.path.dirname(__file__),'clothing2.jpg')

    with io.open(file_name,'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    #response2 = client.image_properties(image=image)
    labels = response.label_annotations

    likelyclothes = ['Raincoat', 'Coat', 'Jacket', 'Shirt', 'T-shirt', 'Trousers', 'Jeans', 'Pants', 'Shorts']
    labelslist = []

    for label in labels:
        
        labelslist.append(str(label.description))

    

    #string value
    length = len(labelslist)
    for i in likelyclothes:
        for j in labelslist:
            if i == j:    
                return i
                break
            
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="mapper.json"

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
    counter = counter + 5
    frame = vs.read()

    #cv2.putText(frame, "STAY STILL!", (10, 30),
    #cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Frame", frame)
    if ((counter % 10000) == 0):
        cv2.imwrite(os.path.join(path,'clothing{}.jpg'.format(counter/10000)), frame)
        cv2.putText(frame, "PICTURE TAKEN!", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        frame = vs.read()
        cv2.imshow("Frame", frame)
        cv2.waitKey(500)


    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()

a = detectImage()
b = detectImage2()
#creates array of two pieces of clothing you are deciding to wear
wardrobe = [a, b]
addresses = ['clothing1.jpg', 'clothing2.jpg'] 
print(wardrobe)


