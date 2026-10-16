from appium.webdriver.common.appiumby import AppiumBy


class ProductDetailsLocators:
    PRODUCT_TITLE = {
        "android": (
            AppiumBy.ID,
            "com.saucelabs.mydemoapp.android:id/productTV",
        ),
        "ios": (
            AppiumBy.ACCESSIBILITY_ID,
            "test-Description",  # Not yet verified on iOS
        ),
    }
    
    PRODUCT_DESCRIPTION = {
        "android": (
            AppiumBy.ID,
            "com.saucelabs.mydemoapp.android:id/descTV",
        ),
        "ios": (
            AppiumBy.ACCESSIBILITY_ID,
            "REPLACE_WITH_IOS_DESCRIPTION_IDENTIFIER",
        ),
    }

    ADD_TO_CART_BUTTON = {
        "android": (
            AppiumBy.ACCESSIBILITY_ID,
            "Tap to add product to cart",
        ),
        "ios": (
            AppiumBy.ACCESSIBILITY_ID,
            "test-ADD TO CART",  # Not yet verified on iOS
        ),
    }
