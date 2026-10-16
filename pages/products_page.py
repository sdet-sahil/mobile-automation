from pages.base_page import BasePage
from locators.products_locators import ProductsLocators


class ProductsPage(BasePage):
    def is_displayed(self):
        locator = self.locator_for(
            ProductsLocators.PRODUCTS_HEADER
        )
        return self.is_element_visible(locator)
    
    def open_first_product(self):
        locator = self.locator_for(
            ProductsLocators.FIRST_PRODUCT
        )
        self.click(locator)

    def open_hamburger_menu(self):
            locator = self.locator_for(
                ProductsLocators.HAMBURGER_MENU_BUTTON
            )
            self.click(locator)

    def open_qr_code_scanner(self):
                locator = self.locator_for(
                    ProductsLocators.QR_CODE_SCANNER_BUTTON
                )
                self.click(locator)
                
    def native_crash(self):
        locator = self.locator_for(
            ProductsLocators.NATIVE_CRASH_BUTTON
        )
        self.click(locator)
