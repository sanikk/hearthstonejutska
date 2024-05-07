from config import LOG_PATH
import json


class LogService:
    def __init__(self):
        self._log_path = LOG_PATH
        self._log_subdir = None
        self.set_subdir()

    def set_subdir(self):
        if not self._log_path or not self._log_path.is_dir():
            return False
        self._log_subdir = sorted(self._log_path.iterdir())[-1]
        if self._log_subdir:
            return True
        return False

    def get_log_subdir(self):
        return self._log_subdir

    def set_log_path(self, new_path):
        self._log_path = new_path
        return self.set_subdir()

    def get_log_path(self):
        return self._log_path

    def save_log_path(self):
        if self._log_path:
            with open('settings.ini', 'w') as f:
                f.write(json.dumps({'LOG_PATH': self._log_path}))
            return True
        return False
