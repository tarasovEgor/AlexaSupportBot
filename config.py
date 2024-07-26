from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
OPEN_AI_TOKEN = os.environ.get("OPEN_AI_TOKEN")
PROXY_URL = os.environ.get("PROXY_URL")