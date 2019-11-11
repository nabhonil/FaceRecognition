import numpy as py
import cv2 as cv
import os as os

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)
recognizer = cv.face.LBPHFaceRecognizer_create()

recognizer.read("trainingData.yml")
id = 0
fontface = cv.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (0, 255, 0)
thickness = 2

while 1:
    ret, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id, loss = recognizer.predict(gray[y:y+h, x:x+w])
        name = ''
        if (loss < 50):
            conf = "  {0}%".format(round(100 - loss))
            if (id==1):
                name = "Alex"
        else:
            name = "Unknown"
            conf = ""
        
        cv.putText(img,name + " " + str(conf),(x,y+h),fontface, fontscale, fontcolor, thickness)

    cv.imshow('Video', img)

    # Wait for Esc key to stop 
    key = cv.waitKey(30) & 0xff

    if key == ord("k"):
        filepath = os.path.sep.join(["capture","test.png"])
        cv.imwrite(filepath, img)
    elif key == 27: 
        break

cap.release 

cv.destroyAllWindows()