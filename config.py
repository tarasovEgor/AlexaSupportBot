from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
OPEN_AI_TOKEN = os.environ.get("OPEN_AI_TOKEN")
PROXY_URL = os.environ.get("PROXY_URL")
ZAMMAD_API_KEY = os.environ.get("ZAMMAD_API_KEY")
ZAMMAD_URL = os.environ.get("ZAMMAD_URL")