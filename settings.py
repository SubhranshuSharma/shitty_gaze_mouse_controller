person='abc'
video_source_number=0
thresholds=[.9,.85,.85,.85,.85,.95,.9]
extra_thresholds=[.85,.85,.85,.85]
#select the image widow and press c while running the script to change threshold
tsrf=True
#if true only image of eye will be processed may increase accuracy
mode=False
print_frame_rate=False
print_additive_average_frame_rate=False
cursor_speed=3
auto_correct_threshold=False
auto_correct_left_pixel_limit=.5
auto_correct_right_pixel_limit=.5
auto_correct_up_pixel_limit=.5
auto_correct_down_pixel_limit=.5
delay_after_dclick_or_enable=.1
threshold_correction_rate=.01
auto_threshold_correct_rate=.01
brightness_correction=False
#brightness_correction doesnt work well
show_left_eye=True
show_left_eyebrow=True
landmarks=[['bros',17,21,19,'1122'],['eye',36,39,37,40],['eye',36,39,37,40],['eye',36,39,37,40],['eye',36,39,37,40],['eye',36,39,37,40],['eye',42,45,43,46]]
data=['bros','up','down','left','right','dclick','r_close']
color=[[0,0,0],[0,50,100],[100,50,0],[100,150,200],[200,150,100],[200,0,0],[0,0,0]]
extra_colors=[[0,50,100],[100,50,0],[100,150,200],[200,150,100]]
correct=['e','u','d','l','r','c','m']
steps=['raise your left eyebrow','look up','look down','look left','look right','close left eye','close right eye']



if tsrf==False and brightness_correction==True:
    brightness_correction=False
    print("brightness correction can't work with tsrf disabled as it takes cropped image from tensorflow and makes its average brightness equal to data")
    print("turning off brightness correction")
if tsrf==False and mode==True:
    mode==False;print('2 modes only when tsrf enabled')