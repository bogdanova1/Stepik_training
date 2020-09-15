from selenium import webdriver
import random
import string
import time

def random_string(prefix, maxlen):
#    symbols = string.ascii_letters + string.digits + string.punctuation + " "
#return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(maxlen)])

password = random_string("", 9)
email = password+"@test.com"

link ="http://selenium1py.pythonanywhere.com/ru/"

def test_registration(email,password):
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)

        button = browser.find_element_by_id("login_link")
        button.click()

        input1 = browser.find_element_by_id("id_registration-email")
        input1.send_keys(email)

        input2 = browser.find_element_by_id("id_registration-password1")
        input2.send_keys(password)

        input3 = browser.find_element_by_id("id_registration-password2")
        input3.send_keys(password)

        button = browser.find_element_by_css_selector("button[name = 'registration_submit']")
        button.click()

        message = browser.find_element_by_class_name("alertinner")
        assert "Спасибо за регистрацию!" in message.text

        button = browser.find_element_by_id("logout_link")
        button.click()

        assert browser.current_url == link


    finally:
#        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()

def test_authorization(email,password):
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)

        button = browser.find_element_by_id("login_link")
        button.click()

        input1 = browser.find_element_by_id("id_login-username")
        input1.send_keys(email)

        input2 = browser.find_element_by_id("id_login-password")
        input2.send_keys(password)

        button = browser.find_element_by_css_selector("button[name = 'login_submit']")
        button.click()

        message = browser.find_element_by_class_name("alertinner")
        assert "Рады видеть вас снова" in message.text

        button = browser.find_element_by_id("logout_link")
        button.click()

        assert browser.current_url == link


    finally:
#        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()

def test_view_all_articles():
    pass

def test_search_article():
    pass

def test_add_article_in_basket():
    pass

test_registration(email,password)
test_authorization(email,password)
test_view_all_articles()
test_search_article()
test_add_article_in_basket()
