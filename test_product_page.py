from .pages.main_page import MainPage
from .pages.product_page import ProductPage
def test_guest_can_add_product_to_basket(browser):
	link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
	page = ProductPage(browser, link)
	page.open()
	page.should_be_message_about_add_new_product()
