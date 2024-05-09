from ui.ui import UI
from service.log_service import LogService


log_service = LogService()
ui = UI(log_service=log_service)
ui.mainloop()
