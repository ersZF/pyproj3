import telebot
from telebot import types
import requests

bot = telebot.TeleBot('6828026739:AAHA9XZTL4PphrxbwCwxb-mFMNyUydFVY-g')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     '''Приветствую! Я бот, и я с радостью отвечу на любые вопросы о Subaru Impreza.

Чтобы получить информацию, просто введите соответствующую команду:

* **Поколения**: /generations
* **Двигатели**: /engines
* **Трансмиссии**: /transmissions
* **Электроника**: /electronics
* **Опции**: /options

Вы также можете найти запчасти для своего автомобиля по VIN-номеру, введя команду /parts.''')


@bot.message_handler(commands=['generations'])
def generations_info(message):
    bot.send_message(message.chat.id, '**Поколения Subaru Impreza по годам выпуска:**')
    generations = [
        {'year_range': '1992-2001', 'generation': '1'},
        {'year_range': '2001-2007', 'generation': '2'},
        {'year_range': '2007-2011', 'generation': '3'},
        {'year_range': '2011-2016', 'generation': '4'},
        {'year_range': '2016-2023', 'generation': '5'}
    ]
    for generation in generations:
        bot.send_message(message.chat.id, f'- Поколение {generation["generation"]}: {generation["year_range"]}')


@bot.message_handler(commands=['engines'])
def engines_info(message):
    bot.send_message(message.chat.id, '**Двигатели Subaru Impreza:**')
    engines = [
        {'generation': '1', 'engines': ['EJ16', 'EJ18', 'EJ20', 'EJ25']},
        {'generation': '2', 'engines': ['EJ16', 'EJ18', 'EJ20', 'EJ25', 'EZ30']},
        {'generation': '3', 'engines': ['FB16', 'FB20', 'FB25', 'FA20']},
        {'generation': '4', 'engines': ['FB16', 'FB20', 'FB25', 'FA20']},
        {'generation': '5', 'engines': ['FB16', 'FB20', 'FA24']}
    ]
    for engine in engines:
        bot.send_message(message.chat.id, f'- Поколение {engine["generation"]}: {", ".join(engine["engines"])}')


@bot.message_handler(commands=['transmissions'])
def transmissions_info(message):
    bot.send_message(message.chat.id, '**Коробки передач Subaru Impreza:**')
    transmissions = [
        {'generation': '1', 'transmissions': ['5-ступенчатая МКПП', '4-ступенчатая АКПП']},
        {'generation': '2', 'transmissions': ['5-ступенчатая МКПП', '4-ступенчатая АКПП', '5-ступенчатая АКПП']},
        {'generation': '3', 'transmissions': ['5-ступенчатая МКПП', '4-ступенчатая АКПП', 'CVT']},
        {'generation': '4', 'transmissions': ['5-ступенчатая МКПП', 'CVT', 'Lineartronic']},
        {'generation': '5', 'transmissions': ['6-ступенчатая МКПП', 'CVT', 'Lineartronic']}
    ]
    for transmission in transmissions:
        bot.send_message(message.chat.id,
                         f'- Поколение {transmission["generation"]}: {", ".join(transmission["transmissions"])}')


@bot.message_handler(commands=['electronics'])
def electronics_info(message):
    bot.send_message(message.chat.id, '**Оснащение электроникой Subaru Impreza:**')
    electronics = [
        {'generation': '1', 'electronics': ['ABS', 'EBD', 'BA']},
        {'generation': '2', 'electronics': ['ABS', 'EBD', 'BA', 'VDC']},
        {'generation': '3', 'electronics': ['ABS', 'EBD', 'BA', 'VDC', 'EyeSight']},
        {'generation': '4', 'electronics': ['ABS', 'EBD', 'BA', 'VDC', 'EyeSight', 'X-Mode']},
        {'generation': '5',
         'electronics': ['ABS', 'EBD', 'BA', 'VDC', 'EyeSight', 'X-Mode', 'Driver Monitoring System']}
    ]
    for electronic in electronics:
        bot.send_message(message.chat.id,
                         f'- Поколение {electronic["generation"]}: {", ".join(electronic["electronics"])}')


@bot.message_handler(commands=['options'])
def options_info(message):
    bot.send_message(message.chat.id, '**Опции Subaru Impreza:**')
    options = [
        {'generation': '1', 'options': ['Люк на крыше', 'Кожаный салон', 'Подогрев сидений']},
        {'generation': '2', 'options': ['Люк на крыше', 'Кожаный салон', 'Подогрев сидений', 'Навигационная система']},
        {'generation': '3', 'options': ['Люк на крыше', 'Кожаный салон', 'Подогрев сидений', 'Навигационная система',
                                        'Камера заднего вида']},
        {'generation': '4', 'options': ['Люк на крыше', 'Кожаный салон', 'Подогрев сидений', 'Навигационная система',
                                        'Камера заднего вида', 'Панорамная крыша']},
        {'generation': '5', 'options': ['Люк на крыше', 'Кожаный салон', 'Подогрев сидений', 'Навигационная система',
                                        'Камера заднего вида', 'Панорамная крыша', 'Система контроля слепых зон']}
    ]
    for option in options:
        bot.send_message(message.chat.id, f'- Поколение {option["generation"]}: {", ".join(option["options"])}')


@bot.message_handler(commands=['parts'])
def vin_search(message):
    bot.send_message(message.chat.id, 'Введите VIN-номер автомобиля (17 символов):')
    bot.register_next_step_handler(message, get_vin)


def get_vin(message):
    vin = message.text
    if len(vin) != 17:
        bot.send_message(message.chat.id, 'Неверный формат VIN-номера.')
    else:
        url = f'https://emex.ru/catalogs/original2/modifications?vin={vin}'
        bot.send_message(message.chat.id, f'Ссылка на поиск запчастей по VIN-номеру: {url}')


bot.polling()
