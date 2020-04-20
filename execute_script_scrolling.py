from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x = browser.find_element_by_id("input_value")
x = x.text
y = math.log(abs(12 * math.sin(int(x))))

input = browser.find_element_by_id("answer")
input.send_keys(str(y))
browser.execute_script("window.scrollBy(0, 100);")

checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()

radiobutton = browser.find_element_by_id("robotsRule")
radiobutton.click()

button = browser.find_element_by_css_selector(".btn")
button.click()
browser.quit()
