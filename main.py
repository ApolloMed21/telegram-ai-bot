from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from transformers import pipeline

# AI modelini yükle
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

# /start komutu
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Merhaba! Ben bir yapay zeka botuyum. Konuşalım mı? 😊")

# Kullanıcının mesajına yanıt ver
async def reply(update: Update, context: CallbackContext):
    user_message = update.message.text
    response = chatbot(user_message, max_length=100, num_return_sequences=1, pad_token_id=50256)
    ai_message = response[0]['generated_text']
    await update.message.reply_text(ai_message)

# Ana fonksiyon
def main():
    TOKEN = "BURAYA_BOT_TOKENINI_YAZ"  # <-- Burayı değiştir
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    app.run_polling()

if __name__ == '__main__':
    main()
