from ui.ui import UI
from service.log_service import LogService

print("starting service")
log_service = LogService()
print("starting ui")
ui = UI(log_service=log_service)
ui.mainloop()
