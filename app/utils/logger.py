from loguru import logger
import sys
from pathlib import Path

Path("logs").mkdir(exist_ok=True)

logger.remove()

logger.add(
    sys.stdout,
    colorize=True,
    level="INFO",
)

logger.add(
    "logs/bot.log",
    rotation="10 MB",
    compression="zip",
    level="INFO",
)

log = logger

from app.utils.logger import log

log.info("Бот запущен")