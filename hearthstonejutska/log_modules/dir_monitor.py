from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path

from log_modules.log_reader import LogReader


class DirectoryMonitor:

    def __init__(self, directory_path, log_service=None, log_reader=None):
        self.observer = Observer()
        self.directory_path = directory_path
        self.log_service = log_service
        self.log_reader = log_reader or LogReader(logfile_path=Path(directory_path, 'Hearthstone.log'))

    def run(self):
        self.observer.schedule(
            event_handler=Handler(log_reader=self.log_reader, log_service=self.log_service),
            path=self.directory_path
        )
        self.observer.start()

    def cleanup(self):
        self.observer.join()


class Handler(FileSystemEventHandler):
    def __init__(self, log_reader=None, log_service=None):
        super().__init__()
        self.log_reader = log_reader
        self.log_service = log_service

    def on_modified(self, event) -> None:
        if event.is_directory:
            return None

        if 'Hearthstone.log' in event.src_path:
            content = self.log_reader.read_log()
            if content:
                # this should be sync/async and threadsafe
                self.log_service.add_content(content=content)


if __name__ == '__main__':
    le_path = Path('/home/karpo/hd/SteamLibrary/steamapps/common/HS/Hearthstone/Logs/Hearthstone_2024_05_09_15_07_58/')
    monitor = DirectoryMonitor(directory_path=le_path)
    monitor.run()
