import telebot
import os
import requests

# دریافت توکن از متغیر محیطی
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# آدرس سرور Selenium (این سرور باید `selenium_script.py` را اجرا کند)
SELENIUM_SERVER_URL = os.getenv("SELENIUM_SERVER_URL")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "✅ بات اجرا شد! مختصات GPS خود را ارسال کنید.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    gps_data = message.text
    bot.send_message(message.chat.id, f"📡 دریافت شد: {gps_data}\n⏳ در حال پردازش...")

    # ارسال داده به سرور Selenium
    response = requests.post(f"{SELENIUM_SERVER_URL}/process", json={"gps": gps_data})

    if response.status_code == 200:
        screenshot_url = response.json().get("screenshot_url")
        bot.send_photo(message.chat.id, screenshot_url, caption="📷 این هم تصویر نقشه!")
    else:
        bot.send_message(message.chat.id, "❌ خطا در پردازش داده!")

bot.polling()
