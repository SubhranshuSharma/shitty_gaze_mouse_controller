# shitty_gaze_mouse_controller

https://user-images.githubusercontent.com/84875500/150298236-d684ef93-9afa-47d6-a763-a84d19ad87da.mp4

**install dependencies**: `pip3 install tensorflow opencv-python pyautogui pillow`

run `python3 main.py` script, it will collect data, raise your left eyebrow (raise both if you want, it will ignore right eyebrow), with cv2 window in focus, press s when photo shot is good enough, press any other key to retake photo, after that look up then down then left then right then blink left eye, pressing s each time to save photo, after pressing s, script doesn't give time to look where you are supposed to, so look where you are supposed to and then press s.

after that it should start working, if its under detecting try changing threshold in settings.py the sequence of thresholds is same as data array in settings.py, threshold means how good of a match image should be to be counted as a match if the class you selected is underdetecting try decreasing threshold if its overdetecting try increasing it.