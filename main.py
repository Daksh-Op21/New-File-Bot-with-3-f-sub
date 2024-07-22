from bot import Bot

# Your existing imports
import schedule
import time
from config import SECONDS

# Define the auto-delete function here or import it if it's in another file
def auto_delete_files(directory, age_in_seconds):
    # (Function code as provided above)

# Schedule the auto-delete function
def job():
    auto_delete_files('/path/to/your/files', SECONDS)

schedule.every().hour.do(job)

if __name__ == "__main__":
    # Your existing bot initialization code
    while True:
        schedule.run_pending()
        time.sleep(1)

Bot().run()
