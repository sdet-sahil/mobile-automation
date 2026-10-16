from datetime import datetime
import re
import os , sys
import pytest
import pytest_html

from configuration.common_config import CAPTURE_ADB_LOGS, CAPTURE_TEST_VIDEOS
from configuration.config_loader import PROJECT_ROOT
from driver.driver_factory import create_driver
from utils.adb_logger import AdbLogger
from utils.adb_video_recorder import AppiumVideoRecorder
from utils.artifact_utils import create_artifact_directories

create_artifact_directories()

import subprocess
import time
import requests
import pytest
from pathlib import Path

def pytest_addoption(parser):
    """Built-in hook to add custom command-line flags."""
    parser.addoption(
        "--manage-appium", 
        action="store_true", 
        default=False,
        help="Automatically spin up and tear down a local Appium server."
    )


@pytest.fixture(scope="function")
def driver():
    appium_driver = create_driver()
    try:
        yield appium_driver
    finally:
        appium_driver.quit()


@pytest.fixture(autouse=True)
def capture_adb_logs(request):
    if not CAPTURE_ADB_LOGS:
        yield
        return
    logger = AdbLogger()
    log_path = logger.start(request.node.name)

    yield

    logger.stop()

    if hasattr(request.node, "rep_call"):
        if request.node.rep_call.failed:
            print(f"\nADB logs saved to: {log_path}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Keep reports available to existing fixtures.
    setattr(item, f"rep_{report.when}", report)

    # Capture screenshots only when the test body fails.
    if report.when != "call" or not report.failed:
        return

    # Find the active Appium driver.
    driver = next((
        value
        for value in item.funcargs.values()
        if callable(getattr(value, "get_screenshot_as_file", None))
    ), None)

    if driver is None:
        print("\nScreenshot skipped: driver unavailable.")
        return

    screenshots_dir = PROJECT_ROOT / "artifacts" / "screenshots"
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    safe_name = re.sub(r"[^a-zA-Z0-9_-]", "_", item.nodeid)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    screenshot_path = screenshots_dir / f"{safe_name}_{timestamp}.png"

    try:
        captured = driver.get_screenshot_as_file(str(screenshot_path))

        if captured:
            extras = getattr(report, "extras", [])
            extras.append(
                pytest_html.extras.image(
                    str(screenshot_path),
                    mime_type="image/png",
                )
            )
            report.extras = extras

            print(f"\nScreenshot saved: {screenshot_path}")

    except Exception as exc:
        print(f"\nScreenshot capture failed: {exc}")


@pytest.fixture(autouse=True)
def capture_test_video(request, driver):
    if not CAPTURE_TEST_VIDEOS:
        yield
        return
    recorder = AppiumVideoRecorder(driver)
    recorder.start(request.node.name)

    try:
        yield
    finally:
        video_path = recorder.stop()

        if video_path and hasattr(request.node, "rep_call"):
            if not request.node.rep_call.failed:
                recorder.discard()
            else:
                print(f"\nFailure video saved to: {video_path}")
