"""
Configurações do Bot
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Telegram
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

# Pluggy.ai
PLUGGY_CLIENT_ID = os.getenv("PLUGGY_CLIENT_ID", "")
PLUGGY_API_KEY = os.getenv("PLUGGY_API_KEY", "")

# Apex Seguidores
APEX_API_KEY = os.getenv("APEX_API_KEY", "")

# SMS-Activate
SMS_ACTIVATE_API_KEY = os.getenv("SMS_ACTIVATE_API_KEY", "")

# Admin
ADMIN_TELEGRAM_ID = int(os.getenv("ADMIN_TELEGRAM_ID", "0"))

# Google Sheets
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID", "")

# Validação
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN não configurado")

if not ADMIN_TELEGRAM_ID:
    raise ValueError("ADMIN_TELEGRAM_ID não configurado")
