from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input = browser.find_element_by_id("answer")
checkbox = browser.find_element_by_id("robotCheckbox")
radiobutton = browser.find_element_by_id("robotsRule")
button = browser.find_element_by_css_selector(".btn")

input.send_keys(y)
checkbox.click()
radiobutton.click()
button.click()

time.sleep(10)
browser.quit()
