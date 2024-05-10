# toistaiseksi sleep/wait timestä
import time
from pathlib import Path


class LogReader:
    """
    Tämä toimii koska se ei varaa tuota tiedostoa.

    :param logfile_path:
    :return:
    """

    def __init__(self, logfile_path: Path):
        """
        :param logfile_path: directory containing logfile as Path object.
        :param logfile_name:  name of logfile to watch, shouldnt change. Should accept Path or string.
        """
        self.logfile_path = logfile_path
        self.last_position = logfile_path.stat().st_size

    def read_log(self):
        with open(self.logfile_path, 'r') as logfile:
            if self.logfile_path.stat().st_size != self.last_position:
                logfile.seek(self.last_position)
                content = logfile.read().splitlines()
                if content:
                    print("log_reader has content!!")
                # print(f"log_reader {content=}")
                self.last_position = self.logfile_path.stat().st_size
                return [line for line in content if line.startswith('E')]
