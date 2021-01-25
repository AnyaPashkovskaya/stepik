from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def add_product_to_basket(self):
		button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
		button_basket.click()
		self.solve_quiz_and_get_code()

	def should_not_be_success_message(self):#элемент не появляется на странице в течение заданного времени
		assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRICE_PRODUCT), \
       "Success message about price is presented, but should not be"
		assert self.is_not_element_present(*ProductPageLocators.TOTAL_MESSAGE), \
		"Success message about product is presented, but should not be"

	def should_dissepeard_message_after_adding_basket(self):
		assert self.is_disappeared(*ProductPageLocators.MESSAGE_PRICE_PRODUCT), \
       "Success message about price product after adding price is not dissapeard"
		assert self.is_disappeared(*ProductPageLocators.TOTAL_MESSAGE), \
		"Success message about product after adding price is not dissapeard"


	def should_be_see_price_product_after_add_to_basket(self):
		price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
		message_price_product = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_PRODUCT).text
		assert price_product == message_price_product, 'price product not equals message about price of product'

	def should_be_see_name_product_after_add_to_basket(self):
		name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
		message_name_product = self.browser.find_elements(*ProductPageLocators.TOTAL_MESSAGE)[0].text
		assert name_product == message_name_product, 'name product not equals message about name of product'

	def should_see_button_basket_view(self):
		assert self.is_element_present(*ProductPageLocators.BUTTON_BASKET_VIEW), \
		"can't see button_basket_view"

	def go_to_basket_view(self):
		button_basket_view = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET_VIEW)
		button_basket_view.click()



	def should_be_message_about_add_new_product(self):
		self.add_product_to_basket()
		self.should_be_see_name_product_after_add_to_basket()
		self.should_be_see_price_product_after_add_to_basket()

