# Описание работы программы

Телеграм-бот calc_bot вычисляет введенные пользователями выражения. К вводу допускаются все рациональные числа, а также числа с мнимой единицей при необходимости комплексных вычислений.
Выражение для вычисления вводится строкой после команды /start. Вводить можно: 
* числа
* мнимую единицу i или j (для комплексных вычислений)
* операции +, -, *, /
* скобки для приоритезации операций

Действия с рациональными числами осуществляются с помощью самописаной библиотеки calc_lib, действия же с комплексными числами осуществляются с помощью встроенной библиотеки eval

Бот поддерживает команды:
/start - начало работы и приглашение ввести выражение для рассчета
/help - описание какие операции может осуществлять бот

![Image](calc_bot.png)
