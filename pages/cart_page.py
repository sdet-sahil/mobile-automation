
from pages.base_page import BasePage
from locators.cart_locators import CartLocators


class CartPage(BasePage):
    def open_cart(self):
        locator = self.locator_for(
            CartLocators.CART_BUTTON
        )
        self.click(locator)

    def contains_product(self, product_name):
        locator = self.locator_for(
            CartLocators.cart_product(product_name)
        )
        return self.is_visible(locator)
