from settings import *
import os ,pyautogui
pwdpath=os.getcwd()
if not os.path.exists(f'{pwdpath}/profiles/{person}'):
    os.makedirs(f'{pwdpath}/profiles/{person}')
pwdpath=os.getcwd()
import numpy as np
import cv2
from frontal_face import *
cap=cv2.VideoCapture(video_source_number)
cap.set(cv2.CAP_PROP_BUFFERSIZE,1)
i=0
while 1:
    try:
        ret, img = cap.read();ret, img = cap.read()
        org=img = cv2.flip(img,1)
        marks,_=findc(img)
        r_=img=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        clas,x1,x2,y1,y2 = landmarks[i]
        if landmarks[i][0]=='bros':
            lx1=int(marks[x1][0]); lx2=int(marks[x2][0])
            ly1=int(marks[y1][1]);ly2=int((marks[landmarks[0][int(landmarks[0][4][0])]][1]+marks[landmarks[0][int(landmarks[0][4][2])]][1])/2)
            img=org[ly1-15:ly2+5,lx1-5:lx2+10]
            img=cv2.resize(img,(50,25))
        elif landmarks[i][0]=='eye':
            lx1=int(marks[x1][0]); lx2=int(marks[x2][0])
            ly1=int(marks[y1][1]);ly2=int(marks[y2][1])
            img=org[ly1-10:ly2+10,lx1-10:lx2+15]
            if i in [1,2,3,4]:
                lx1=int(marks[42][0]); lx2=int(marks[45][0])
                ly1=int(marks[43][1]);ly2=int(marks[46][1])
                r_=org[ly1-10:ly2+10,lx1-10:lx2+15]
                r_=cv2.resize(r_,(50,25))
            img=cv2.resize(img,(50,25))
        if brightness_correction==True:    
                img=img*(60/np.average(img));img=img.astype('uint8')
        print(f'{clas} brightness:',np.average(img))
        if brightness_correction==True:    
            img=img*(60/np.average(img));img=img.astype('uint8')
            r_=r_*(60/np.average(r_));r_=r_.astype('uint8')
#         img=cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
        cv2.imshow('img',img)
        sizex,sizey=pyautogui.size()
        if i in [1,2,3,4]:
            cv2.imshow('right eye',r_);cv2.moveWindow('right eye',int((sizex/2)-150),int(sizey/2)-150)
        if i==5:cv2.destroyWindow('right eye')
        print(steps[i])
        print('press s to save anything else to retake')
        if cv2.waitKey(0)==ord('s'):
            img=cv2.resize(img,(50,25))
            cv2.imwrite(f'{pwdpath}/profiles/{person}/{data[i]}.jpg',img)
            if i in [1,2,3,4]:cv2.imwrite(f'{pwdpath}/profiles/{person}/r_{data[i]}.jpg',r_)
            i+=1
        if i==len(data):
            cap.release()
            cv2.destroyAllWindows()
            break
    except Exception as a:
        print(a)
