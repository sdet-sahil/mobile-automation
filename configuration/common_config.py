
import os


def _get_bool(name, default=False):
    value = os.getenv(name, str(default)).strip().lower()

    if value not in ("true", "false"):
        raise ValueError(
            f"{name} must be 'true' or 'false', got: {value!r}"
        )

    return value == "true"


CAPTURE_ADB_LOGS = _get_bool(
    "CAPTURE_ADB_LOGS",
    default=True,
)

CAPTURE_TEST_VIDEOS = _get_bool(
    "CAPTURE_TEST_VIDEOS",
    default=False,
)