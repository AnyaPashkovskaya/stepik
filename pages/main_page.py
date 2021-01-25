from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
class MainPage(BasePage):
	pass

	def go_to_basket(self):
		button = self.browser.find_element(*MainPageLocators.BUTTON_BASKET_VIEW)
		button.click()

	def should_be_basket(self):
		assert self.is_element_present(*MainPageLocators.BUTTON_BASKET_VIEW), "Button basket is not presented"

