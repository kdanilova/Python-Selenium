from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button = browser.find_element_by_tag_name("button")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element_by_id("input_value")
x = x.text
y = math.log(abs(12 * math.sin(int(x))))

input = browser.find_element_by_id("answer")
input.send_keys(str(y))

button = browser.find_element_by_css_selector(".btn")
button.click()

time.sleep(10)

browser.quit()