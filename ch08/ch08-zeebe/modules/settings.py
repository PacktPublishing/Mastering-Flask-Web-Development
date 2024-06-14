import os
from pathlib import Path

from modules.logger import error_handler, log_decorator

class Zeebe:
    ZEEBE_HOSTNAME = "zeebe"
    ZEEBE_PORT = 26500
    ZEEBE_MAX_CONNECTION_RETRIES = -1
    BPMN_DUMP_PATH = Path("./bpmn")
    TASK_DEFAULT_PARAMS = {
        "exception_handler": error_handler,
      
        "before": [log_decorator],
        "after": [log_decorator],
    }