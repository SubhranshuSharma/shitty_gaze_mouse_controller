import os
pwdpath=os.getcwd()
from settings import *
from PIL import ImageGrab
from haar_face import *
if tsrf==True:
    from frontal_face import *
if not os.path.isfile(f'{pwdpath}/profiles/{person}/dclick.jpg'):
    from collect_data import *
else:
    if input('collect new data?(y/enter)')=='y':
        from collect_data import *
    else:pass
data.extend(['r_up','r_down','r_left','r_right'])
thresholds.extend(extra_thresholds)
color.extend(extra_colors)
for i in range(4):
    landmarks.append(['eye',42,45,43,46])
# data=['bros','up','down','left','right','dclick']
# color=[[0,0,0],[0,50,100],[100,50,0],[100,150,200],[200,150,100],[200,0,0]]
# thresholds=[.95,.85,.85,.85,.85,.9]
import math, time, cv2, pyautogui
import numpy as np;from numpy import interp
f_rate=[];x=[];locc=[];probabilities=[];r_min_x_prob=min_x_prob=r_max_x_prob=max_x_prob=r_last_max_x_prob=last_max_x_prob=r_last_min_x_prob=last_min_x_prob=r_min_y_prob=min_y_prob=r_max_y_prob=max_y_prob=r_last_max_y_prob=last_max_y_prob=r_last_min_y_prob=last_min_y_prob=r_m2x=m2x=r_m2y=m2y=0
pyautogui.FAILSAFE = False; pyautogui.PAUSE=0
enable=True;sizex,sizey=pyautogui.size()
cap = cv2.VideoCapture(video_source_number)
# loading saved images 
for i in range(len(data)):
    y = cv2.imread(f'{pwdpath}/profiles/{person}/{data[i]}.jpg',0)
    w, h = y.shape[::-1]
    x.append(y)
# function to crop eyes and eyebrows out of frame
def tnsf(img,landmarks):
    images=[]
    marks,img=findc(img)
    i=0
    org=img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    for cls,x1,x2,y1,y2 in landmarks:
        if landmarks[i][0]=='bros':
            lx1=int(marks[x1][0]); lx2=int(marks[x2][0])
            ly1=int(marks[y1][1]);ly2=int((marks[landmarks[0][int(landmarks[0][4][0])]][1]+marks[landmarks[0][int(landmarks[0][4][2])]][1])/2)
            img=org[ly1-15:ly2+5,lx1-5:lx2+10]
            img=cv2.resize(img,(50,25))
            if brightness_correction==True:    
                img=img*(60/np.average(img));img=img.astype('uint8')
        elif landmarks[i][0]=='eye':
            lx1=int(marks[x1][0]); lx2=int(marks[x2][0])
            ly1=int(marks[y1][1]);ly2=int(marks[y2][1])
            img=org[ly1-10:ly2+10,lx1-10:lx2+15]
            img=cv2.resize(img,(50,25))
            if brightness_correction==True:    
                img=img*(60/np.average(img));img=img.astype('uint8')
#         img=cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
        images.append(img)
        if i==(len(data)-1):
            images=np.asarray(images,dtype=np.uint8)
        i+=1
    return images 
while 1:
    try:
        times=time.time()
        ret, img = cap.read()
        org=img = cv2.flip(img,1)
        if tsrf==False:
            try:
                img,faces=find_face(img,face_cascade)
            except:img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);faces=[[0,0]]
            images=[]
            for i in range(len(data)):
                images.append(img)
            images=np.asarray(images,dtype=np.uint8)
        if tsrf==True:
            images=tnsf(img,landmarks);faces=[[0,0]]
#       compares images cropped from live feed with saved images and applies threshold 
        for i in range(len(data)):
            prob = cv2.matchTemplate(images[i],x[i],cv2.TM_CCOEFF_NORMED)
            loc = np.where(prob >= thresholds[i])
            locc.append(loc)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(org, (pt[0]+faces[0][0],pt[1]+faces[0][1]), (pt[0]+faces[0][0] + w, pt[1]+faces[0][1] + h), (color[i][0],color[i][1],color[i][2]), 2)
            if tsrf==True:
                probability=np.average(prob)
            # if tsrf==False:
            #     probability=np.average(prob[pt[1]+faces[0][1]:pt[1]+faces[0][1]+h,pt[0]+faces[0][0]:pt[0]+faces[0][0]+w])
            if tsrf==True:
                probabilities.append(probability)
#       tracks minimum probability number and max probability number
        if tsrf==True:
            if probabilities[4]-probabilities[3]<0 and last_min_x_prob>probabilities[4]-probabilities[3]:
                last_min_x_prob=min_x_prob=probabilities[4]-probabilities[3]
            if probabilities[4]-probabilities[3]>0 and last_max_x_prob<probabilities[4]-probabilities[3]:
                last_max_x_prob=max_x_prob=probabilities[4]-probabilities[3]
            if probabilities[2]-probabilities[1]<0 and last_min_y_prob>probabilities[2]-probabilities[1]:
                last_min_y_prob=min_y_prob=probabilities[2]-probabilities[1]
            if probabilities[2]-probabilities[1]>0 and last_max_y_prob<probabilities[2]-probabilities[1]:
                last_max_y_prob=max_y_prob=probabilities[2]-probabilities[1]
            if probabilities[len(data)-1]-probabilities[len(data)-2]<0 and r_last_min_x_prob>probabilities[len(data)-1]-probabilities[len(data)-2]:
                r_last_min_x_prob=r_min_x_prob=probabilities[len(data)-1]-probabilities[len(data)-2]
            if probabilities[len(data)-1]-probabilities[len(data)-2]>0 and r_last_max_x_prob<probabilities[len(data)-1]-probabilities[len(data)-2]:
                r_last_max_x_prob=r_max_x_prob=probabilities[len(data)-1]-probabilities[len(data)-2]
            if probabilities[len(data)-3]-probabilities[len(data)-4]<0 and r_last_min_y_prob>probabilities[len(data)-3]-probabilities[len(data)-4]:
                r_last_min_y_prob=r_min_y_prob=probabilities[len(data)-3]-probabilities[len(data)-4]
            if probabilities[len(data)-3]-probabilities[len(data)-4]>0 and r_last_max_y_prob<probabilities[len(data)-3]-probabilities[len(data)-4]:
                r_last_max_y_prob=r_max_y_prob=probabilities[len(data)-3]-probabilities[len(data)-4]
        if len(locc[0][0])>0:
            enable = not enable
            cap.set(cv2.CAP_PROP_BUFFERSIZE,1);ret, img = cap.read()
            print('enable:',enable)
            time.sleep(delay_after_dclick_or_enable);cap.set(cv2.CAP_PROP_BUFFERSIZE,4)
        mousex,mousey=pyautogui.position()
#       displays screen in small windows
        if mode==False:
            box = (mousex-100,mousey-100,mousex+100,mousey+100)
            cursor=np.asarray(ImageGrab.grab(box),dtype=np.uint8)
            cursor=cv2.cvtColor(cursor,cv2.COLOR_BGR2RGB)
            cursor=cv2.resize(cursor,(120,120))
            cv2.imshow('cursoru',cursor);cv2.imshow('cursord',cursor);cv2.imshow('cursorl',cursor);cv2.imshow('cursorr',cursor)
            cv2.moveWindow('cursoru',int(sizex/2)-120,0)
            cv2.moveWindow('cursord',int(sizex/2)-120,sizey-200)
            cv2.moveWindow('cursorl',0,int(sizey/2)-100)
            cv2.moveWindow('cursorr',sizex-300,int(sizey/2)-100)
        if mode==True:
            cv2.destroyAllWindows()
        if auto_correct_threshold==True:
            if len(locc[7][0])>0 and len(locc[8][0])>0:
                if mousey<(sizey*auto_correct_up_pixel_limit) or mousey>(sizey*auto_correct_down_pixel_limit):
                    print('auto correcting threshold')
                    thresholds[7]=thresholds[7]+auto_threshold_correct_rate;thresholds[8]=thresholds[8]+auto_threshold_correct_rate
            if len(locc[1][0])>0 and len(locc[2][0])>0:
                if mousey<(sizey*auto_correct_up_pixel_limit) or mousey>(sizey*auto_correct_down_pixel_limit):
                    print('auto correcting threshold')
                    thresholds[1]=thresholds[1]+auto_threshold_correct_rate;thresholds[2]=thresholds[2]+auto_threshold_correct_rate
            if len(locc[9][0])>0 and len(locc[10][0])>0:
                if mousey<(sizey*auto_correct_up_pixel_limit) or mousey>(sizey*auto_correct_down_pixel_limit):
                    print('auto correcting threshold')
                    thresholds[9]=thresholds[9]+auto_threshold_correct_rate;thresholds[10]=thresholds[10]+auto_threshold_correct_rate   
            if len(locc[3][0])>0 and len(locc[4][0])>0:
                if mousex<(sizex*auto_correct_left_pixel_limit) or mousex>(sizex*auto_correct_right_pixel_limit):
                    thresholds[3]=thresholds[3]+auto_threshold_correct_rate;thresholds[4]=thresholds[4]+auto_threshold_correct_rate
                    print('auto correcting threshold')
        if tsrf==False:mode=False
#       takes action according to result from templet matching
        if (len(locc[1][0])>0 or (len(locc[7][0])>0) and len(locc[7][0])>0) and enable and mode==False:
#             print('up')
#             cv2.moveWindow('cursor',int(sizex/2)-20,0)
            cv2.destroyWindow('cursord')
            for i in range(cursor_speed):
                pyautogui.move(0, -1)
        if (len(locc[2][0])>0 or len(locc[8][0])>0) and enable and mode==False:
#             print('down')
#             cv2.moveWindow('cursor',int(sizex/2)-20,sizey-20)
            cv2.destroyWindow('cursoru')
            for i in range(cursor_speed):
                pyautogui.move(0, 1)
        if (len(locc[3][0])>0 or len(locc[9][0])>0) and enable and mode==False:
#             print('left')
#             cv2.moveWindow('cursor',0,int(sizey/2)-20)
            cv2.destroyWindow('cursorr')
            for i in range(cursor_speed):
                pyautogui.move(-1, 0)
        if (len(locc[4][0])>0 or len(locc[10][0])>0) and enable and mode==False:
#             print('right')
#             cv2.moveWindow('cursor',sizex-100,int(sizey/2))
            cv2.destroyWindow('cursorl')
            for i in range(cursor_speed):
                pyautogui.move(1,0)
        if len(locc[5][0])>0 and enable and len(locc[6][0])==0:
            pyautogui.doubleClick()
            print('dc')
            cap.set(cv2.CAP_PROP_BUFFERSIZE,1);ret, img = cap.read()
            time.sleep(delay_after_dclick_or_enable);cap.set(cv2.CAP_PROP_BUFFERSIZE,4)
        if len(locc[6][0])>0 and enable and tsrf and not len(locc[5][0])>0:
            mode=not mode
            print(f'mode:{mode}')
            cap.set(cv2.CAP_PROP_BUFFERSIZE,1);ret, img = cap.read()
            time.sleep(delay_after_dclick_or_enable);cap.set(cv2.CAP_PROP_BUFFERSIZE,4)
#       exact pixel pridiction
        if mode==True and enable and tsrf:
            m2x=interp(probabilities[4]-probabilities[3],[min_x_prob,max_x_prob],[0,sizex])
            m2y=interp(probabilities[2]-probabilities[1],[min_y_prob,max_y_prob],[0,sizey])
            r_m2x=interp(probabilities[len(data)-1]-probabilities[len(data)-2],[r_min_x_prob,r_max_x_prob],[0,sizex])
            r_m2y=interp(probabilities[len(data)-3]-probabilities[len(data)-4],[r_min_y_prob,r_max_y_prob],[0,sizey])
            pyautogui.moveTo(int((m2x+r_m2x)/2),int((m2y+r_m2y)/2))
        if tsrf==True and not mode:
            if show_left_eye==True:
                cv2.imshow('left eye',images[1])
            if show_left_eyebrow==True:    
                cv2.imshow('left eyebrow',images[0])
        if tsrf==False:
            cv2.imshow('org',org)
#       threshold correction by arrow keys
        if cv2.waitKey(1)==82 and (len(locc[1][0])==0 or len(locc[len(data)-4][0])==0 or len(locc[2][0])>0 or len(locc[3][0])>0 or len(locc[4][0])>0 or len(locc[len(data)-3][0])>0 or len(locc[len(data)-2][0])>0 or len(locc[len(data)-1][0])>0):
            print('correcting up',thresholds)
            for i in [1,len(data)-4]:
                if len(locc[i][0])==0:thresholds[i]-=threshold_correction_rate
            for i in [2,3,4,len(data)-3,len(data)-2,len(data)-1]:
                if len(locc[i][0])>0:thresholds[i]+=threshold_correction_rate
        if cv2.waitKey(1)==84 and (len(locc[2][0])==0 or len(locc[len(data)-3][0])==0 or len(locc[1][0])>0 or len(locc[3][0])>0 or len(locc[4][0])>0 or len(locc[len(data)-4][0])>0 or len(locc[len(data)-2][0])>0 or len(locc[len(data)-1][0])>0):
            print('correcting down',thresholds)
            for i in [2,len(data)-3]: 
                if len(locc[i][0])==0:thresholds[i]-=threshold_correction_rate
            for i in [1,3,4,len(data)-4,len(data)-2,len(data)-1]:
                if len(locc[i][0])>0:thresholds[i]+=threshold_correction_rate   
        if cv2.waitKey(1)==81 and (len(locc[3][0])==0 or len(locc[len(data)-2][0])==0 or len(locc[1][0])>0 or len(locc[2][0])>0 or len(locc[4][0])>0 or len(locc[len(data)-4][0])>0 or len(locc[len(data)-3][0])>0 or len(locc[len(data)-1][0])>0):
            print('correcting left',thresholds)
            for i in [3,len(data)-2]:
                if len(locc[i][0])==0:thresholds[i]-=threshold_correction_rate
            for i in [1,2,4,len(data)-4,len(data)-3,len(data)-1]:
                if len(locc[i][0])>0:thresholds[i]+=threshold_correction_rate
        if cv2.waitKey(1)==83 and (len(locc[4][0])==0 or len(locc[len(data)-1][0])==0 or len(locc[1][0])>0 or len(locc[2][0])>0 or len(locc[3][0])>0 or len(locc[len(data)-4][0])>0 or len(locc[len(data)-3][0])>0 or len(locc[len(data)-2][0])>0):
            print('correcting right',thresholds)
            for i in [4,len(data)-1]:
                if len(locc[i][0])==0:thresholds[i]-=threshold_correction_rate
            for i in [1,2,3,len(data)-4,len(data)-4,len(data)-2]:
                if len(locc[i][0])>0:thresholds[i]+=threshold_correction_rate
        f_rate.append(1/(time.time()-times))
        if print_frame_rate==True:
            print('fr:',1/(time.time()-times))
        if print_additive_average_frame_rate==True:
            print('afr:',sum(f_rate)/len(f_rate))
        locc=[];probabilities=[]
    except Exception as a:
        print(a)
        