import telebot
import nolik_lib

API_TOKEN = "5641081713:AAGgQT2BgXL2zTfVTZuIjoNIL0_JwjvDhtc"
bot = telebot.TeleBot(API_TOKEN)
game_status = False
wait_row = False
wait_column = False
cur_row = 0
cur_column = 0
pleer = 0
sign = ['X', 'O']
n = 3

@bot.message_handler(commands=['start'])
def start_message(message):
    global game_status
    global wait_row
    global field

    # Начальное заполнение поля пустыми символами
    field = nolik_lib.field_init(n)
    # Приглашение к игре
    bot.send_message(message.chat.id, "Сыграем в крестики-нолики?\n")
    bot.send_message(message.chat.id, nolik_lib.field_string(field))
    bot.send_message(message.chat.id, f"\nХодит {pleer+1}-й игрок\nНапишите номер строчки, где поставить {sign[pleer]}?")
    game_status = True
    wait_row = True

@bot.message_handler(commands=['help'])
def help_message(message):
    message_text = "Для начала игры нажмите /start\n"
    message_text += "Для изменения размера квадратного поля напишите /change_size и через пробел укажите новый размер в поля (2, 3, 4 и т.д.)\n"
    message_text += "Для вызова справки по командам нажмите /help"
    bot.send_message(message.chat.id, message_text)

@bot.message_handler(commands=['change_size'])
def change_message(message):
    global n
    try:
        n = int(message.text.split(" ")[1])
        bot.send_message(message.chat.id, f"Размер поля изменен на {n}x{n}.")
    except:
        bot.send_message(message.chat.id, "Неверный формат размера поля!")

@bot.message_handler()
def game_message(message):
    global cur_row
    global cur_column
    global wait_row
    global wait_column
    global pleer
    global field
    global game_status

    # Если идет игра переходим к проверкам
    if game_status == True:
        # Если ожидалась на вход строка хода
        try:
            if wait_row == True:
                cur_row = int(message.text)
                bot.send_message(message.chat.id, "А в каком номере столбца?")
                wait_row = False
                wait_column = True
            # Если ожидался на вход столбец хода
            elif wait_column == True:
                cur_column = int(message.text)
                wait_row = True
                wait_column = False
                if field[cur_row - 1][cur_column - 1] == '--':
                    field[cur_row - 1][cur_column - 1] = sign[pleer]
                    bot.send_message(message.chat.id, nolik_lib.field_string(field))
                    # Проверка, вдруг кто-то уже виграл
                    if nolik_lib.check_win(field) != 0:
                        bot.send_message(message.chat.id, f"Игра окончена!\nВыиграл {pleer+1}-й игрок\nЧтобы сыграть еще раз, нажмите /start")
                        game_status = False

                    # Если игра продолжается, идет смена хода
                    if game_status == True:
                        # Переход хода и сброс координат хода
                        pleer = 1 - pleer
                        cur_row = 0
                        cur_column = 0
                        bot.send_message(message.chat.id, f"\nХодит {pleer+1}-й игрок\nНапишите номер строчки, где поставить {sign[pleer]}?")
                else:
                    bot.send_message(message.chat.id, nolik_lib.field_string(field))
                    bot.send_message(message.chat.id,
                                     f"В это поле уже походили ранее, попробуйте еще раз\nНапишите номер строчки, где поставить {sign[pleer]}?")
                    wait_row = True
                    wait_column = False
        except:
            bot.send_message(message.chat.id, nolik_lib.field_string(field))
            bot.send_message(message.chat.id, f"Неверные координаты, попробуйте еще раз\nНапишите номер строчки, где поставить {sign[pleer]}?")
            wait_row = True
            wait_column = False
    # Если игра не начиналась, подсказать команду начала
    else:
        # bot.send_message(message.chat.id, "Для начала игры нажмите /start")
        help_message(message)

print("Бот работает")
bot.polling()