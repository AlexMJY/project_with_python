# 날씨 화면 저동 캡처 후 저장하는 코드

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

start_x = 1005  
start_y = 317
end_x = 1830
end_y = 817

pyautogui.screenshot(r'project\10.automouse\seoul_weather.png', region=(start_x, start_y, end_x-start_x, end_y-start_y))