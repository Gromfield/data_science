# функция вывода поля, элементы строк-списков разделяем пробелами, убираем скобки
def vyvod_polya():
    for i in range(4):
        print(' '.join(pole[i]))


# создаем функцию ввода координат
def vvod_koordinat():
    print('Введите координаты')
    input_x, input_y = int(input('Столбец: ')), int(input('Строка: '))
    return input_x, input_y


# функция проверки координат и их повторного ввода в случае ошибки
def coord_check(check_x, check_y):
    while not (0 <= check_x <= 2) or not (0 <= check_y <= 2):
        print('Неверные координаты')
        check_x, check_y = vvod_koordinat()
    return check_x, check_y


# создаем функцию проверки заполнения ячейки
def field_empty(fne_pole, fne_x, fne_y): # объявляем переменные, в которые будут сохраняться входные данные, и которые будут использоваться внутри функции
    # объявляем локальную переменную, в которую будем записывать проверяемую строку целиком
    str_proverki = fne_pole[fne_x + 1]
    # проверяем элемент строки, который находится на позиции [fne_y + 1]
    # возвращяем результаты проверки
    return str_proverki[fne_y + 1] == '-'


# создаем поле в виде списка строк-списков
pole = [
    [' ', '0', '1', '2'],
    ['0', '-', '-', '-'],
    ['1', '-', '-', '-'],
    ['2', '-', '-', '-']
]
# печатаем пустое поле
vyvod_polya()
# объявляем переменную счетчика ходов
turn = 1
# начинаем цикл хода
while turn <= 9:
    # объявляем ход крестиков или ноликов в зависимости от значения счетчика ходов
    if turn % 2 == 0:
        print('Ход ноликов')
    else:
        print('Ход крестиков')
    # присваиваем переменным значения координат размещения крестика/нолика, введенным с клавиатуры
    hod_x, hod_y = vvod_koordinat()
    # проверяем правильность указания координат
    hod_x, hod_y = coord_check(hod_x, hod_y)
    str_zapolnenia = pole[hod_y + 1]
    ostanov = True
    # запускаем цикл: пока остановка не False
    while ostanov:
        # сравниваем результат работы функции проверки заполнения ячейки, передаем на вход переменные pole, hod_x, hod_y
        if field_empty(pole, hod_x, hod_y):
            # если ячейка пустая, заполняем ячейку крестиком/ноликом
            # str_zapolnenia = pole[hod_y + 1]
            if turn % 2 == 0:
                str_zapolnenia[hod_x + 1] = 'O'
            else:
                str_zapolnenia[hod_x + 1] = 'X'
            break
        else:
            # если занята, просим ввести новые координаты
            print('Ячейка занята')
            # для проверки вывод ячейки, которая оказалась занятой
            print(str_zapolnenia[hod_x + 1])
            hod_x, hod_y = vvod_koordinat()
            # проверяем правильность ввода координат
            hod_x, hod_y = coord_check(hod_x, hod_y)
    # записываем крестик/нолик в ячейку
    if turn % 2 == 0:
        # меняем значение строки на значение с результатом хода
        pole[hod_y + 1] = str_zapolnenia
        str_0 = pole[1]
        str_1 = pole[2]
        str_2 = pole[3]
        # проверяем условия победы, если да, звершаем игру
        if any([
            pole[1] == ['0', 'O', 'O', 'O'],
            pole[2] == ['1', 'O', 'O', 'O'],
            pole[3] == ['2', 'O', 'O', 'O'],
            (str_0[1] == 'O' and str_1[1] == 'O' and str_2[1] == 'O'),
            (str_0[2] == 'O' and str_1[2] == 'O' and str_2[2] == 'O'),
            (str_0[3] == 'O' and str_1[3] == 'O' and str_2[3] == 'O'),
            (str_0[1] == 'O' and str_1[2] == 'O' and str_2[3] == 'O'),
            (str_0[3] == 'O' and str_1[2] == 'O' and str_2[1] == 'O')
        ]):
            break
    else:
        # меняем значение строки на значение с результатом хода
        pole[hod_y + 1] = str_zapolnenia
        str_0 = pole[1]
        str_1 = pole[2]
        str_2 = pole[3]
        if any([
            pole[1] == ['0', 'X', 'X', 'X'],
            pole[2] == ['1', 'X', 'X', 'X'],
            pole[3] == ['2', 'X', 'X', 'X'],
            (str_0[1] == 'X' and str_1[1] == 'X' and str_2[1] == 'X'),
            (str_0[2] == 'X' and str_1[2] == 'X' and str_2[2] == 'X'),
            (str_0[3] == 'X' and str_1[3] == 'X' and str_2[3] == 'X'),
            (str_0[1] == 'X' and str_1[2] == 'X' and str_2[3] == 'X'),
            (str_0[3] == 'X' and str_1[2] == 'X' and str_2[1] == 'X')
        ]):
            break
    # увеличиваем счетчик ходов на 1
    turn += 1
    # выводим обновленное поле
    vyvod_polya()
    print('---------------------------------')
print('---------------------------------')
# выводим итоговое поле
vyvod_polya()
print('Игра окончена')
# объявляем победителя
if turn % 2 == 0:
    print('Победили нолики')
else:
    print('Победили крестики')
