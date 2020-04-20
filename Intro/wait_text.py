from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

button1 = browser.find_element_by_id("book")
button1.click()

x = browser.find_element_by_id("input_value")
x = x.text
y = math.log(abs(12 * math.sin(int(x))))

input = browser.find_element_by_id("answer")
input.send_keys(str(y))

button2 = browser.find_element_by_css_selector("#solve")
button2.click()

time.sleep(10)
browser.quit()



