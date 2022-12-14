from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators:
    BASKET_PRODUCT = (By.CSS_SELECTOR, "#basket_formset")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
    EMAIL = (By.CSS_SELECTOR, "input[name='registration-email']")
    PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password1']")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "div.alert-info strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "h1 ~ .price_color")




