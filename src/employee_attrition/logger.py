import logging
from pathlib import Path
from datetime import datetime

LOG_DIR_NAME = "logs"

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

LOG_DIR = Path(LOG_DIR_NAME)
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE_PATH = LOG_DIR / LOG_FILE

LOG_FORMAT = "[%(asctime)s] %(levelname)s | %(name)s | %(message)s"

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger("employee_attrition")