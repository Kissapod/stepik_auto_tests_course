from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    res = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    button = browser.find_element(By.TAG_NAME, "button")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(res)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radioRobotsRule = browser.find_element(By.ID, "robotsRule")
    radioRobotsRule.click()

    button.click()

except Exception as err:
    print(err)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()