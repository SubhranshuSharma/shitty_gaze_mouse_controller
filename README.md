# shitty_gaze_mouse_cotroller

https://user-images.githubusercontent.com/84875500/150298236-d684ef93-9afa-47d6-a763-a84d19ad87da.mp4

install tensorflow, cv2, pyautogui, PIL, numpy and run main.py script it will collect data, raise your left eyebrow (raise both if you want it will ignore right eyebrow), press s when photo shot is good enough, press any other key to retake photo, after that look at the camara then down then left then right then blink left eye then blink right eye pressing s each time to save photo, after pressing s script doesnt give time to look where you are supposed to so look where you are supposed to and then press s.

left eyebrow up toggles script between on and off state

new mode added in which script tries to predict exactly which pixel you are looking at, lot of room for improvement like for now script assumes that relation between probability and eye angle is linear. toggle betwnn modes by right eye blink. 

after that it should start working, if its under detecting try changing threshold in settings.py the sequence of thresholds is same as data array in settings.py, you can also change thresholds while script is running by bringing cv2 window into focus (by clicking on it) and then look at the camara while pressing w key then look down while pressing s then look left while pressing a and then look right while pressing d, threshold means how good of a match image should be to be counted as a match if the class you selected is underdetecting try decreasing threshold if its overdetecting try increasing it.

if script is running slower than in video that is because the default setting of tsrf boolian is true in settings.py try making it false.

more detailed instructions coming in no longer than 8 years.

discord server for suggestions or whatever- https://discord.gg/YBuQuHRc59
