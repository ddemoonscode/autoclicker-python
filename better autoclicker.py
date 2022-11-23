import pyautogui

#how often repeated
for _ in range(50):
    pyautogui.click()

#imports
from pwinput.mouse import Button, Controller

mouse = Controller()

# Press and release
mouse.press(Button.left)

mouse.release(Button.left)