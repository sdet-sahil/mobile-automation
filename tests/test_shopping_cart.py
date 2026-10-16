
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage


def test_add_product_to_cart(driver):
    products_page = ProductsPage(driver)
    details_page = ProductDetailsPage(driver)
    cart_page = CartPage(driver)

    # Step 1: Verify the products screen
    assert products_page.is_displayed(), (
        "Products screen is not displayed"
    )

    # Step 2: Open a product
    products_page.open_first_product()

    # Step 3: Verify product details
    product_name = details_page.get_product_title()
    assert product_name, "Product title is empty"

    # Step 4: Add the product to the cart
    details_page.add_to_cart()

    # Step 5: Open cart and verify the selected product
    cart_page.open_cart()

    assert cart_page.contains_product(product_name), (
        f"Product '{product_name}' was not found in the cart"
    )
