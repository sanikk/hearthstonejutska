from tkinter.ttk import Frame, LabelFrame, Label, Button
from tkinter.filedialog import askdirectory


class PathTab:
    def __init__(self, master=None, path_service=None):
        self.frame = Frame(master=master)
        self._path_service = path_service
        self.log_path_label = None
        self.log_subdir_label = None

        self._get_log_path_box(master=self.frame).grid(row=1, column=0)

    def _get_log_path_box(self, master=None):
        container = LabelFrame(master=master)

        self.log_path_label = Label(master=container, text=self._path_service.get_log_path())
        log_path_dialog_button = Button(master=container, text='set path', command=self._log_path_dialog)
        log_path_save_button = Button(master=container, text='save path', command=self._path_service.save_log_path)

        Label(master=container, text='Log path').grid(row=0, column=0)
        self.log_path_label.grid(row=0, column=1)
        log_path_dialog_button.grid(row=0, column=2)
        log_path_save_button.grid(row=0, column=3)

        self.log_subdir_label = Label(master=container, text=self._path_service.get_subdir())
        Label(master=container, text='Used log subdir').grid(row=1, column=0)
        self.log_subdir_label.grid(row=1, column=1)
        subdir_reset_button = Button(master=container, text='reset subdir', command=self._set_subdir())
        subdir_reset_button.grid(row=1, column=2)
        return container

    def _log_path_dialog(self):
        answer = askdirectory(mustexist=True, parent=self.frame, initialdir=self._path_service.get_log_path() or '.')
        if answer and self._path_service.set_log_path(answer):
            self.log_path_label.config(text=str(answer))

    def _set_subdir(self):
        self._path_service.set_subdir()

    def get_frame(self):
        return self.frame

    def grid(self, row, column):
        self.frame.grid(row=row, column=column)
