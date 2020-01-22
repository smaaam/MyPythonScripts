import pyautogui, time

pyautogui.doubleClick(110,100)
time.sleep(.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
pyautogui.press('enter')
pyautogui.moveTo(1380,300, duration = .5)
pyautogui.click()
