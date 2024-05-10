from pathlib import Path
import json

from config import LOG_PATH


class PathService:
    def __init__(self, log_path=None):
        self._log_path = log_path or LOG_PATH
        self._log_subdir = None
        self._log_file = None
        self.set_subdir()

    def set_subdir(self):
        if not self._log_path or not self._log_path.is_dir():
            return False
        self._log_subdir = str(sorted(self._log_path.iterdir())[-1]).split('Hearthstone/Logs')[1]

    def get_subdir(self):
        return self._log_subdir

    def set_log_path(self, new_path: str = None):
        self._log_path = Path(new_path)
        return self.set_subdir()

    def get_log_path(self):
        return self._log_path

    def save_log_path(self):
        if self._log_path:
            with open('settings.ini', 'w') as f:
                f.write(json.dumps({'LOG_PATH': str(self._log_path)}))
            return True
        return False

    def _set_file(self):
        # not used right now
        if not self._log_subdir:
            return
        self._log_file = Path(self._log_subdir, 'Hearthstone.log')
