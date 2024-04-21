from telegram.ext import Updater, CommandHandler
from googletrans import Translator

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот-переводчик с русского на английский. Используй команду /translate для перевода текста.")

# Функция перевода текста с русского на английский
def translate_to_english(update, context):
    if len(context.args) == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Использование: /translate <текст>")
    else:
        text = ' '.join(context.args)
        print(text)
        translator = Translator()
        translated_text = translator.translate(text, src='ru', dest='en').text
        context.bot.send_message(chat_id=update.effective_chat.id, text=translated_text)

# Главная функция
def main():
    # Замените 'YOUR_TELEGRAM_BOT_TOKEN' на ваш токен бота
    updater = Updater("6909461627:AAEdMB1un71Qebre1MycnkNTB57hFbnrTLQ", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("translate", translate_to_english))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
