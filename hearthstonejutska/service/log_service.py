import json
from pathlib import Path
from config import LOG_PATH

from log_modules.dir_monitor import DirectoryMonitor

class LogService:
    def __init__(self, log_path=None):
        self._log_path = log_path or LOG_PATH
        self._log_subdir = None
        self._log_file = None
        self.set_subdir()

        self.monitor = None

    # LOG FILE/SUBDIR/PATH
    def set_file(self):
        # not used right now
        if not self._log_subdir:
            return
        self._log_file = Path(self._log_subdir, 'Hearthstone.log')

    def set_subdir(self):
        print(f"{self._log_path=}")
        if not self._log_path or not self._log_path.is_dir():
            return False
        self._log_subdir = sorted(self._log_path.iterdir())[-1]
        # if self._log_subdir:
        #     self.set_file()
        self._start_monitor()

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

    # DIR_MONITOR/LOG_READER
    def _start_monitor(self):
        self.monitor = DirectoryMonitor(directory_path=self._log_subdir, log_service, log_reader)
        pass