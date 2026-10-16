import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException

from locators.product_details_locators import ProductDetailsLocators


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout, ignored_exceptions=[StaleElementReferenceException])

        platform_name = driver.capabilities.get("platformName", "")
        self.platform = platform_name.lower()

        if self.platform not in ("android", "ios"):
            raise ValueError(
                f"Unsupported platform: {platform_name}"
            )

    def locator_for(self, platform_locators):
        """Return the locator configured for the active platform."""
        try:
            return platform_locators[self.platform]
        except KeyError as exc:
            raise ValueError(
                f"No locator configured for {self.platform}"
            ) from exc

    def find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def get_text(self, locator):
        return self.find(locator).text

    def get_text(self, locator):
        return self.find(locator).text

    def is_element_visible(self, locator):
        try:
            self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def scroll_to_element(self, locator):
        strategy, value = locator
        escaped_value = value.replace("\\", "\\\\").replace('"', '\\"')
        if strategy == AppiumBy.ACCESSIBILITY_ID:
            selector = f'new UiSelector().description("{escaped_value}")'
        elif strategy == AppiumBy.ID:
            selector = f'new UiSelector().resourceId("{escaped_value}")'
        else:
            raise ValueError(
                f"Unsupported Android scroll locator strategy: {strategy}"
            )

        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            "new UiScrollable(new UiSelector().scrollable(true))"
            f".scrollIntoView({selector})",
        )
    
    def open_hamburger_menu(self):
        locator = self.locator_for(
            ProductDetailsLocators.HAMBURGER_MENU_BUTTON
        )
        self.wait.until(
        EC.element_to_be_clickable(locator)
    ).click()
        self.click(locator)
        
    def login(self, username, password):
        self.open_hamburger_menu();
        self.wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Login Menu Item"))).click();
        self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET"))).send_keys(username)
        self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET"))).send_keys(password)
        self.wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Tap to login with given credentials"))).click()

    def is_logged_in(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOGOUT_BUTTON)
        ).is_displayed()


