from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes
import schedule, time, os, asyncio

TOKEN = os.getenv("TOKEN_INTELITECH")
CANAL_ID = "@intelitechofertas"

if not TOKEN:
    raise ValueError("TOKEN não encontrado ou inválido.")

app = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Digite /promo para ver as melhores ofertas!")
    
async def promo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = """
    🔥 *Oferta Especial!* 🔥
    👉 [Monitor Acer](https://www.mercadolivre.com.br/monitor-gamer-kg241y-ebii-238h-hdmi-vga-lcd-238-100hz/p/MLB35374778?pdp_filters=item_id:MLB4863711736#polycard_client=recommendations_pdp-pads-up&reco_backend=pdp_pads_up_merge_rars_v2_with_default&reco_client=pdp-pads-up&reco_item_pos=0&reco_backend_type=low_level&reco_id=18eb1d44-46ff-4922-9d61-1f414cefe37b&wid=MLB4863711736&sid=recos&is_advertising=true&ad_domain=PDPDESKTOP_UP&ad_position=1&ad_click_id=MWExZDc5NDUtNjYwYS00ZjQzLWE3ZTktMjBhNzE4NjdkNzI5)
    💰 *Desconto exclusivo!*
    """
    await update.message.reply_text(mensagem, parse_mode="Markdown")

async def produtos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ofertas = """
🔹 *Curso de Programação* - [Comprar](https://www.alura.com.br)
🔹 *E-book de Investimentos* - [Comprar](https://www.amazon.com.br/Perigoso-Este-livro-cont%C3%A9m-coelhos/dp/6526113427?pf_rd_p=5dac4ebf-f085-41f6-b0dd-1ec3fea5d8c2&pf_rd_r=AVTA08VF8AAXDNS66A6C&ref_=sc-insirasuareftagaqui_6526113427)
🔹 *Ferramenta SEO* - [Comprar](https://www.google.com)
"""
    await update.message.reply_text(ofertas, parse_mode="Markdown")

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("promo", promo))
app.add_handler(CommandHandler("produtos", produtos))

bot = Bot(token=TOKEN)

async def enviar_promo():
    await bot.send_message(CANAL_ID, "🔥 Oferta do Dia: [Curso Python](https://www.hotmart.com/curso123) 🔥")

async def scheduler():
    while True:
        schedule.run_pending()
        await asyncio.sleep(60)

schedule.every().day.at("12:00").do(lambda: asyncio.create_task(enviar_promo()))

async def main():
    await asyncio.gather(
        app.run_polling(),
        scheduler()
    )

if __name__ == '__main__':
    asyncio.run(main())