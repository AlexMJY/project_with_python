# 여러 지역 날씨를 검색 후 캡처 저장하는 코드

import pyautogui
import time
import pyperclip

weather = ['서울 날씨', '시흥 날씨', '청주 날씨', '부산 날씨', '강원도 날씨']

addr_x = 1377 
addr_y = 296
start_x = 1005  
start_y = 317
end_x = 1830
end_y = 817

for region_weather in weather:
    pyautogui.moveTo(addr_x, addr_y, 1)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.write('www.naver.com', interval=0.1)
    pyautogui.write(['enter'])
    time.sleep(1)
    
    pyperclip.copy(region_weather)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.write(['enter'])
    time.sleep(1.0)
    path = f'project\{int(10)}.automouse\{region_weather}.png' 
    pyautogui.screenshot(path, region=(start_x, start_y, end_x-start_x, end_y-start_y))
