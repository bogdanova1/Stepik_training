from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link ="http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn-primary")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(2)
    x_element = browser.find_element_by_id("input_value")

    x = x_element.text
    print(x)
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()