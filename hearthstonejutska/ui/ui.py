from tkinter import Tk
from tkinter.ttk import Notebook
from ui.logTab import LogPathTab


class UI:
    def __init__(self, master=None, log_service=None):
        self.frame = Tk()
        self.frame.geometry("800x600")
        self.log_tab = None
        self.log_service = log_service

        self._menu = self.get_menu_bar(master=self.frame, log_service=log_service)
        self._menu.grid(row=0, column=0)

    def tab_switch_event_handler(self, event):
        selected_tab = event.widget.tab(event.widget.select(), 'text')
        if selected_tab == 'log dir tab':
            pass

    def get_menu_bar(self, master=None, log_service=None, syncqueue=None):
        menu_bar = Notebook(master=master)
        self.log_tab = LogPathTab(master=master, log_service=log_service)
        menu_bar.add(self.log_tab.get_frame(), text='log dir tab')
        # menu_bar.add(self.settings_tab(master=master), text='settings')
        return menu_bar

    def mainloop(self):
        self.frame.mainloop()
