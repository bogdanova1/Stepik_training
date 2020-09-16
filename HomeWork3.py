from selenium import webdriver
import random
import string
import time
from selenium.webdriver.support.ui import Select

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(maxlen)])

main_page_link ="http://selenium1py.pythonanywhere.com/ru/"

def test_registration(email,password):
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

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
        assert "Спасибо за регистрацию!" in message.text, "No message about registration"

        button = browser.find_element_by_id("logout_link")
        button.click()

        assert browser.current_url == main_page_link, "No return to main page"


    finally:
#        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()

def test_authorization(email,password):
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        button = browser.find_element_by_id("login_link")
        button.click()

        input1 = browser.find_element_by_id("id_login-username")
        input1.send_keys(email)

        input2 = browser.find_element_by_id("id_login-password")
        input2.send_keys(password)

        button = browser.find_element_by_css_selector("button[name = 'login_submit']")
        button.click()

        message = browser.find_element_by_class_name("alertinner")
        assert "Рады видеть вас снова" in message.text,  "No message about authorization"

        button = browser.find_element_by_id("logout_link")
        button.click()

        assert browser.current_url == main_page_link, "No return to main page"


    finally:
#        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()

def test_view_all_articles():
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        browser.find_element_by_link_text('Все товары').click()
        header=browser.find_elements_by_css_selector('.page-header h1')
        assert len(header) > 0 and header[0].text == 'Все товары', "Нет заголовка"
        assert len(browser.find_elements_by_class_name('side_categories'))>0, "Нет области фильтров"
        assert len(browser.find_elements_by_class_name('form-horizontal'))>0,\
            "Нет количества найденных результатов"
        assert len(browser.find_elements_by_css_selector('ol.row')) > 0, "Нет таблицы с товарами"
        assert len(browser.find_elements_by_css_selector('article img')) > 0  # картинка товара
        assert len(browser.find_elements_by_css_selector('article h3')) > 0  # название товара
        assert len(browser.find_elements_by_css_selector('article .price_color')) > 0  # цена товара
        assert len(browser.find_elements_by_css_selector('article .availability')) > 0 #  доступность на складе
        assert len(browser.find_elements_by_css_selector('article button.btn')) > 0 or \
               len(browser.find_elements_by_css_selector('article span.btn')) > 0 #  кнопка "Добавить в корзину"
        if len(browser.find_elements_by_class_name('pager')) > 0: #есть пагинация
            browser.find_elements_by_css_selector('.next a')[0].click()
            assert browser.current_url.endswith("catalogue/?page=2"), "Нет перхода на 2 страницу"

        browser.find_element_by_css_selector('article a').click() #перейти на страницу товара
        assert len(browser.find_elements_by_css_selector('.product_page img')) > 0 # картинка
        assert len(browser.find_elements_by_css_selector('.product_page h1')) > 0# название
        assert len(browser.find_elements_by_css_selector('.product_page .price_color')) > 0 # цена
        assert len(browser.find_elements_by_css_selector('.product_page .availability')) > 0  # доступность на складе
        assert len(browser.find_elements_by_css_selector('.product_page #write_review')) > 0 # кнопка "Написать отзыв"
        assert len(browser.find_elements_by_css_selector('.product_page button.btn')) > 0 # кнопка "Добавить в корзину" или кнопка "Сообщить мне"
        assert len(browser.find_elements_by_css_selector('.product_page #product_description')) > 0     # заголовок "Описание товара"
        assert len(browser.find_elements_by_css_selector('.product_page .sub-header')) > 1 and \
            browser.find_elements_by_css_selector('.product_page .sub-header')[1].text=='Информация о товаре' # заголовок "Информация о товаре"
        assert len(browser.find_elements_by_css_selector('.product_page #reviews')) > 0 # заголовок "Отзывы Клиентов"

        browser.find_element_by_css_selector('.breadcrumb a[href="/ru/"]').click()
        assert browser.current_url == main_page_link, "No return to main page"

    finally:
    # закрываем браузер после всех манипуляций
        browser.quit()

def test_search_article_by_part_name(part_name):
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)
        browser.find_element_by_css_selector("input[type = 'search']").send_keys(part_name)
        browser.find_element_by_css_selector('.navbar-form.navbar-right input[type = "submit"]').click()
        assert part_name in browser.find_element_by_class_name('page-header').text
        articles=browser.find_elements_by_css_selector("product_pod a[title]")
        for article in articles:
            assert part_name in article.text
        select = Select(browser.find_element_by_css_selector("select#id_sort_by"))
        select.select_by_value("title-asc")


        time.sleep(3)

    finally:
    # закрываем браузер после всех манипуляций
        browser.quit()

def test_add_article_in_basket():
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)

        add_basket = browser.find_elements_by_css_selector('article button.btn')
        if len(add_basket) > 0: #есть кнопка "Добавить в корзину"
            add_basket[0].click()
            #assert browser.current_url.endswith("catalogue/?page=2")
    finally:
    # закрываем браузер после всех манипуляций
        browser.quit()

#1. Регистрация
#test_registration('1@test.com','QqWWEe!1@2')

#2. Авторизация
password = random_string("", 9)
email = password+"@test.com"
#test_authorization(email,password)

# 3. Просмотр товаров
#test_view_all_articles()

# 4. Поиск товара по части наименовани
test_search_article_by_part_name("coder")

# 5. Добавление товара в корзину
# test_add_article_in_basket()
