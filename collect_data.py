import os
pwdpath=os.getcwd()
import numpy as np
import cv2, time
from frontal_face import *
from settings import *
print('collecting data')
a='bros';data=['bros','up','down','left','right','dclick']
lighting=[]
if not os.path.exists(f'{pwdpath}/profiles/{person}'):
    os.makedirs(f'{pwdpath}/profiles/{person}')
cap=cv2.VideoCapture(video_source_number if video_source_number else 0)
cap.set(cv2.CAP_PROP_BUFFERSIZE,1)
i=0
while 1:
    try:
        times=time.time()
        ret, img = cap.read();ret, img = cap.read()
        org=img = cv2.flip(img,1)
        marks=findc(cap)
        img=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        if a=='bros':
            lbx1=int(marks[17][0]); lbx2=int(marks[21][0])
            lby1=int(marks[19][1]); lby2=int((marks[17][1]+marks[17][1])/2)
            img=img[lby1-15:lby2+5,lbx1-5:lbx2+10]
        if a=='eye':
            lx1=int(marks[36][0]); lx2=int(marks[39][0])
            ly1=int(marks[37][1]); ly2=int(marks[40][1])
            img=img[ly1-10:ly2+10,lx1-10:lx2+15]
        eye=cv2.resize(img, (0,0),fx=5,fy=5)
        print(i,':',np.average(img))
        lighting.append(np.average(img))
        cv2.imshow('img',img)
        print(f'{steps[i]}')
        print('press s to save and anything else to retake photo')
        if cv2.waitKey(0)==ord('s'):
            cv2.imwrite(f'{pwdpath}/profiles/{person}/{data[i]}.jpg',img)
            i+=1;a='eye'
        else:pass
        if i==len(data):
            cap.release()
            cv2.destroyAllWindows()
            break
    except Exception as a:
        print(a)
# eye=img=img[ly1-int(1.5*abs(ly1-ly2)):ly2+int(1*abs(ly1-ly2)),lx1-int(.4*abs(lx1-lx2)):lx2+int(.3*abs(lx1-lx2))]
for p in range(len(data)):
    x=cv2.imread(f'{pwdpath}/profiles/{person}/{data[p]}.jpg',0)
    if p==0:
        factor=lighting[0]/np.average(x)
    else:
        factor=60.2/np.average(x)
    x=cv2.resize(x,(55,27))
    x=x*factor
    x=x.astype('uint8')
    cv2.imwrite(f'{pwdpath}/profiles/{person}/{data[p]}.jpg',x)
current_lighting=((sum(lighting)-lighting[0])/(len(data)-1))
print(current_lighting)