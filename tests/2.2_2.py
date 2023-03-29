import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/execute_script.html"



try:

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")

    x = x_element.text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)
    check_box = browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]')
    check_box.click()
    radio_button = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
    radio_button.click()

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла