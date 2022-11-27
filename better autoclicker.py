import pyautogui
import time

#input
num = int(input('How often?: '))

#Time between answering and clicking
time.sleep(3)

#how often repeated
for _ in range(num):
    pyautogui.click()