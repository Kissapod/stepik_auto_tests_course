import pytest
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/236895/step/1"

def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="session")
def load_config():
    # Открываем файл с конфигом в режиме чтения
    with open('config.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        return config

class TestLogin:
    def test_authorization(self, browser, load_config):
        login = load_config['login_stepik']
        password = load_config['password_stepik']
        browser.get(link)
        time.sleep(1)
        buttonEnter = browser.find_element(By.ID, "ember458")
        buttonEnter.click()
        time.sleep(1)
        inputEmail = browser.find_element(By.ID, "id_login_email")
        inputEmail.send_keys(login)
        time.sleep(1)
        inputPassword = browser.find_element(By.ID, "id_login_password")
        inputPassword.send_keys(password)
        time.sleep(1)
        enterButton = browser.find_element(By.CLASS_NAME, "sign-form__btn")
        enterButton.click()
        time.sleep(5)