
from pages.base_page import BasePage
from locators.product_details_locators import (
    ProductDetailsLocators,
)


class ProductDetailsPage(BasePage):
    
    def get_product_title(self):
        locator = self.locator_for(
            ProductDetailsLocators.PRODUCT_TITLE
        )
        return self.get_text(locator)

    def add_to_cart(self):
        locator = self.locator_for(
            ProductDetailsLocators.ADD_TO_CART_BUTTON
        )
        self.click(locator)

    def get_product_description(self):
        locator = self.locator_for(
        ProductDetailsLocators.PRODUCT_DESCRIPTION
        )
        self.scroll_to_element(locator)
        return self.get_text(locator)
