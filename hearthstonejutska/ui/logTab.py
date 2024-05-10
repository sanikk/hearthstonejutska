import queue
import tkinter
from tkinter.ttk import Frame, Label, Button, LabelFrame
from tkinter.filedialog import askdirectory


class LogPathTab:
    def __init__(self, master=None, log_service=None):
        self._frame = Frame(master=master)
        self._log_service = log_service
        self._ui = master

        self.log_path_label = None
        self.log_subdir_label = None

        self.output_box = tkinter.Text(master=self._frame)
        self.output_box.grid(row=2, column=0)
        self._get_log_path_box(master=self._frame).grid(row=1, column=0)

        if self._log_service.get_log_path():
            # pieni viive alkuun niin tämä ehtii nostaa kaiken ylös
            self.start_updater(200)

    def _get_log_path_box(self, master=None):
        container = LabelFrame(master=master)

        self.log_path_label = Label(master=container, text=self._log_service.get_log_path())
        log_path_dialog_button = Button(master=container, text='set path', command=self._log_path_dialog)
        log_path_save_button = Button(master=container, text='save path', command=self._log_service.save_log_path)

        self.log_path_label.grid(row=0, column=0)
        log_path_dialog_button.grid(row=0, column=1)
        log_path_save_button.grid(row=0, column=2)

        self.log_subdir_label = Label(master=container, text=self._log_service.get_log_subdir())
        self.log_subdir_label.grid(row=1, column=0)

        return container

    def _log_path_dialog(self):
        answer = askdirectory(mustexist=True, parent=self._frame)
        if answer and self._log_service.set_log_path(answer):
            self.log_path_label.config(text=str(answer))
            self.start_updater()

    def get_frame(self):
        return self._frame

    def grid(self):
        self._frame.grid()

    def start_updater(self, delay=50):
        self._ui.after(delay, self.after_callback)

    def after_callback(self):
        content = self._log_service.fetch()
        if content:
            print(f"ui.after_callback {content=}")
            self.output_box.insert('end', *content)
        self._ui.after(0, self.after_callback)
        self._frame.update_idletasks()

