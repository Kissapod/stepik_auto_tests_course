import pytest
import math
import json
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://stepik.org/lesson/236895/step/1"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestInput:
    resultMessage = ""
    linksTests = [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1",
    ]
    @pytest.mark.parametrize('links', linksTests)
    def test_links(self, browser, links):
        link = f"{links}"
        login = "aksel@gmail.com"
        password = "64342"
        browser.get(link)
        buttonEnter = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "ember458"))
        )
        buttonEnter.click()
        time.sleep(1)
        inputEmail = browser.find_element(By.ID, "id_login_email")
        inputEmail.send_keys(login)
        inputPassword = browser.find_element(By.ID, "id_login_password")
        inputPassword.send_keys(password)
        enterButton = browser.find_element(By.CLASS_NAME, "sign-form__btn")
        enterButton.click()
        textarea = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "textarea"))
        )
        textarea.send_keys(str(math.log(int(time.time() + 1))))
        button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        button.click()
        hintMessage = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        )
        message = hintMessage.text
        if message != "Correct!":
            self.resultMessage += message
            print(self.resultMessage)

        assert "Correct!" in message

if __name__ == "__main__":
    unittest.main()