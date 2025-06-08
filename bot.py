import telegram
from telegram.ext import Updater, CommandHandler

BOT_TOKEN = '7281967575:AAHCXsMmKwiGNNEBvRxCj30LBzfi2TrMnL0'

def start(update, context):
    update.message.reply_text("👋 Hello Darrell. You will now receive crypto scalp signals here.")

def btcnow(update, context):
    update.message.reply_text("📈 BTC/USD: Buy at $68,250, SL: $68,000, TP: $68,800")

updater = Updater(BOT_TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("btcnow", btcnow))

updater.start_polling()
updater.idle()
