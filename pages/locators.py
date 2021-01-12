from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
	BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	MESSAGE_PRICE_PRODUCT = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
	PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main .price_color')
	NAME_PRODUCT = (By.CSS_SELECTOR,'.product_main h1')
	TOTAL_MESSAGE = (By.CSS_SELECTOR,'.alertinner strong')





