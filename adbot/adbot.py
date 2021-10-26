import pyautogui
import time

n = 5
print(pyautogui.size())
print(pyautogui.position())
time.sleep(3)
#infinite loop
while n > 0:
    time.sleep(1)
    #look for adbutton
    try:
        x, y = pyautogui.locateCenterOnScreen('adbutton.png', confidence=0.8)
        pyautogui.moveTo(x, y, duration=1)
        pyautogui.click()
    except:
        pass
    time.sleep(1)
    #look for xbutton
    pyautogui.locateOnScreen('xbutton.png')
    try:
        z, q = pyautogui.locateCenterOnScreen('xbutton.png', confidence=0.6)
        pyautogui.moveTo(z, q, duration=2)
        pyautogui.click(z, q)
    except:
        pass
