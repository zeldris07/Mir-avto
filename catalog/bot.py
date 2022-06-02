import telebot
from django.core.management.base import BaseCommand

bot = telebot.TeleBot('5374226274:AAHUaEuBDvr3rHNHAuzPAlg7aKALh089uoY')

group = -795067208


def send_message(id, address, orient, number, name, text, price):
    bot.send_message(group,   f'💰Заказ Номер: {id}\n'
                              f'🏘Адресс {address}\n'
                              f'🌆Ориентир {orient}\n'
                              f'☎️Телефон: {number}\n'
                              f'💸К оплате {price}\n'
                              f'👱‍♂️Имя:{name}\n\n'
                              f'{text}')