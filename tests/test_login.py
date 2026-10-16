from locators.base_locators import BaseLocators
from pages.base_page import BasePage
from locators.products_locators import ProductsLocators
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
import time

def test_valid_login(driver):
    products_page = ProductsPage(driver)
    product_details_page = ProductDetailsPage(driver)
    products_page.open_hamburger_menu();
    products_page.login("bod@example.com", "10203040");
    products_page.open_hamburger_menu();
    time.sleep(5)
    assert products_page.is_element_visible(
        products_page.locator_for(BaseLocators.LOGOUT_BUTTON)
    )

    assert products_page.get_text(
        products_page.locator_for(BaseLocators.LOGOUT_BUTTON)
    ) == "Log Out"
    
