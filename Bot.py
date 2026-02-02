import telebot
import google.generativeai as genai
import os

# یہ ٹوکنز ہم رینڈر کی سیٹنگز میں سیٹ کریں گے
GEMINI_API_KEY = os.getenv("GEMINI_KEY")
TELEGRAM_TOKEN = "8304198939:AAFcK1mUJjnjncu2GDztqk452gESfFjZsYo"

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        # Gemini سے اردو جواب لینا
        response = model.generate_content("صرف اردو میں جواب دیں: " + message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Error: {e}")

# بوٹ کو 24 گھنٹے آن رکھنے کے لیے
bot.infinity_polling()
