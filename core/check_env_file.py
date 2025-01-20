from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access variables
PARENT_FOLDER_ID = os.getenv("PARENT_FOLDER_ID")

