# 네이버에서 자동으로 서울 날씨 검색하는 코드

import pyautogui
import time
import pyperclip

pyautogui.moveTo(1344, 300, 0.2) # serach bar coordinate
pyautogui.click()
time.sleep(1.0)

pyperclip.copy('서울 날씨') # search keyword
pyautogui.hotkey("ctrl", "v")
time.sleep(1.0)

pyautogui.write(['enter'])
time.sleep(1.0)