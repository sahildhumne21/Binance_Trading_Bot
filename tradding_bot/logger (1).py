import logging
from datetime import datetime

def setup_logger():
    logger = logging.getLogger("BinanceBot")
    logger.setLevel(logging.INFO)

    # File handler
    fh = logging.FileHandler(f"bot_log_{datetime.now().strftime('%Y%m%d')}.log")
    fh.setLevel(logging.INFO)

    # Format: [TIME] LEVEL - message
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
