import queue
import tkinter
from tkinter.ttk import Frame, Label, Button, LabelFrame
from tkinter.filedialog import askdirectory


class LogPathTab:
    def __init__(self, master=None, log_service=None):
        self._frame = Frame(master=master)
        self._log_service = log_service

        self.log_path_label = None
        self.log_subdir_label = None

        self._get_log_path_box(master=self._frame).grid(row=1, column=0)

        self.output_box = tkinter.Text(master=self._frame)
        self.output_box.grid(row=2, column=0)

    def _get_log_path_box(self, master=None):
        container = LabelFrame(master=master)
        self.log_path_label = Label(master=container, text=self._log_service.get_log_path())
        self.log_path_label.grid(row=0, column=0)
        log_path_dialog_button = Button(master=container, text='set path', command=self._set_log_path)
        log_path_dialog_button.grid(row=0, column=1)
        log_path_save_button = Button(master=container, text='save path', command=self._log_service.save_log_path)
        log_path_save_button.grid(row=0, column=2)

        self.log_subdir_label = Label(master=container, text=self._log_service.get_log_subdir())
        self.log_subdir_label.grid(row=1, column=0)
        return container

    def _set_log_path(self):
        answer = askdirectory(mustexist=True, parent=self._frame)
        if answer and self._log_service.set_log_path(answer):
            self.log_path_label.config(text=str(answer))

    def get_frame(self):
        return self._frame

    def grid(self):
        self._frame.grid()

