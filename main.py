# Case-study #6
# Developers:   Braer P. (%),
#               Kokorina D. (%),
#               Novoselov V. (%)

print("""Case-study Тесселяция
Разработчики:
Браер П.С., Кокорина Д.Е., Новоселов В.В.

""")

import turtle as t
t.setup(500, 500)
t.speed(99999999)

def draw_hexagon(x, y, side_len, color):
    t.up()
    t.fillcolor(color)
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.left(90)
    for i in range(1, 7):
        t.forward(side_len)
        t.right(60)
    for j in range(7, 11):
        t.up()
        t.forward(side_len)
        t.right(60)
        t.down()
    t.right(210)
    t.end_fill()
    t.up()
    t.home()

def get_color_choice():

    print('Пожалуйста, введите цвет: ', sep='', end='')
    color = ''
    while color == '':
        color = input()
        color = color.lower()
        if color == 'красный':
            color = '#A60400'
            return color
        elif color == 'синий':
            color = '#1D0772'
            return color
        elif color == 'зеленый' or color == 'зелёный':
            color = '#369100'
            return color
        elif color == 'желтый' or color == 'жёлтый':
            color = '#FFF700'
            return color
        elif color == 'оранжевый':
            color = '#FF8100'
            return color
        elif color == 'пурпурный':
            color = '#BC38D3'
            return color
        elif color == 'розовый':
            color = '#E667AF'
            return color
        else:
            print("'", color, "' не является верным значением. Пожалуйста, повторите попытку: ", sep='', end='')
            color = ''
