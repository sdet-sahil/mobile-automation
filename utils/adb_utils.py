
import subprocess


class AdbUtils:

    @staticmethod
    def run(*args, timeout=30):
        command = ["adb", *args]

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=timeout,
                check=True,
            )
            return result.stdout.strip()

        except subprocess.CalledProcessError as exc:
            raise RuntimeError(
                f"ADB command failed: {exc.stderr.strip()}"
            ) from exc

        except subprocess.TimeoutExpired as exc:
            raise RuntimeError(
                f"ADB command timed out: {command}"
            ) from exc

    @classmethod
    def get_connected_devices(cls):
        output = cls.run("devices")
        devices = []

        for line in output.splitlines()[1:]:
            parts = line.split()

            if len(parts) == 2 and parts[1] == "device":
                devices.append(parts[0])

        return devices

    @classmethod
    def get_device_id(cls):
        devices = cls.get_connected_devices()

        if not devices:
            raise RuntimeError(
                "No authorized Android device found. "
                "Check USB debugging and run adb devices."
            )

        if len(devices) > 1:
            raise RuntimeError(
                "Multiple devices found. Set DEVICE_ID explicitly."
            )

        return devices[0]

    @classmethod
    def open_url(cls, url, device_id=None):
        command = []

        if device_id:
            command.extend(["-s", device_id])

        command.extend([
            "shell", "am", "start",
            "-a", "android.intent.action.VIEW",
            "-d", url,
        ])

        return cls.run(*command)

    @classmethod
    def force_stop_app(cls, package_name, device_id=None):
        command = []

        if device_id:
            command.extend(["-s", device_id])

        command.extend([
            "shell", "am", "force-stop", package_name
        ])

        return cls.run(*command)

    @classmethod
    def start_logcat(cls, output_file, device_id=None):
        """Start continuous ADB log capture."""
        command = ["adb"]

        if device_id:
            command.extend(["-s", device_id])

        command.extend([
            "logcat",
            "-v", "threadtime",
        ])

        path = Path(output_file)
        path.parent.mkdir(parents=True, exist_ok=True)

        file_handle = path.open("w", encoding="utf-8")

        try:
            process = subprocess.Popen(
                command,
                stdout=file_handle,
                stderr=subprocess.STDOUT,
            )
        except Exception:
            file_handle.close()
            raise

        return process, file_handle

    @classmethod
    def stop_logcat(cls, process, file_handle):
        """Stop log capture and close the output file."""
        if process and process.poll() is None:
            process.terminate()

            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()

        if file_handle and not file_handle.closed:
            file_handle.close()

    @classmethod
    def get_app_pid(cls, package_name, device_id=None):
        """Return the app PID, or None if it is not running."""
        command = []

        if device_id:
            command.extend(["-s", device_id])

        command.extend([
            "shell", "pidof", "-s", package_name
        ])

        try:
            output = cls.run(*command)
            return output or None
        except RuntimeError:
            return None
