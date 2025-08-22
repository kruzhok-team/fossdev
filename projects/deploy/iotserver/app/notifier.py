import telebot
import os
import requests


# Load environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Validate environment variables
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is not set in environment variables.")

IOT_SERVICE_HOST = os.getenv("IOT_SERVICE_HOST", "http://localhost")
IOT_SERVICE_PORT = os.getenv("IOT_SERVICE_PORT", "8008")

REGISTER_USER_URL = f"{IOT_SERVICE_HOST}:{IOT_SERVICE_PORT}/register_user"
REMOVE_USER_URL = f"{IOT_SERVICE_HOST}:{IOT_SERVICE_PORT}/remove_user"
ADD_DEVICE_URL = f"{IOT_SERVICE_HOST}:{IOT_SERVICE_PORT}/link_device"
GET_USERS_URL = f"{IOT_SERVICE_HOST}:{IOT_SERVICE_PORT}/users"
IDENTIFY_USERS_URL = f"{IOT_SERVICE_HOST}:{IOT_SERVICE_PORT}/identify_user"

# Load environment variables
TELEGRAM_CHAT_ID = None
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if TELEGRAM_CHAT_ID:
    chat_ids = [int(TELEGRAM_CHAT_ID)]
else:
    chat_ids = []

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['chatid'])
def send_chatid(message: telebot.types.Message) -> None:
    bot.reply_to(message, f"Your chat id is {message.chat.id}")


@bot.message_handler(commands=['start'])
def handle_start(message: telebot.types.Message):
    payload = {"chat_id": message.chat.id, "username": ""}
    response = requests.post(IDENTIFY_USERS_URL, json=payload)
    if response.status_code == 200:
        user_data = response.json()
        resp_msg = f"Hello {user_data['username']}." \
            f" You are already registered! Your role: {user_data['role']}"
        bot.reply_to(message, resp_msg)
    else:
        bot.reply_to(message, "Welcome! Please provide your username.")
        bot.register_next_step_handler(message, register_user)

def register_user(message: telebot.types.Message):
    payload = {"chat_id": message.chat.id, "username": message.text}
    response = requests.post(REGISTER_USER_URL, json=payload)
    if response.status_code == 200:
        bot.reply_to(message, "Registration successful! Your role is 'manager'.")
    else:
        bot.reply_to(message, "Error registering user. Please try again later.")

@bot.message_handler(commands=['forget_me'])
def handle_start(message: telebot.types.Message):
    payload = {"chat_id": message.chat.id, "username": ""}
    response = requests.post(IDENTIFY_USERS_URL, json=payload)
    if response.status_code == 200:
        user_data = response.json()
        remove_user(message, user_data["user_id"])
    else:
        bot.reply_to(message, "You are not registered.")

def remove_user(message: telebot.types.Message, user_id: str):
    response = requests.delete(f"{REMOVE_USER_URL}/{user_id}")
    if response.status_code == 200:
        bot.reply_to(message, "You are sucessfully removed from the system")
    else:
        bot.reply_to(message, "Error removing user. Please try again later.")

@bot.message_handler(commands=['help'])
def handle_help(message: telebot.types.Message):
    help_message = (
        "Available commands:\n" +
        "/start - Register\n" +
        "/forget_me - Removes user\n" +
        "/chatid - Get your chat ID\n" +
        "/help - Show this help message\n" +
        "/add_device - Link a device to your account\n" + 
        "/remove_device - Link a device to your account\n" + 
        "/change_config - Link a device to your account"
    )
    bot.reply_to(message, help_message)

@bot.message_handler(commands=['add_device'])
def handle_add_device(message: telebot.types.Message):
    bot.reply_to(message, "Not implemented yet")

@bot.message_handler(commands=['remove_device'])
def handle_remove_device(message: telebot.types.Message):
    bot.reply_to(message, "Not implemented yet")

@bot.message_handler(commands=['change_config'])
def handle_change_config(message: telebot.types.Message):
    bot.reply_to(message, "Not implemented yet")

def send_telegram_notification(message: str):
    """Send a notification message to the configured Telegram chat."""
    for chat_id in chat_ids:
        try:
            bot.send_message(chat_id, message)
        except Exception as e:
            print(f"Error sending Telegram notification: {e}")

def start_bot():
    """Runs the Telegram bot polling"""
    bot.polling(none_stop=True)

if __name__ == "__main__":
    send_telegram_notification("Hello there?")
    bot.infinity_polling()


