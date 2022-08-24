from selenium.webdriver.common.by import By



class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-group > a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REG = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REG = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REPEATE = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form > .btn")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success > .alertinner strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alertinner > p strong")
    

class BasketPageLocators():
    MESSAGE_NO_PRODUCTS = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCT_FORM = (By.CSS_SELECTOR, ".basket-items")