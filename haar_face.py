import numpy as np
import cv2
import time
from settings import *
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('face.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
def find_face(img,face_cascade):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    for (x,y,w,h) in faces:
        roi = img[y:y+h, x:x+w]
    return roi,faces
if __name__=='__main__':
    cap = cv2.VideoCapture(video_source_number)  
    while 1:
        try:
            times=time.time()
            _, img = cap.read()
            img=cv2.flip(img,1);org=img;org=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            img,faces=find_face(img,face_cascade)
            cv2.imshow('img',img)
            cv2.waitKey(1)
#             print(faces[0][0])
            print(1/(time.time()-times))
        except Exception as a:
            print(a)
            cv2.imshow('img',org)
            cv2.waitKey(1)