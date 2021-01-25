from .locators import BasketPageLocators
from .base_page import BasePage
class BasketPage(BasePage):
	pass

	def should_not_items_in_empty_busket(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "empty busket has items"

	def should_see_title_about_empty_basket(self):
		assert self.is_element_present(*BasketPageLocators.TITLE_BASKET_IS_EMPTY), "can't see title about empty basket"

		