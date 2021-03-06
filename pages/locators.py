from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	BUTTON_BASKET_VIEW = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")





class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
	REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
	REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
	REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTRATION_BUTTON =  (By.CSS_SELECTOR, "[name=registration_submit]")

class Urls():
	PROMO_LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	LINK_BOOK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

class ProductPageLocators():
	BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	MESSAGE_PRICE_PRODUCT = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
	PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main .price_color')
	NAME_PRODUCT = (By.CSS_SELECTOR,'.product_main h1')
	TOTAL_MESSAGE = (By.CSS_SELECTOR,'.alertinner strong')
	BUTTON_BASKET_VIEW = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
	BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
	TITLE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner")





