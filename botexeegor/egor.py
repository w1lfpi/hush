from telebot import TeleBot
from PIL import Image
import os
import random

# Создаем экземпляр бота
TOKEN = 'your_token'
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я бот для отправки случайных егоров :3 используй команду /pic")

@bot.message_handler(commands=['pic'])
def send_random_image(message):
    # Получаем список изображений в директории
    images_dir = 'yor_way_to_the_photo'
    image_files = [f for f in os.listdir(images_dir) if f.lower().endswith('.jpg') or f.lower().endswith('.png')]
    
    if not image_files:
        bot.reply_to(message, "К сожалению, нет доступных егоров.")
        return
    
    # Выбираем случайное изображение
    random_image = random.choice(image_files)
    
    # Отправляем изображение
    with open(os.path.join(images_dir, random_image), 'rb') as image_file:
        bot.send_photo(message.chat.id, image_file, caption='сейчас вы такой Егор:      /pic')

if __name__ == '__main__':
    bot.polling()
