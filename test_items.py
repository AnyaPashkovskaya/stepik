import time

def test_check_button(browser):
	browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
	time.sleep(30)
	button = browser.find_elements_by_css_selector("#add_to_basket_form>.btn")
	assert len(button)==1, "the button doesn't exist"