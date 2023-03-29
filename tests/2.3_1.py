import time
import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/alert_accept.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла