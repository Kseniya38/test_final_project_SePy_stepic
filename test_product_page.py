#rom .pages.main_page import MainPage
#from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By
import time

#def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
#    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#    page.open()                      # открываем страницу
#    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
#    login_page = LoginPage(browser, browser.current_url)
#    login_page.should_be_login_page()

#def test_guest_should_see_login_link(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
#    page = MainPage(browser, link)
#    page.open()
#    page.should_be_login_link()

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(10)
    #check_success_message_added_product()
    #check_total_basket_message()

    