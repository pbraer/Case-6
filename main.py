# Case-study #6
# Developers:   Braer P. (%),
#               Kokorina D. (%),
#               Novoselov V. (%)

print("""Case-study Тесселяция
Разработчики:
Браер П.С., Кокорина Д.Е., Новоселов В.В.

""")
d_y = 1.5*side_len
d_x = d*0.5
n_y = round((500/(2*d + side_len))*2)
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