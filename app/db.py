import json

from app.config import File_Name, DP_File_Name


def save_database(data: dict):
    with open(File_Name, "w") as f:
        json.dump(data, f, indent=4)


def save_dataphone(data: dict):
    with open(DP_File_Name, "w") as f:
        json.dump(data, f, indent=4)


def add_user(chat_id: str | int, full_name: str, username: str | None = None):
    chat_id = str(chat_id)
    try:
        with open(File_Name, "r") as f:
            data = json.load(f)
    except:
        data = {}
        
    if chat_id not in data:
        data[chat_id] = {
            'full_name': full_name,
            'username': username
        }
        save_database(data)
        return True
    return False


def add_contact(phone_number: int | str, first_name: str, user_id: int | str):
    phone_number = str(phone_number)
    
    try:
        with open(DP_File_Name, "r") as f:
            dataPhone = json.load(f)
    except:
        dataPhone = {}
        
    if str(user_id) not in dataPhone:
        dataPhone[user_id] = {
            'first_name': first_name,
            'phone_number': phone_number
        }
        save_dataphone(dataPhone)
        
        
def checkPhoneNumber(chat_id: str | int) -> bool:
    chat_id = str(chat_id)
    try:
        with open(DP_File_Name, "r") as f:
            data = json.load(f)
    except:
        data = {}
        
    if str(chat_id) not in data:
        return True
    return False


