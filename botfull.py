import telebot
import random
import time
from datetime import datetime
from bot_oorr import chose
from bot_logic import gen_pass
from bot_smile import smile

# Замени 'YOUR_TOKEN_HERE' на токен
TOKEN = '8468601259:AAFuuZGdYosvMND6H-br3MJle5ztl7xepZw'
bot = telebot.TeleBot(TOKEN)

# 1. Хендлер для команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,"Привет! Я бот с 13 функциями. Напиши /help, чтобы узнать, что я умею.")

# 2. Хендлер для команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
    Я умею:
    /hello - Приветствие
    /fortune - Предсказание дня
    /date = Текущая дата
    /dice - Бросить игральный кубик
    /coin - Бросить монетку (орел/решка)
    /time - Текущее время
    /random - Случайное число от 1 до 100
    /photo - Случайное фото
    /echo - Повторю твое сообщение
    /info - Информация о тебе
    /reverse - Переворачивает текст
    /password (длина) - Генерирует пароль
    /smile - Рандомный смайлик
    """
    bot.send_message(message.chat.id, help_text)

# 3. Хендлер для команды /hello
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.send_message(message.chat.id, "Привет, как дела? 👋")

# 4. Хендлер для команды /fortune (Предсказание дня)
@bot.message_handler(commands=['fortune'])
def send_fortune(message):
    fortunes = [
        "Тебя ждет что-то невероятное!",
        "Сегодня — идеальный день, чтобы начать что-то новое.",
        "Ожидай приятный сюрприз!",
        "Будь внимателен к деталям, и успех не заставит себя ждать.",
        "Не бойся рисковать, тебе повезет!"
    ]
    random_fortune = random.choice(fortunes)
    bot.send_message(message.chat.id, f"Вот твое предсказание на сегодня: \n\n✨ {random_fortune} ✨")

# 5. Хендлер для команды /dice (Кубик)
@bot.message_handler(commands=['dice'])
def roll_dice(message):
    dice_message = bot.send_dice(message.chat.id)
    time.sleep(4)
    result = dice_message.dice.value
    bot.send_message(message.chat.id, f"Выпало число: **{result}**!")

# 6. Хендлер для команды /coin (Монетка)
@bot.message_handler(commands=['coin'])
def monetka(message):
    bot.send_message(message.chat.id,"Я подкинул монетку:\n"+chose())

# 7. Хендлер для команды /time
@bot.message_handler(commands=['time'])
def get_time(message):
    current_time = datetime.now().strftime("%H:%M:%S")
    bot.send_message(message.chat.id, f"Текущее время: **{current_time}**")


# 8. Хендлер для /date
@bot.message_handler(commands=['date'])
def get_date(message):
    today = datetime.now().strftime("%d.%m.%Y")
    bot.send_message(message.chat.id, f"Сегодняшняя дата: **{today}**")

# 9. Хендлер для /fact
@bot.message_handler(commands=['fact'])
def get_fact(message):
    facts = [
        "Пчелы могут летать быстрее, чем человек бегает.",
        "Крокодилы не могут высунуть язык.",
        "Клетки человеческого тела полностью обновляются каждые 7-10 лет.",
        "У кошек 32 мышцы в каждом ухе.",
        "Единственный континент, на котором нет действующих вулканов, это Антарктида."
    ]
    bot.send_message(message.chat.id, random.choice(facts))


# 10. Хендлер для команды /random
@bot.message_handler(commands=['random'])
def get_random_number(message):
    random_num = random.randint(1, 100)
    bot.send_message(message.chat.id, f"Случайное число от 1 до 100: **{random_num}**")

# 11. Хендлер для команды /photo (Отправка фото по URL)
@bot.message_handler(commands=['photo'])
def send_photo(message):
    photo_url = "https://picsum.photos/200/300" # Случайная картинка с сервиса picsum.photos
    bot.send_photo(message.chat.id, photo_url)


 # 12 Хендлер для команды /info
@bot.message_handler(commands=['info'])
def get_user_info(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    bot.send_message(message.chat.id, f"Ваш ID: `{user_id}`\nВаше имя: **{first_name}**", parse_mode='Markdown')


# 13. Хендлер для /reverse
@bot.message_handler(commands=['reverse'])
def reverse_text(message):
    text = message.text.replace('/reverse ', '', 1)
    reversed_text = text[::-1]
    bot.send_message(message.chat.id, reversed_text)

@bot.message_handler(commands=['password'])
def genpass(message):
    simvols = int(message.text.split()[1]) if len(message.text.split()) > 1 else 12
    bot.send_message(message.chat.id,"Я сгенерировал тебе пароль длиной "+str(simvols)+" символов:\n"+gen_pass(simvols))

@bot.message_handler(commands=['smile'])
def sm(message):
    bot.send_message(message.chat.id,"Моё настроение сегодня:")
    bot.send_message(message.chat.id,smile())


# 14 Хендлер, который отвечает на любое текстовое сообщение (Эхо)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("Бот запущен. Напиши /help, чтобы начать.")
bot.polling(none_stop=True)