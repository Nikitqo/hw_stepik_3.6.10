from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_has_add_to_cart_button(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    assert browser.find_element(By.ID, "add_to_basket_form"), 'Button is not visible'