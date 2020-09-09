from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


# X:  762 Y:  742 RGB: (  0,   0,   0)

# X:  868 Y:  742 RGB: (  0,   0,   0)

# X: 1024 Y:  742 RGB: (  0,   0,   0)

# X: 1150 Y:  742 RGB: (  0,   0,   0)


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(868,742)[0] == 0:            #[0] checks for red [1] for green [2] for blue
        click(868,742)

    if pyautogui.pixel(1024,742)[0] == 0:            #[0] checks for red [1] for green [2] for blue
        click(1024,742)

    if pyautogui.pixel(762,742)[0] == 0:            #[0] checks for red [1] for green [2] for blue
        click(762,742)
    
    if pyautogui.pixel(1150,742)[0] == 0:            #[0] checks for red [1] for green [2] for blue
        click(1150,742)
