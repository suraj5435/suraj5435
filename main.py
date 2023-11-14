import telebot
import requests
import json
import time

# Replace with your Telegram Bot Token
bot_token = '6650149619:AAERrE6RCI3nOHdIxzGep8BwcpfZv0uAkA4'

# Create a bot instance
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start(message):
    welcome_message = "Hello! I am your professional chatbot. Created by my owner @TryToLiveAlon .How can I assist you today?"
    bot.reply_to(message, welcome_message)

@bot.message_handler(commands=['ask'])
def ask(message):
    bot.reply_to(
        message,
        "Sure, please ask your question, and I'll do my best to answer!"
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_question = message.text
    if 'Ai' in user_question:
        api_url = f'https://chatgpt.apinepdev.workers.dev/?question={user_question}'
        response = requests.get(api_url)

        if response.status_code == 200:
            api_response = json.loads(response.text)
            answer = api_response.get(
                'answer',
                'I am sorry, I cannot answer your question at the moment. Please ask another question.'
            )

            response_with_emoji = "Ai " + answer
            bot.reply_to(message, response_with_emoji)
        else:
            bot.reply_to(
                message,
                "Sorry, I couldn't fetch a response at the moment. Please try again later."
            )

if name == "main":
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            print(f"Bot error: {e}")
            time.sleep(10)
