# Case-study #6
# Developers:   Braer P. (%),
#               Kokorina D. (%),
#               Novoselov V. (%)

print("""Case-study Тесселяция
Разработчики:
Браер П.С., Кокорина Д.Е., Новоселов В.В.

""")

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

def get_num_hexagons():
    n = 0
    print('Пожалуйста, введите количество шестиугольников, располагаемых в ряд: ',  sep='', end='')
    while n < 4:
        try:
            n = int(input())
            if n >= 4:
                return n
            else:
                print('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ', sep='', end ='')
                n = 0
        except ValueError:
            print('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ', sep='', end ='')
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
d = 500/(num+1.5)
side_len = (d*d/3)**(0.5)

d_y = 1.5*side_len
d_x = d*0.5
n_y = round((500/(2*d + side_len))*2)

import turtle as t
t.setup(500, 500)
t.speed(99999999)

color_n = 1
for f in range(1, num+1):
    if f % 2 == 1:
        indent = 2*d_x
    else:
        indent = d_x
    for s in range(1, num+1):
        if color_n % 2 == 1:
            color = '' + color_1 + ''
        else:
            color = '' + color_2 + ''
        draw_hexagon(-250+indent+d*(s-1), 250-d_y*0.5-d_y*f, side_len, color)
        color_n = color_n + 1
    if f % 2 == 0:
        color_n = color_n + 1

t.done()
