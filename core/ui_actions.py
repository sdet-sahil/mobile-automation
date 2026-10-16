import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger(__name__)


class UIActions:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

        self.wait = WebDriverWait(
            driver,
            timeout,
            poll_frequency=0.5,
        )

    def find_visible(self, locator, name="element"):
        logger.debug("Waiting for visible %s: %s", name, locator)

        try:
            return self.wait.until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException as exc:
            logger.exception(
                "Timed out waiting for visible %s: %s",
                name,
                locator,
            )
            raise TimeoutException(
                f"Timed out after {self.timeout}s waiting for "
                f"'{name}' using locator {locator}"
            ) from exc

    def click(self, locator, name="element"):
        logger.debug("Waiting to click %s: %s", name, locator)

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

        logger.debug("Clicked %s successfully", name)

    def enter_text(
        self,
        locator,
        value,
        name="text field",
        clear_first=True,
    ):
        logger.debug("Entering text into %s", name)

        element = self.find_visible(locator, name)

        if clear_first:
            element.clear()

        element.send_keys(value)

        logger.debug("Text entered into %s", name)

    def get_text(self, locator, name="element"):
        element = self.find_visible(locator, name)
        value = element.text.strip()

        logger.debug("Read text from %s: %r", name, value)
        return value