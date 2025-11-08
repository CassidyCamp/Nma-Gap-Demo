from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import CallbackContext

from app.db import add_user, checkPhoneNumber, add_contact
try:
    from app.config import WEB_APP_URL, wep_app_btn
except ImportError:
    from app.config_simple import WEB_APP_URL, wep_app_btn


feedback_mode = {}


def showLenguage() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
            keyboard=[
                ["🇺🇿 O'zbekcha", '🇷🇺 Pyccкий'],
                ['🇺🇸 English']
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )


def showMainMenu(button) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            [button],
            ['📦Buyurtmalarim', '⚙️Sozlamalar'],
            ['ℹ️Biz haqimizda', '✍️ Fikr qoldirish']
        ],
        resize_keyboard=True,
    )


def start(update: Update, context: CallbackContext):
    if not add_user(update.message.from_user.id, update.message.from_user.full_name, update.message.from_user.username):
        update.message.reply_text(
            text=f'Assalomu alaykum {update.message.from_user.full_name}!',
            reply_markup=showLenguage()
        )
    else:
        update.message.reply_text(
            text=f'Assalomu alaykum {update.message.from_user.full_name}!',
            reply_markup=showMainMenu(wep_app_btn)
        )
    
    
def help(update: Update, context: CallbackContext):
    update.message.reply_text('hello')


def uzLanguage():
    pass


def ruLanguage():
    pass


def enLanguage():
    pass

# getPhoneNumber
def getPhoneNumber(update: Update, context: CallbackContext):
    button = KeyboardButton('Telefon raqam yuborish', request_contact=True)
    update.message.reply_text(
        text='Iltimos, telefon raqamingizni yuboring',
        reply_markup=ReplyKeyboardMarkup(
            [
                [button]
            ],
            resize_keyboard=True,
            one_time_keyboard=True,
        )
    )
        

def sendMessage(update: Update, context: CallbackContext):
    if checkPhoneNumber(update.message.from_user.id):
        getPhoneNumber(update, context)
    else:
        update.message.reply_text(text="Xabaringiz uchun tashakkur, imkon qadar tezroq siz bilan bog'lanamiz.")


def myOrders(update: Update, context: CallbackContext):
    if not checkPhoneNumber(update.message.from_user.id):
        update.message.reply_text(text='Sizda hali birorta ham buyurtma yo`q')
    else:
        getPhoneNumber(update, context)


def settings(update: Update, context: CallbackContext):
    if not checkPhoneNumber(update.message.from_user.id):
        update.message.reply_text(
            text='Sozlamalar',
            reply_markup=ReplyKeyboardMarkup(
                [
                    ["🌐 Tilni o'zgartirish"],
                    ["📞 Telefon raqamingizni o'zgartiring"],
                    ['⬅️ Orqaga']
                ]
            )
        )
    else:
        getPhoneNumber(update, context)


def editLanguage(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="Tilni tanlang",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                ["🇺🇿 O'zbekcha", '🇷🇺 Pyccкий'],
                ['🇺🇸 English'],
                ['⬅️ Orqaga']
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )


def editPhone(update: Update, context: CallbackContext):
    button = KeyboardButton('Mening telefon raqamim', request_contact=True)
    update.message.reply_text(
        text='Iltimos, telefon raqamingizni yuboring',
        reply_markup=ReplyKeyboardMarkup(
            [
                [button],
                ['⬅️ Orqaga']
            ],
            resize_keyboard=True,
            one_time_keyboard=True,
        )
    )


def back(update: Update, context: CallbackContext):
    if not checkPhoneNumber(update.message.from_user.id):
        update.message.reply_text(
            text='🏠 Asosiy Menu',
            reply_markup=showMainMenu(wep_app_btn)
        )
    else:
        getPhoneNumber(update, context)


def about(update: Update, context: CallbackContext):
    if not checkPhoneNumber(update.message.from_user.id):
        update.message.reply_text(text='shu yerda joylashganmiz')
        update.message.reply_text(text='Email: abror4work@gmail.com')
    else:
        getPhoneNumber(update, context)


def feedback(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if not checkPhoneNumber(update.message.from_user.id):
        feedback_mode[user_id] = True
        update.message.reply_text(
            text="""Buyurtma berish uchun asosiy menyudagi “Buyurtma” tugmasidan foydalaning.\nBiz sizning fikr-mulohazalaringizni juda qadrlaymiz! Buyurtma berganingizdan so'ng, o'z fikr va mulohazalaringizni shu yerda qoldirishingiz mumkin""",
            reply_markup=ReplyKeyboardMarkup(
                [
                    ['⬅️ Orqaga']
                ],
                resize_keyboard=True
            )
        )
        feedback_mode[update.message.from_user.id] = True
    else:
        getPhoneNumber(update, context)


def feedbackEnding(update: Update, context: CallbackContext):
    if not checkPhoneNumber(update.message.from_user.id):
        user_id = update.message.from_user.id
        text = update.message.text
        if feedback_mode.get(user_id):
            if text == '⬅️ Orqaga':
                feedback_mode[user_id] = False
                back(update, context)
            else:
                update.message.reply_text("Fikr qoldirganingiz uchun rahmat!")
                feedback_mode[user_id] = False
                back(update, context)
        else:
            sendMessage(update, context)
            back(update, context)
    else:
        sendMessage(update, context)
    feedback_mode[update.message.from_user.id] = False


def saveContact(update: Update, context: CallbackContext):
    contact = update.message.contact
    add_contact(contact.phone_number, contact.first_name, contact.user_id)
    update.message.reply_text(
        text='✅ Sizning telefon raqamingiz muvaffaqiyatli saqalandi',
        reply_markup=showMainMenu(wep_app_btn)
    )