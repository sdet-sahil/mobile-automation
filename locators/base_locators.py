
from appium.webdriver.common.appiumby import AppiumBy


class BaseLocators:
    LOGOUT_BUTTON = {
        "android": (
            AppiumBy.ACCESSIBILITY_ID,
            "Logout Menu Item",
        ),
        "ios": (
            AppiumBy.ACCESSIBILITY_ID,
            "test-Cart",
        ),
    }

    QR_CODE_SCANNER_BUTTON = {
            "android": (
                AppiumBy.XPATH,
                "//android.widget.TextView[@resource-id='com.saucelabs.mydemoapp.android:id/itemTV' and @text='Crash app (debug)']",
            ),
            "ios": (
                AppiumBy.ACCESSIBILITY_ID,
                "test-Cart",
            ),
        }