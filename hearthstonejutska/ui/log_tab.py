import queue
import tkinter
from tkinter.ttk import Frame, Label, Button, LabelFrame



class LogTab:
    def __init__(self, master=None, log_service=None):
        self._frame = Frame(master=master)
        self._log_service = log_service
        self._ui = master

        self.log_path_label = None
        self.log_subdir_label = None

        self.output_box = tkinter.Text(master=self._frame)
        self.output_box.grid(row=0, column=0)

        #if self._log_service.get_log_path():
            # pieni viive alkuun niin tämä ehtii nostaa kaiken ylös
        #    self.start_updater(200)

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

