import pyautogui
import time

#input
num = int(input('How often?: '))

#Time till start after input
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('Go')

#how often repeated
for _ in range(num):
    pyautogui.click()