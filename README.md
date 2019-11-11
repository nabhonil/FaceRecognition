# FaceRecognition
The Following project does Face detection, creating a dataset and training a model and finally doing Face Identification and Recognition. The project is created using Python 3.7 and OpenCV 4.1.2. 

# Want to try it out
1. Install the Python 3.7 and OpenCV 4.1.2 for the windows OS or mac OS whereever you want to run this project.
2. Do the following PIP installs
3. pip install opencv-python 
4. pip install opencv-contrib-python
5. pip install pillow
6. pip install numpy

# About the Code
There is two python files. The purpose of these files are mentioned below:-

1. FaceTraining.py - This code basically does the face detection and whenever you click key "k", it will capture a picture of your face in the gray format and store it in the dataset folder. Take as many as 5 to 6 pictures by pressing the key "k" 5 to 6 times. Once the picture is taken press "ESC" key to exit, while exit it will create a training.yml file which is basically a trainined model of the faces that have been captured. Presently it is assumed that we are training the face for a person named Alex. 

You can execute the code as "python FaceTraining.py"

2 FaceRecognition.py - This code uses the training.yml file does the recognition of the present face that is detected using camera and if the match happens it mentions the Name and also tells the confidence level. So if you want to take a screen shot of the camera which is showing the detection and identification of the Alex, you can press the key "k" and the picture will be saved in the capture folder. Press "ESC" key to exit the program.

You can execute the code as "python FaceRecognition.py"

# Disclaimer
If you see any packages are missing while executing the code, please add it as part of PIP install.
