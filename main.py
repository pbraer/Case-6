# Case-study #6
# Developers:   Braer P. (%),
#               Kokorina D. (%),
#               Novoselov V. (%)

print("""Case-study Тесселяция
Разработчики:
Браер П.С., Кокорина Д.Е., Новоселов В.В.

""")

def get_num_hexagons():
    n = 0
    print('Пожалуйста, введите количество шестиугольников, располагаемых в ряд: ',  sep='', end='')
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



