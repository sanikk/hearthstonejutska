from doctest import debug
from tkinter import Tk
from tkinter.ttk import Notebook
from ui.log_tab import LogTab
from ui.path_tab import PathTab


class UI:
    def __init__(self, master=None, log_service=None, path_service=None):
        self.frame = Tk()
        self.frame.geometry("800x600")
        self.path_tab = None
        self.log_tab = None

        # prolly not needed here
        self.log_service = log_service
        self.path_service = path_service

        self._menu = self.get_menu_bar(master=self.frame, log_service=log_service, path_service=path_service)
        self._menu.grid(row=0, column=0)

    def tab_switch_event_handler(self, event):
        selected_tab = event.widget.tab(event.widget.select(), 'text')
        if selected_tab == 'path tab':
            pass
        if selected_tab == 'log tab':
            pass

    def get_menu_bar(self, master=None, log_service=None, path_service=None):
        menu_bar = Notebook(master=master)
        self.path_tab = PathTab(master=master, path_service=path_service)
        menu_bar.add(self.path_tab.get_frame(), text='path tab')
        self.log_tab = LogTab(master=master, log_service=log_service)
        menu_bar.add(self.log_tab.get_frame(), text='log tab')
        # menu_bar.add(self.settings_tab(master=master), text='settings')
        return menu_bar

    def mainloop(self):
        self.frame.mainloop()
