import pyautogui
import keyboard
import time
import os
sl = 0
sl2 = 0


def on_release(key):
    global sl, sl2
    if key.name == 'print screen' and key.event_type == 'down':
        while str(sl) + '_screen.png' in os.listdir():
            sl += 1
        pyautogui.screenshot(str(sl) + '_screen.png')
    if key.name == "м" and key.event_type == 'down':
        x, y = pyautogui.position()
        pyautogui.mouseDown(x, y, button='middle')
        time.sleep(10)
        """pyinstaller --onefile -w main.py"""
        x, y = pyautogui.position()
        pyautogui.mouseUp(x, y, button='middle')
    if key.name == "ё" and key.event_type == 'down':
        with open('mus.txt', 'r', encoding='Windows-1251') as file:
            data = file.readlines()
        ti, eny = data[sl2 % len(data)].split('#')
        sl2 += 1
        for i in eny:
            if i != '.':
                if i.isupper():
                    keyboard.press_and_release('shift+' + i.lower())
                elif i == '!':
                    keyboard.press_and_release('esc')
                else:
                    keyboard.press_and_release(i)
            time.sleep(float(ti))



keyboard.hook(on_release)
keyboard.wait()