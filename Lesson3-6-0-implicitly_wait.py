from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()

    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait1.html")

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

    browser.get("http://suninjuly.github.io/cats.html")
    browser.find_element_by_id("button")

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()