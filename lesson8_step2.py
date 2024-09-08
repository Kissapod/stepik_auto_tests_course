from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
import math
def calc(x, y):
  return int(x) + int(y)

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    res = calc(x, y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(res)).click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

except Exception as err:
    print(err)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()