import asyncio
import json
from pathlib import Path

from config import LOG_PATH
# from log_watcher import async_file_monitor

class LogService:
    def __init__(self):
        self._log_path = LOG_PATH
        self._log_subdir = None
        self._log_file = None
        self.set_subdir()

    async def start_monitor(self):
        with open(Path(self._log_subdir, 'Hearthstone.log')) as log_file:
            gen = async_file_monitor(log_file)
            while True:
                line = await anext(gen)
                print(line)

    def execute(self, cmd, stdout, stderr):
        pass

    async def _stream_subprocess(self):
        # asyncio.create_subprocess_exec()
        pass

    def set_file(self):
        if not self._log_subdir:
            return
        self._log_file = Path(self._log_subdir, 'Hearthstone.log')

    def set_subdir(self):
        print(f"{self._log_path=}")
        if not self._log_path or not self._log_path.is_dir():
            return False
        self._log_subdir = sorted(self._log_path.iterdir())[-1]
        if self._log_subdir:
            self.set_file()



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
