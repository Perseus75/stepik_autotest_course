from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
locator = (By.ID, "price")
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element(locator, '$100')
    )
button = browser.find_element(By.ID, "book")
button.click()

check = browser.find_element(By.ID, "input_value")
x = check.text
y = calc(x)
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)
button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
button.click()
time.sleep(35)