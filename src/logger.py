import logging
import os
from datetime import datetime

# Generate a log file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

# Define the path where the log file will be stored
# os.getcwd() returns the current working directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the directory for logs if it does not exist, and avoid raising an error if it already exists
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

# Construct the full path to the log file
LOG_FILE_PATH = logs_path

# Configure the basic logging settings
logging.basicConfig(
    # Specify the file where the logs will be written
    filename=LOG_FILE_PATH,
    
    # Define the format of the log messages
    # %(asctime)s: Timestamp of when the log message was created
    # %(lineno)d: Line number where the log message was issued
    # %(name)s: Name of the logger
    # %(levelname)s: Severity level of the log message (e.g., INFO, WARNING, ERROR)
    # %(message)s: The actual log message
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    
    # Set the minimum logging level to INFO, meaning only INFO and higher severity messages will be logged
    level=logging.INFO
)



#this is just to test if my logger is working or not
if __name__=="__main__":
    logging.info("Logging has started")
