# import pyautogui ,cv2
# x,y=pyautogui.position()
# img=pyautogui.screenshot(region=(0,0, 300, 400))
from PIL import ImageGrab
import cv2
import numpy as np
box = (0,0,1166,679) #Upper left and lower right corners
cursor=np.asarray(ImageGrab.grab(box),dtype=np.uint8)
cursor=cv2.cvtColor(cursor,cv2.COLOR_BGR2RGB)
cv2.imshow('n',cursor)
cv2.waitKey(0)