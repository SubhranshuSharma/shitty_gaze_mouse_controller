import os
pwdpath=os.getcwd()
if not os.path.isfile(f'{pwdpath}/profiles/abc/dclick.jpg'):
    from collect_data import *
else:
    current_lighting=100
    if input('collect data again?(y/enter):')=='y':
        from collect_data import *
data=['bros','up','down','left','right','dclick']
color=[[0,0,0],[0,50,100],[100,50,0],[100,150,200],[200,150,100],[200,0,0]]
thresholds=[.9,.9,.9,.9,.9,.9]
import math, time, cv2, pyautogui
import numpy as np
from settings import *
f_rate=[];x=[];locc=[]
pyautogui.FAILSAFE = False; pyautogui.PAUSE=0
enable=True
cap = cv2.VideoCapture(video_source_number if video_source_number else 0)
for i in range(len(data)):
    y = cv2.imread(f'{pwdpath}/profiles/{person}/{data[i]}.jpg',0)
    w, h = y.shape[::-1]
    x.append(y)
while 1:
        times=time.time()
        ret, img = cap.read()
        org=img = cv2.flip(img,1)
        img=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img=img*60.2/current_lighting
        img=img.astype('uint8')
        for i in range(len(data)):
            prob = cv2.matchTemplate(img,x[i],cv2.TM_CCOEFF_NORMED)
            loc = np.where(prob >= thresholds[i])
            locc.append(loc)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(org, pt, (pt[0] + w, pt[1] + h), (color[i][0],color[i][1],color[i][2]), 2)
        if len(locc[0][0])>0:
            enable = not enable
            cap.set(cv2.CAP_PROP_BUFFERSIZE,1);ret, img = cap.read()
            print(enable)
            time.sleep(.2);cap.set(cv2.CAP_PROP_BUFFERSIZE,4)
        if len(locc[1][0])>0 and enable:
            pyautogui.move(0, -3)
        if len(locc[2][0])>0 and enable:
            pyautogui.move(0, 3)
        if len(locc[3][0])>0 and enable:
            pyautogui.move(-3, 0)
        if len(locc[4][0])>0 and enable:
            pyautogui.move(3,0)
        if len(locc[5][0])>0 and enable:
            pyautogui.doubleClick()
            cap.set(cv2.CAP_PROP_BUFFERSIZE,1);ret, img = cap.read()
            print('dc')
            time.sleep(.2);cap.set(cv2.CAP_PROP_BUFFERSIZE,4)
        cv2.imshow('img',org)
        cv2.waitKey(1)
        f_rate.append(1/(time.time()-times))
        if print_frame_rate==True:
            print('fr:',1/(time.time()-times))
        elif print_additive_average_frame_rate==True:
            print('afr:',sum(f_rate)/len(f_rate))
        locc=[]