person='abc'
thresholds=[.95,.9,.9,.9,.9,.93]
tsrf=True
#if true only image of eye will be processed may increase accuracy
print_frame_rate=False
print_additive_average_frame_rate=False
cursor_speed=3
auto_correct_threshold=True
auto_correct_left_pixel_limit=.3
auto_correct_right_pixel_limit=.7
auto_correct_up_pixel_limit=.3
auto_correct_down_pixel_limit=.7
delay_after_dclick_or_enable=.2
threshold_correction_rate=.01
auto_threshold_correct_rate=.005
show_left_eye=True
show_left_eyebrow=True
landmarks=[['bros',17,21,19,'1122'],['eye',36,39,37,40],['eye',36,39,37,40],['eye',36,39,37,40],['eye',36,39,37,40],['eye',36,39,37,40]]
data=['bros','up','down','left','right','dclick']
color=[[0,0,0],[0,50,100],[100,50,0],[100,150,200],[200,150,100],[200,0,0]]
correct=['e','u','d','l','r','c']
#select the image widow and press c while running the script to change threshold
steps=['raise your left eyebrow','look up','look down','look left','look right','close left eye']