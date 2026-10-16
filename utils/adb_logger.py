
import subprocess
from pathlib import Path
from datetime import datetime


class AdbLogger:
    def __init__(self, output_dir="artifacts/logs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.process = None
        self.log_file = None

    def start(self, test_name):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = "".join(
            c if c.isalnum() or c in "-_" else "_"
            for c in test_name
        )

        self.log_file = self.output_dir / (
            f"{safe_name}_{timestamp}.log"
        )

        # Clear old device logs before this test.
        subprocess.run(
            ["adb", "logcat", "-c"],
            check=True,
            timeout=10,
        )

        self.file_handle = self.log_file.open(
            "w", encoding="utf-8"
        )

        self.process = subprocess.Popen(
            ["adb", "logcat", "-v", "threadtime"],
            stdout=self.file_handle,
            stderr=subprocess.STDOUT,
        )

        return self.log_file

    def stop(self):
        if self.process is not None:
            self.process.terminate()

            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait()

            self.process = None

        if getattr(self, "file_handle", None):
            self.file_handle.close()
            self.file_handle = None
