import telebot
import openai

# Установите свой токен Telegram и ключ API от OpenAI
TELEGRAM_TOKEN = '6120427647:AAGO4UJlUOpTx2FM5tNmK7TaIW4kSuDM4QQ'
OPENAI_API_KEY = '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'

# Создайте экземпляр бота
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Подключение к API OpenAI
openai.api_key = OPENAI_API_KEY

# Функция для отправки запроса к ChatGPT
def send_to_chatgpt(message):
    response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt=message,
        max_tokens=900,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, 'Привет! Я бот, готовый отвечать на твои вопросы.')

# Обработчик всех остальных сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    bot_response = send_to_chatgpt(user_input)
    bot.reply_to(message, bot_response)

# Запуск бота
bot.polling()
