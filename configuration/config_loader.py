import json
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIGURATION_DIR = PROJECT_ROOT / "configuration"
COMMON_CONFIG_FILE = CONFIGURATION_DIR / "common.json"
DEVICES_CONFIG_FILE = CONFIGURATION_DIR / "devices.json"
ENVIRONMENTS_DIR = CONFIGURATION_DIR / "environments"


def load_config():
    with COMMON_CONFIG_FILE.open(encoding="utf-8") as file:
        common_config = json.load(file)

    with DEVICES_CONFIG_FILE.open(encoding="utf-8") as file:
        devices = json.load(file)

    environment_name = os.getenv("TEST_ENV", "local")
    available_environments = sorted(
        path.stem for path in ENVIRONMENTS_DIR.glob("*.json")
    )
    if environment_name not in available_environments:
        raise ValueError(
            f"Unknown test environment: {environment_name}. "
            f"Available environments: {available_environments}"
        )

    environment_file = ENVIRONMENTS_DIR / f"{environment_name}.json"
    with environment_file.open(encoding="utf-8") as file:
        environment_config = json.load(file)

    profile_name = os.getenv(
        "DEVICE_PROFILE",
        environment_config["default_device"],
    )
    if profile_name not in devices:
        raise ValueError(
            f"Unknown device profile: {profile_name}. "
            f"Available profiles: {list(devices)}"
        )

    app_name = environment_config.get(
        "default_app",
        common_config["default_app"],
    )
    if app_name not in common_config["apps"]:
        raise ValueError(
            f"Unknown app: {app_name}. "
            f"Available apps: {list(common_config['apps'])}"
        )

    app_config = common_config["apps"][app_name]
    capabilities = devices[profile_name].copy()
    capabilities["appium:app"] = str(PROJECT_ROOT / app_config["path"])

    return {
        "environment": environment_name,
        "appium_server_url": common_config["appium_server_url"],
        "api_base_urls": environment_config.get("api_base_urls", {}),
        "device_profile": profile_name,
        "app": app_config,
        "capabilities": capabilities,
    }