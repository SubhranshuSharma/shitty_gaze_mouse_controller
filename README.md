# shitty_gaze_mouse_cotroller

https://user-images.githubusercontent.com/84875500/150298236-d684ef93-9afa-47d6-a763-a84d19ad87da.mp4

install tensorflow, cv2, pyautogui, PIL, numpy and run main.py script it will collect data, raise your left eyebrow (raise both if you want it will ignore right eyebrow), press s when photo shot is good enough, press any other key to retake photo, after that look up then down then left then right then blink pressing s each time to save photo, after pressing s script doesnt give time to look where you are supposed to so look where you are supposed to and then press s.

after that it should start working, if its under detecting try changing threshold in settings.py the sequence of thresholds is same as data array in settings.py, you can also change thresholds while script is running by bringing cv2 window into focus (by clicking on it) and then pressing c then it will ask which function is not working then u can bring terminal into focus and select from options and press enter then it will ask if you have to increase or decrease threshold, threshold means how good of a match image should be to be counted as a match if the class you selected is underdetecting try decreasing threshold if its overdetecting try increasing it.

if script is running slower than in video that is because the default setting of tsrf boolian is true in settings.py try making it false.

more detailed instructions coming in no longer than 8 years.
