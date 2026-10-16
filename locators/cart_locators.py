
from appium.webdriver.common.appiumby import AppiumBy


class CartLocators:
    CART_BUTTON = {
        "android": (
            AppiumBy.ACCESSIBILITY_ID,
            "View cart",
        ),
        "ios": (
            AppiumBy.ACCESSIBILITY_ID,
            "test-Cart",
        ),
    }

    CART_HEADER = {
        "android": (
            AppiumBy.ANDROID_UIAUTOMATOR,
'new UiSelector().text("My Cart")',
),
        "ios": (
            AppiumBy.ACCESSIBILITY_ID,
            "test-Cart Content",
        ),
    }

    # Text locator examples for platform-specific implementations.
    @staticmethod
    def cart_product(product_name):
        return {
            "android": (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().text("{product_name}")',
            ),
            "ios": (
                AppiumBy.IOS_PREDICATE,
                f'label == "{product_name}"',
            ),
        }
