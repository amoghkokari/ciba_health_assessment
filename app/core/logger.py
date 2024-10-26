import logging
import sys
from app.core.config import config

def setup_logger(name: str = "app_logger") -> logging.Logger:
    """
    Configures and returns a logger instance with the specified name.

    Args:
        name (str): Name of the logger instance.

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create logger with specified name
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, config.log_level.upper(), "INFO"))

    # Avoid duplicate log entries
    if not logger.hasHandlers():
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(getattr(logging, config.log_level.upper(), "INFO"))

        # Define log message format
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        logger.addHandler(console_handler)

    return logger

# Initialize and export a default logger instance
logger = setup_logger()
