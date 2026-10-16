
from configuration.config_loader import PROJECT_ROOT

ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
REPORTS_DIR = ARTIFACTS_DIR / "reports"
ADB_LOGS_DIR = ARTIFACTS_DIR / "logs" / "adb"
APPIUM_LOGS_DIR = ARTIFACTS_DIR / "logs" / "appium"


def create_artifact_directories():
    for directory in (
        REPORTS_DIR,
        ADB_LOGS_DIR,
        APPIUM_LOGS_DIR,
    ):
        directory.mkdir(parents=True, exist_ok=True)
