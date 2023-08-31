import numpy as np
import cv2
import time
from settings import *
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
def find_face(img,face_cascade):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    for (x,y,w,h) in faces:
        roi = img[y:y+h, x:x+w]
    return roi,faces
if __name__=='__main__':
    cap = cv2.VideoCapture(video_source_number if video_source_number else 0)  
    while 1:
        try:
            times=time.time()
            _, img = cap.read()
            img=cv2.flip(img,1)
            _,faces=find_face(img,face_cascade)
            for (x,y,w,h) in faces:
                img = img[y:y+h, x:x+w]
            cv2.imshow('img',img)
            cv2.waitKey(1)
#             print('\r',faces[0][0])
            print('\rFPS: ', 1/(time.time()-times), end='',sep='')
        except Exception as a:
            print('\r', a, sep='', end='')
            cv2.imshow('img',img)
            cv2.waitKey(1)