import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
BASE_URL = "https://api.github.com"

if not GITHUB_TOKEN:
    raise Exception("GITHUB_TOKEN not found in environment variables")