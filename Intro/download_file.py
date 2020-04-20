from selenium import webdriver
import os
import time

browser = webdriver.Chrome()
link = " http://suninjuly.github.io/file_input.html"
browser.get(link)

input1 = browser.find_element_by_css_selector("[name='firstname']")
input1.send_keys("Ivan")
input2 = browser.find_element_by_css_selector("[name='lastname']")
input2.send_keys("Petrov")
input3 = browser.find_element_by_css_selector("[name='email']")
input3.send_keys("Ivan@test.com")

element = browser.find_element_by_css_selector("#file")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
element.send_keys(file_path)

button = browser.find_element_by_css_selector(".btn")
button.click()

time.sleep(10)
browser.quit()

