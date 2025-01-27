from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os, asyncio, logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("TOKEN_INTELITECH")
CANAL_ID = "@intelitechofertas"

if not TOKEN:
    raise ValueError("TOKEN não encontrado ou inválido.")

def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text("Olá! Digite /promo para ver as melhores ofertas!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    loop = asyncio.get_running_loop()
    app.run_polling()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except RuntimeError:
        logging.error("Erro ao executar o loop de eventos.")
    
