from settings import *
import os
pwdpath=os.getcwd()
if not os.path.exists(f'{pwdpath}/profiles/{person}'):
    os.makedirs(f'{pwdpath}/profiles/{person}')
pwdpath=os.getcwd()
import numpy as np
import cv2
from frontal_face import *
a='bros'
# data=['bros','up','down','left','right','dclick']
cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE,1)
i=0
while 1:
    try:
        ret, img = cap.read();ret, img = cap.read()
        org=img = cv2.flip(img,1)
        marks,_=findc(img)
        img=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        if a=='bros':
            lbx1=int(marks[17][0]); lbx2=int(marks[21][0])
            lby1=int(marks[19][1]); lby2=int((marks[17][1]+marks[17][1])/2)
            img=img[lby1-15:lby2+5,lbx1-5:lbx2+10]
        if a=='eye':
            lx1=int(marks[36][0]); lx2=int(marks[39][0])
            ly1=int(marks[37][1]); ly2=int(marks[40][1])
            img=img[ly1-10:ly2+10,lx1-10:lx2+15]
        print(f'{a} brightness:',np.average(img))
#         img=img*(60/np.average(img));img=img.astype('uint8')
#         img=cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
        cv2.imshow('img',img)
        print(steps[i])
        print('press s to save anything else to retake')
        if cv2.waitKey(0)==ord('s'):
            img=cv2.resize(img,(50,25))
            cv2.imwrite(f'{pwdpath}/profiles/{person}/{data[i]}.jpg',img)
            i+=1
        if i==1:
            a='eye'
        else:pass
        if i==len(data):
            cap.release()
            cv2.destroyAllWindows()
            break
    except Exception as a:
        print(a)
