import os
import sys
import logging

# Logging format string
logging_str = "[%(asctime)s:%(levelname)s:%(module)s:%(message)s:]"

log_dir = 'logs'
log_filepath = os.path.join(log_dir, "running_logs.log")

# Ensure the log directory exists, or create it
try:
    os.makedirs(log_dir, exist_ok=True)
except PermissionError as e:
    print(f"PermissionError: Unable to create the log directory. {e}")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred while creating the log directory: {e}")
    sys.exit(1)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # Log to file
        logging.StreamHandler(sys.stdout)   # Log to console
    ]
)

logger = logging.getLogger('cnnClassifierLogger')