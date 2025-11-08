from telegram.ext import (
    Updater, 
    CommandHandler, 
    MessageHandler,
    Filters,
)

from app.handlers import (
    start, 
    help,
    sendMessage,
    saveContact,
    myOrders,
    settings,
    editLanguage,
    editPhone,
    back,
    about,
    feedback,
    feedbackEnding
)

try:
    from app.config import Token
except ImportError:
    from app.config_simple import Token

updater = Updater(Token)
dispatcher = updater.dispatcher


# commandHendler
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))

# messangHendler
dispatcher.add_handler(MessageHandler(Filters.contact, saveContact))
dispatcher.add_handler(MessageHandler(Filters.text("🇺🇿 O'zbekcha"), back))
dispatcher.add_handler(MessageHandler(Filters.text('🇷🇺 Pyccкий'), back))
dispatcher.add_handler(MessageHandler(Filters.text('🇺🇸 English'), back))
dispatcher.add_handler(MessageHandler(Filters.text('📦Buyurtmalarim'), myOrders))
dispatcher.add_handler(MessageHandler(Filters.text('⚙️Sozlamalar'), settings))
dispatcher.add_handler(MessageHandler(Filters.text("🌐 Tilni o'zgartirish"), editLanguage))
dispatcher.add_handler(MessageHandler(Filters.text("📞 Telefon raqamingizni o'zgartiring"), editPhone))
dispatcher.add_handler(MessageHandler(Filters.text("ℹ️Biz haqimizda"), about))
dispatcher.add_handler(MessageHandler(Filters.text("✍️ Fikr qoldirish"), feedback))
dispatcher.add_handler(MessageHandler(Filters.text("⬅️ Orqaga"), back))
dispatcher.add_handler(MessageHandler(Filters.text &~ Filters.command, feedbackEnding))

updater.start_polling()
updater.idle()