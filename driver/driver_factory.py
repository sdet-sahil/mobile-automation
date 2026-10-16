from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from configuration.config_loader import load_config


def create_driver():
    config = load_config()
    capabilities = config["capabilities"]

    platform = capabilities["platformName"].lower()

    if platform == "android":
        options = UiAutomator2Options()
    elif platform == "ios":
        options = XCUITestOptions()
    else:
        raise ValueError(f"Unsupported platform: {platform}")

    options.load_capabilities(capabilities)

    # Apply the device-specific workaround only to Android.
    if platform == "android":
        options.ignore_hidden_api_policy_error = True
        options.skip_device_initialization = True

    driver = webdriver.Remote(
        command_executor=config["appium_server_url"],
        options=options,
    )

    return driver