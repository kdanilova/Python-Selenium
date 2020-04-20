from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

button = browser.find_element_by_css_selector(".btn")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = browser.find_element_by_id("input_value")
x = x.text
y = math.log(abs(12 * math.sin(int(x))))

input = browser.find_element_by_id("answer")
input.send_keys(str(y))

button = browser.find_element_by_css_selector(".btn")
button.click()

time.sleep(10)
browser.quit()