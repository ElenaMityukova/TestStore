from selenium.webdriver.common.by import By
from time import sleep

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"


def test_guest_should_see_button_add_to_basket(browser):
    browser.get(link)
    add_to_basket = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    sleep(3)
    assert add_to_basket
    print("We found button 'Add to basket'!")
    sleep(3)
    
