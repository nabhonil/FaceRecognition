import numpy as py
import cv2 as cv
import os as os
from PIL import Image

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml') 

cap = cv.VideoCapture(0) 
cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)
total = 0

recognizer = cv.face.LBPHFaceRecognizer_create()
datapath = "dataset"
ID = 1

def createTrainingData(path):
    imagePaths = [os.path.join(datapath, f) for f in os.listdir(datapath)]
    faces = []
    IDs = []
    for imagePath in imagePaths:
        print (imagePath)
        if (imagePath.lower().endswith('.png')):
            imageFace = Image.open(imagePath).convert('L')
            faceNP = py.array(imageFace, 'uint8')
            faces.append(faceNP)
            IDs.append(ID)
            cv.imshow("Adding faces for training", faceNP)
            cv.waitKey(10)

    return py.array(IDs), faces
  
# loop runs if capturing has been initialized. 
while 1:  
  
    # reads frames from a camera 
    ret, img = cap.read()  
  
    # convert to gray scale of each frames 
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
  
    # Detects faces of different sizes in the input image 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
  
    for (x,y,w,h) in faces: 
        # To draw a rectangle in a face  
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)  
  
    # Display an image in a window 
    cv.imshow('Video', img) 
  
    # Wait for Esc key to stop 
    key = cv.waitKey(30) & 0xff

    # if the `k` key was pressed, write the *original* frame to disk
	# so we can later process it and use it for face recognition
    if key == ord("k"):
        filepath = os.path.sep.join(["dataset","{}.png".format(str(total).zfill(5))])
        cv.imwrite(filepath, gray[y:y+h, x:x+w])
        total += 1

    elif key == 27: 
        break
  
# Close the window 
cap.release() 

# Trainned yml file createion
IDList, faceList = createTrainingData(datapath)
recognizer.train(faceList, IDList)
recognizer.save("trainingData.yml")

# De-allocate any associated memory usage 
cv.destroyAllWindows()
