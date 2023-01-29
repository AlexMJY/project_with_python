import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# go to naver
browser = webdriver.Chrome()
browser.get("http://naver.com")

# click login button
elem = browser.find_element(By.CLASS_NAME, "link_login")
elem.click()

# enter id, pw
browser.find_element(By.ID, "id").send_keys("naver_id")
browser.find_element(By.ID, "pw").send_keys("naver_pw")

# click login button
browser.find_element(By.ID, "log.login").click()

# enter the id again
time.sleep(3)
browser.find_element(By.ID, "id").clear()
browser.find_element(By.ID, "id").send_keys("my_id")

# html 정보 출력
print(browser.page_source)

# quit browser
# browser.close() # quit current tab
browser.quit() # quit all page

while(True):
    pass