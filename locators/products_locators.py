from appium.webdriver.common.appiumby import AppiumBy
from locators.base_locators import BaseLocators


class ProductsLocators(BaseLocators):
    PRODUCTS_HEADER = {
        "android": (AppiumBy.ID,
                    "com.saucelabs.mydemoapp.android:id/productTV",),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "title"),
    }

    FIRST_PRODUCT = {
        "android": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/productIV").instance(0)'),
        "ios": (AppiumBy.ACCESSIBILITY_ID, "Product Title"),
    }

    HAMBURGER_MENU_BUTTON = {
                "android": (
                    AppiumBy.ACCESSIBILITY_ID,
                    "View menu",
                ),
                "ios": (
                    AppiumBy.ACCESSIBILITY_ID,
                    "test-ADD TO CART",  # Not yet verified on iOS
                ),
            }

    NATIVE_CRASH_BUTTON = {
                    "android": (
                        AppiumBy.ID,
                        "com.saucelabs.mydemoapp.android:id/cause_native_crash_button",
                    ),
                    "ios": (
                        AppiumBy.ACCESSIBILITY_ID,
                        "test-ADD TO CART",  # Not yet verified on iOS
                    ),
                }
