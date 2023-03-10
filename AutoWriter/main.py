import pyautogui
import time
from random import *
import parser as p
var=0
time.sleep(5) #to open the application for autotype
with open('p1.txt', 'r') as file:
    data=file.read()
    data=p.parse(data)
    print(data)
    for x in data:
        for z in x:
            if(z=='{'):
                var+=1
            randomin=randint(1,30)
            if(p.israndomrandom(randomin) and z.isalpha()):
                pyautogui.typewrite(z.upper())
                pyautogui.hotkey('backspace')
            time.sleep(randomin/100)
            pyautogui.typewrite(z)
pyautogui.hotkey('pgdn')
for x in range(0,var+1):
    pyautogui.hotkey('backspace')
