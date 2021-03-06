import unittest
from selenium import webdriver
import time


class TestRegistration(unittest.TestCase):
    def test_link1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        try:
            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_css_selector(".first_block .first")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector(".first_block .second")
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_css_selector(".first_block .third")
            input3.send_keys("ivan@test.com")
            input4 = browser.find_element_by_css_selector(".second_block .first")
            input4.send_keys("+469202039847")
            input5 = browser.find_element_by_css_selector(".second_block .second")
            input5.send_keys("131 Gamla Stan, Stockholm, Sweden, 12522")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 'incorrect message')

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        try:
            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_css_selector(".first_block .first")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector(".first_block .second")
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_css_selector(".first_block .third")
            input3.send_keys("ivan@test.com")
            input4 = browser.find_element_by_css_selector(".second_block .first")
            input4.send_keys("+469202039847")
            input5 = browser.find_element_by_css_selector(".second_block .second")
            input5.send_keys("131 Gamla Stan, Stockholm, Sweden, 12522")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 'incorrect message')

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()