from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os, asyncio, logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

TOKEN = os.getenv("TOKEN_INTELITECH")
CANAL_ID = "@intelitechofertas"

if not TOKEN:
    raise ValueError("TOKEN não encontrado ou inválido.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Digite /promo para ver as melhores ofertas!")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    loop = asyncio.get_running_loop()
    await app.run_polling()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except RuntimeError:
        logging.error("Erro ao executar o loop de eventos.")
