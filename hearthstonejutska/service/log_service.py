from pathlib import Path
from queue import Queue, Empty

from log_modules.dir_monitor import DirectoryMonitor


class LogService:
    def __init__(self, log_path: Path = None):
        self.data_queue = Queue()
        self.monitor = None

    # DIR_MONITOR/LOG_READER
    def _start_monitor(self):
        self.monitor = DirectoryMonitor(directory_path=self._log_subdir, data_queue=self.data_queue)
        self.monitor.run()

    def fetch(self):
        try:
            content = self.data_queue.get(block=False)
            print(f"log_service {content=}")
            if content:
                return content
        except Empty:
            pass

        return None



