from pages.base_page import BasePage
from locators.products_locators import ProductsLocators
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage

def test_product_description(driver):
    products_page = ProductsPage(driver)
    product_details_page = ProductDetailsPage(driver)

    products_page.open_first_product()

    actual_description = (
        product_details_page.get_product_description()
    )

    expected_description = (
        "carry.allTheThings() with the sleek, streamlined "
        "Sly Pack that melds uncompromising style with "
        "unequaled laptop and tablet protection."
    )

    assert actual_description == expected_description
