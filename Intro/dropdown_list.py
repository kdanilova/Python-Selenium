from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

# s = 0
x = browser.find_element_by_id("num1")
y = browser.find_element_by_id("num2")
x = x.text
y = y.text
# s = str(int(x) + int(y))
# print(str(int(x)+int(y)))

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(int(x)+int(y)))

button = browser.find_element_by_css_selector(".btn")
button.click()

time.sleep(10)
browser.quit()
