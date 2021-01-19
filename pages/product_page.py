from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def add_product_to_basket(self):
		button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
		button_basket.click()
		self.solve_quiz_and_get_code()

	def should_be_see_price_product_after_add_to_basket(self):
		price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
		message_price_product = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_PRODUCT).text
		assert price_product == message_price_product, 'price product not equals message about price of product'

	def should_be_see_name_product_after_add_to_basket(self):
		name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
		message_name_product = self.browser.find_elements(*ProductPageLocators.TOTAL_MESSAGE)[0].text
		assert name_product == message_name_product, 'name product not equals message about name of product'

	def should_be_message_about_add_new_product(self):
		self.add_product_to_basket()
		self.should_be_see_name_product_after_add_to_basket()
		self.should_be_see_price_product_after_add_to_basket()
