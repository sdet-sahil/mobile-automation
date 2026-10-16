# Mobile Automation

An Appium and pytest-based UI automation project for testing the demo shopping app on Android or iOS. The suite uses page objects and locators, and can capture screenshots, ADB logs, and test videos.

## Requirements

- Python 3.9 or later
- Appium Server 2.x, running at `http://127.0.0.1:4723`
- The Appium driver for your target platform:
  - Android: UiAutomator2
  - iOS: XCUITest
- A configured Android emulator or device, or an iOS simulator or device
- Android only: Android SDK Platform Tools (`adb`)

The demo app is included at `apk/demo.apk`.

## Setup

Create and activate a virtual environment, then install the Python dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Start the Appium server in a separate terminal:

```bash
appium
```

Before running tests, check `configuration/devices.json` and update the device profile for your target device. In particular, set the correct `udid` and `deviceName`. The default profile is `Redmi_Note10S` in `configuration/environments/local.json`. The included iPhone profile has a placeholder UDID and must be configured before use.

The app path and Appium server URL are configured in `configuration/common.json`. Environment-specific defaults, including the device profile, are in `configuration/environments/`.

## Running tests

Run the full test suite:

```bash
pytest
```

Run an individual test file or select tests by name:

```bash
pytest tests/test_shopping_cart.py
pytest -k product_description
```

By default, pytest writes an HTML report to `artifacts/reports/report.html`. Failed UI tests can attach screenshots to the report. ADB logs are captured by default; disable them with `CAPTURE_ADB_LOGS=false`. Test video capture is off by default; enable it with `CAPTURE_TEST_VIDEOS=true`.

```bash
CAPTURE_ADB_LOGS=false pytest
CAPTURE_TEST_VIDEOS=true pytest
```

## Configuration

| Setting | Location or environment variable | Default |
| --- | --- | --- |
| Appium server URL and app definitions | `configuration/common.json` | `http://127.0.0.1:4723`, `demo_app` |
| Device capabilities | `configuration/devices.json` | `Redmi_Note10S` |
| Environment defaults | `configuration/environments/<name>.json` | `local` |
| Environment to load | `TEST_ENV` | `local` |
| Device profile to use | `DEVICE_PROFILE` | Environment's `default_device` |
| Capture ADB logs | `CAPTURE_ADB_LOGS` | `true` |
| Capture test videos | `CAPTURE_TEST_VIDEOS` | `false` |

Boolean capture variables accept `true` or `false`.

## Project layout

```text
configuration/  Appium, device, and environment configuration
core/           Shared UI actions
driver/         Appium driver setup
locators/       App element locators
models/         Data models
pages/          Page objects
tests/          pytest UI tests
utils/          ADB logging, video recording, and artifact helpers
apk/            Demo application package
artifacts/      Test reports and captured output
```
# mobile-automation
