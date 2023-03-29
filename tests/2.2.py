import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/execute_script.html"



try:

    browser = webdriver.Chrome()
    browser.get(link)

    x_1 = browser.find_element(By.CSS_SELECTOR, "#num1")

    x_2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    sum = str(int(x_1.text) + int(x_2.text))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)




    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла