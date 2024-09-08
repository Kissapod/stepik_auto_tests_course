from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который:
    # Считать значение для переменной x.
    # Посчитать математическую функцию от x (код для этого приведён ниже).
    # Ввести ответ в текстовое поле.
    # Отметить checkbox "I'm the robot".
    # Выбрать radiobutton "Robots rule!".
    x_element = browser.find_element(By.TAG_NAME, "img").get_attribute("valuex")
    y = calc(x_element)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radioRobotsRule = browser.find_element(By.ID, "robotsRule")
    radioRobotsRule.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

except Exception as err:
    print(err)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()