from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

 
@pytest.mark.user
class TestUserAddToBasketFromProductPage:

	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
		page = LoginPage(browser, link)
		page.open()
		email = str(time.time()) + "@fakemail.org"
		password = str(time.time())
		page.register_new_user(email, password)
		page.should_be_authorized_user()
  
	@pytest.mark.xfail
	def test_user_cant_see_success_message_after_adding_product_to_basket(browser):
		link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
		page = ProductPage(browser, link)
		page.open()
		page.should_be_message_about_add_new_product()


	def test_user_cant_see_success_message(browser):
		link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
		page = ProductPage(browser, link)
		page.open()
		page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
	link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_message_about_add_new_product()
	page.should_dissepeard_message_after_adding_basket()

def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = MainPage(browser, link)
	page.open()
	page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_see_button_basket_view()
	page.go_to_basket_view() 
	page = BasketPage(browser, browser.current_url)
	page.should_not_items_in_empty_busket()
	page.should_see_title_about_empty_basket()




