import pyautogui
import time
import keyboard
import random
import win32api, win32con

pianoCount = 0
delay = 0.03

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(delay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    pianoCount += 1
    if pianoCount == 999 :
        delay = 0.02
    elif pianoCount == 3000 :
        delay = 0.01
    if pyautogui.pixel(659,435)[0] < 2:
        click(659,435)
    if pyautogui.pixel(743,435)[0] < 2:
        click(743,435)
    if pyautogui.pixel(824,435)[0] < 2:
        click(824,435)
    if pyautogui.pixel(909,435)[0] < 2:
        click(909,435)
    print(str(delay))
