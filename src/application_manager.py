import subprocess


class ApplicationManager:
    def __init__(self, application_path: str) -> None:
        self.application_path = application_path
        self.process = None

    def open_app(self) -> None:
        if not self.process:
            self.process = subprocess.Popen([self.application_path])

    def close_app(self) -> None:
        if self.process:
            self.process.terminate()
        self.process = None
