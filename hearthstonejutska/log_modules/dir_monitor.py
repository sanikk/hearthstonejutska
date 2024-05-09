import re
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path

# from log_modules.log_watcher import LogFileReader
from log_file_reader import LogFileReader


class DirectoryMonitor:

    def __init__(self, directory_path, log_service=None, log_reader=None):
        self.observer = Observer()
        self.directory_path = directory_path
        self.log_service = log_service
        self.log_reader = log_reader or LogFileReader(logfile_path=Path(directory_path, 'Hearthstone.log'))

    def run(self):
        self.observer.schedule(event_handler=Handler(logfile_reader=self.log_reader), path=self.directory_path)
        self.observer.start()
        try:
            while True:
                sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()

        self.observer.join()


class Handler(FileSystemEventHandler):
    def __init__(self, logfile_reader):
        super().__init__()
        self.logfile_reader = logfile_reader

    def on_modified(self, event) -> None:
        if event.is_directory:
            return None

        if 'Hearthstone.log' in event.src_path:
            print(f"dir_monitor.Handler Watchdog received modified event - {event.src_path}.")
            content = self.logfile_reader.read_log()
            print(f"{content=}")

if __name__ == '__main__':
    le_path = Path('/home/karpo/hd/SteamLibrary/steamapps/common/HS/Hearthstone/Logs/Hearthstone_2024_05_09_12_00_01/')
    monitor = DirectoryMonitor(directory_path=le_path)
    monitor.run()

m = re.search(r'(?<=-)\w+', 'spam-egg')
m.group(0)
'egg'
