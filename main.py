from bot import Bot

from bot import Bot  # Ensure this import works correctly and the Bot class is defined

# Your existing imports
import schedule
import time
import os
import logging
from config import SECONDS

# Define a logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the auto-delete function
def auto_delete_files(directory, age_in_seconds):
    now = time.time()
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_age = now - os.path.getctime(file_path)
            if file_age > age_in_seconds:
                try:
                    os.remove(file_path)
                    logger.info(f"Deleted {file_path}")
                except Exception as e:
                    logger.error(f"Failed to delete {file_path}: {e}")

# Schedule the auto-delete function
def job():
    auto_delete_files('/path/to/your/files', SECONDS)

schedule.every().hour.do(job)

if __name__ == "__main__":
    # Initialize and run the bot
    bot = Bot()
    
    # Ensure scheduling runs in a separate thread or within the main loop without blocking the bot
    while True:
        schedule.run_pending()
        time.sleep(1)
        bot.run()  # Ensure bot.run() is non-blocking or refactor if necessary


Bot().run()
