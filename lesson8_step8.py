from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstName = browser.find_element(By.NAME, "firstname")
    firstName.send_keys("Maxim")

    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("Kot")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("Kot@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'biografy.txt')  # добавляем к этому пути имя файла
    file = browser.find_element(By.NAME, "file")
    file.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

except Exception as err:
    print(err)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()