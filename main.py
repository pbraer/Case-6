# Case-study #6
# Developers:   Braer P. (70%),
#               Kokorina D. (35%),
#               Novoselov V. (25%)

print("""Case-study Тесселяция
Разработчики:
Браер П.С., Кокорина Д.Е., Новоселов В.В.

""")


def draw_hexagon(x, y, side_length, color):
    t.up()
    t.fillcolor(color)
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.left(90)
    for i in range(1, 7):
        t.forward(side_length)
        t.right(60)
    for j in range(7, 11):
        t.up()
        t.forward(side_length)
        t.right(60)
        t.down()
    t.right(210)
    t.end_fill()
    t.up()
    t.home()


def get_color_choice():
    print('Пожалуйста, введите цвет: ', sep='', end='')
    col = ''
    while col == '':
        col = input()
        col = col.lower()
        if col == 'красный':
            col = '#A60400'
            return col
        elif col == 'синий':
            col = '#1D0772'
            return col
        elif col == 'зеленый' or col == 'зелёный':
            col = '#369100'
            return col
        elif col == 'желтый' or col == 'жёлтый':
            col = '#FFF700'
            return col
        elif col == 'оранжевый':
            col = '#FF8100'
            return col
        elif col == 'пурпурный':
            col = '#BC38D3'
            return col
        elif col == 'розовый':
            col = '#E667AF'
            return col
        else:
            print("'", col, "' не является верным значением. Пожалуйста, повторите попытку: ", sep='', end='')
            col = ''


def get_num_hexagons():
    n = 0
    print('Пожалуйста, введите количество шестиугольников, располагаемых в ряд: ', sep='', end='')
    while n < 4:
        try:
            n = int(input())
            if n >= 4:
                return n
            else:
                print('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ', sep='', end='')
                n = 0
        except ValueError:
            print('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ', sep='', end='')
            n = 0


print('''Допустимые цвета заливки:
    красный
    синий
    зеленый
    желтый
    оранжевый
    пурпурный
    розовый''')

color_1 = get_color_choice()
color_2 = get_color_choice()

num = get_num_hexagons()
d = 500 / (num + 1.5)
side_len = (d * d / 3) ** 0.5

d_y = 1.5 * side_len
d_x = d * 0.5
n_y = round((500 / (2 * d + side_len)) * 2)

import turtle as t

t.setup(500, 500)
t.speed(99999999)

color_n = 1

for f in range(1, num + 1):
    if f % 2 == 1:
        indent = 2 * d_x
    else:
        indent = d_x
    for s in range(1, num + 1):
        if color_n % 2 == 1:
            clr = '' + color_1 + ''
        else:
            clr = '' + color_2 + ''
        draw_hexagon(-250 + indent + d * (s - 1), 250 - d_y * 0.5 - d_y * f, side_len, clr)
        color_n = color_n + 1
    if f % 2 == 0:
        color_n = color_n + 1

t.done()
