import os
import logging

log_level = os.environ.get("LOG_LEVEL", "INFO")

if log_level == "INFO":
    LOG_LEVEL = logging.INFO
elif log_level == "DEBUG":
    LOG_LEVEL = logging.DEBUG
elif log_level == "NOTSET":
    LOG_LEVEL = logging.NOTSET
elif log_level == "WARNING":
    LOG_LEVEL = logging.WARNING
elif log_level == "ERROR":
    LOG_LEVEL = logging.ERROR
elif log_level == "CRITICAL":
    LOG_LEVEL = logging.CRITICAL
else:
    LOG_LEVEL = logging.NOTSET


LOG_DIR = os.environ.get("LOG_DIR", "")