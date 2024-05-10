from ui.ui import UI
from service.log_service import LogService
from service.path_service import PathService

path_service = PathService()
log_service = LogService()
print("starting ui")
ui = UI(log_service=log_service, path_service=path_service)
ui.mainloop()
