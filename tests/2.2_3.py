import time
import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/alert_accept.html"



try:

    browser = webdriver.Chrome()
    browser.get(link)

    confirm = browser.switch_to.alert
    confirm.accept()

    x_1 = browser.find_element(By.CSS_SELECTOR, "#num1")


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)


    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла