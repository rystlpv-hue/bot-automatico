import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler
from telegram.constants import ParseMode
from collections import deque
import json
import os

# ====== CONFIGURAÇÕES ======
TOKEN = "9063985756:AAEsOahAsvPfi_j3YH8fXAysbI0ptj_Wx9A"
CHANNEL_ID = -1003926830337
ADMIN_USERNAME = "mariansxj"
POST_INTERVAL = 15 * 60  # 15 minutos

DEFAULT_CAPTION = """🔥 Conteúdo exclusivo

👉 Link nos destaques"""

# ===========================

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

queue = deque()
QUEUE_FILE = "queue.json"

def