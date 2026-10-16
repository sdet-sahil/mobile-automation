from locators.base_locators import BaseLocators
from pages.base_page import BasePage
from locators.products_locators import ProductsLocators
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
import time

def test_native_crash(driver):
    products_page = ProductsPage(driver)
    products_page.open_hamburger_menu()
    products_page.open_qr_code_scanner()
    products_page.native_crash()
    time.sleep(3)
    
