
import base64
import re
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
VIDEO_DIR = PROJECT_ROOT / "artifacts" / "videos"


class AppiumVideoRecorder:
    def __init__(self, driver, output_dir=VIDEO_DIR):
        self.driver = driver
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.video_data = None
        self.video_path = None

    def start(self, test_name):
        safe_name = re.sub(
            r"[^a-zA-Z0-9_.-]+", "_", test_name
        ).strip("._") or "test"

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        self.video_path = self.output_dir / (
            f"{safe_name}_{timestamp}.mp4"
        )

        self.driver.start_recording_screen(
            options={
                "timeLimit": "180",
                "bitRate": 4_000_000,
            }
        )

    def stop(self):
        if self.video_path is None:
            return None

        self.video_data = self.driver.stop_recording_screen()

        if not self.video_data:
            raise RuntimeError("Appium returned no screen recording.")

        self.video_path.write_bytes(
            base64.b64decode(self.video_data)
        )

        return self.video_path

    def discard(self):
        if self.video_path and self.video_path.exists():
            self.video_path.unlink()
