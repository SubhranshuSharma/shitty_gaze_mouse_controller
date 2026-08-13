import os
import sys
import time
import atexit
import signal
import pyautogui

# Ensure PyAutoGUI defaults remain active
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

import evdev
from evdev import UInput, ecodes as e

_screen_w, _screen_h = pyautogui.size()

# Internal position accumulator (tracks mouse coordinates purely from dispatched deltas)
_cur_x = _screen_w // 2
_cur_y = _screen_h // 2

# ---------------------------------------------------------
# Virtual Input Setup (/dev/uinput)
# ---------------------------------------------------------
cap = {
    e.EV_REL: [e.REL_X, e.REL_Y],
    e.EV_KEY: [e.BTN_LEFT, e.BTN_RIGHT, e.BTN_MIDDLE],
}

try:
    v_mouse = UInput(cap, name='python-hybrid-gaze-mouse')
except PermissionError:
    print("[!] Missing /dev/uinput permissions. Run once: sudo chmod 666 /dev/uinput")
    sys.exit(1)

time.sleep(0.1)

# ---------------------------------------------------------
# Movement & Click Routines
# ---------------------------------------------------------
def wayland_move(dx, dy, *args, **kwargs):
    global _cur_x, _cur_y
    if v_mouse:
        v_mouse.write(e.EV_REL, e.REL_X, int(dx))
        v_mouse.write(e.EV_REL, e.REL_Y, int(dy))
        v_mouse.syn()

        # Update internal coordinate state for Mode 2 relative offsets
        _cur_x = max(0, min(_screen_w, _cur_x + int(dx)))
        _cur_y = max(0, min(_screen_h, _cur_y + int(dy)))

def wayland_move_to(target_x, target_y, *args, **kwargs):
    target_x = max(0, min(_screen_w, int(target_x)))
    target_y = max(0, min(_screen_h, int(target_y)))
    
    # Calculate offset relative to internally tracked position
    dx = target_x - _cur_x
    dy = target_y - _cur_y
    wayland_move(dx, dy)

def wayland_position():
    return _cur_x, _cur_y

def wayland_click(button='left', *args, **kwargs):
    if not v_mouse:
        return
    btn_code = e.BTN_LEFT if button == 'left' else e.BTN_RIGHT
    v_mouse.write(e.EV_KEY, btn_code, 1)
    v_mouse.syn()
    time.sleep(0.04)
    v_mouse.write(e.EV_KEY, btn_code, 0)
    v_mouse.syn()

def wayland_double_click(*args, **kwargs):
    for _ in range(2):
        wayland_click('left')
        time.sleep(0.06)

# ---------------------------------------------------------
# Cleanup & Lifecycle
# ---------------------------------------------------------
def _cleanup():
    global v_mouse
    if v_mouse:
        try:
            v_mouse.close()
            v_mouse = None
        except Exception:
            pass

atexit.register(_cleanup)
signal.signal(signal.SIGINT, lambda s, f: [_cleanup(), sys.exit(0)])
signal.signal(signal.SIGTERM, lambda s, f: [_cleanup(), sys.exit(0)])

# Patch PyAutoGUI routines
pyautogui.move = wayland_move
pyautogui.moveTo = wayland_move_to
pyautogui.click = wayland_click
pyautogui.doubleClick = wayland_double_click
pyautogui.position = wayland_position
