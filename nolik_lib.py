# Задача 1. Создайте программу для игры в "Крестики-нолики".
def field_init(n):
    field = []
    for i in range(n):
        s = []
        for j in range(n):
            s.append('--')
        field.append(s)
        s = []
    return field

def field_string(field):
    field_string = ''
    for i in range(len(field)):
        if i != 0:
            field_string += '\n'
        for j in range(len(field)):
            field_string += field[i][j] + '  '
    return field_string


def check_win(field):
    combinations = []
    
    # Запись в массив всех имеющихся на поле комбинаций по строкам, столбцам
    n = len(field)
    for i in range(n):
        string_comb = []
        column_comb = []
        for j in range(n):
            string_comb.append(field[i][j])
            column_comb.append(field[j][i])
        combinations.append(string_comb)
        combinations.append(column_comb)
        
    # Запись в массив всех имеющихся на поле комбинаций по диагоналям, если применимо
    if n%2 == 1:
        diag1_comb = []
        diag2_comb = []
        for i in range(n):
            diag1_comb.append(field[i][i])
            diag2_comb.append(field[n-i-1][i])
        combinations.append(diag1_comb)
        combinations.append(diag2_comb)
    
    # Проверка выигрыша
    win_combination_1 = []
    win_combination_2 = []
    for i in range(n):
        win_combination_1.append('X')
        win_combination_2.append('O')
    if win_combination_1 in combinations:
        return 1
    elif win_combination_2 in combinations:
        return 2
    else:
        return 0
  
# try:
#     n=3
#     field = field_init()
#     pleer_flag = True
#     win_pleer = 0
#     while win_pleer == 0:
#         field_print()
#         if pleer_flag:
#             print("Ход 1-го игрока, укажите строку и столбец, где поставите Х")
#             x = int(input("Строка: "))
#             y = int(input("Столбец: "))
#             field[x-1][y-1] = 'X'
#         else:
#             print("Ход 2-го игрока, укажите строку и столбец, где поставите О")
#             x = int(input("Строка: "))
#             y = int(input("Столбец: "))
#             field[x-1][y-1] = 'O'
#         win_pleer = check_win()
#         pleer_flag = not pleer_flag
#
#     field_print()
#     print()
#     print(f"Выиграл {win_pleer}-й игрок! Поздравляем победителя!")
#
# except Exception as err:
#     print("Возникла ошибка: ", str(err.args))