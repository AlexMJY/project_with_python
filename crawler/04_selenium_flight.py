from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/"
browser.get(url)

ad = browser.find_element(By.LINK_TEXT, "한 달간 안보기").click()


while True:
    pass