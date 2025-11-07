from telegram import KeyboardButton, WebAppInfo


Token = 'TG_TOKEN'
File_Name = 'database/database.json'
DP_File_Name = 'database/dataphone.json'
WEB_APP_URL = "WEP_APP_URL"
wep_app_btn = KeyboardButton(text='🛍️ Buyurtma berish', web_app=WebAppInfo(url=WEB_APP_URL))