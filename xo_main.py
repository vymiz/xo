import func
import time
# приветствие и в двух словах ч0 делать будем
print(''''Играем в "Крестики-нолики"
Выбери символ, которым будешь играть, Х или О.
Вводить символ надо в английской раскладке клавиатуры.
Итак, каков твой выбор?''')

# ввод игорового символа и проверка его валидности
xo = False
while xo == False:
    xo = input('Введи символ: ')
    xo = func.check_input(xo)

xo_ = 'O' if xo == 'X' else 'X'
print(f'второй игрок будет играть симоволом {xo_}\n')

# создание пустого игрового поля и отрисовка его
f = [[' ',0,1,2],[0,'-','-','-'],[1,'-','-','-'],[2,'-','-','-']] # an empty game field
f_ctr = 9
print('так выглядит наше игровое поле\n')
func.play_field_draw(f)

# основно цикл игры: получаем значок, проверям доступность клетки, проверяем условия для продолжения игры
game = True
r,c, r_, c_ = False, False, None, None
xo_arr = []
xo_arr_ = []
win = [
    [0,1,2],
    [10,11,12],
    [20,21,22],
    [0,10,20],
    [1,11,21],
    [2,12,22],
    [0,11,22],
    [20,11,2]
    ]

while game:
    # получение символа от игрока, проверка поля, размещение символа
    r,c, f_ctr, xo_arr  = func.smb_input(f_ctr, xo_arr)

    if not r or not c:
        continue

    if f[r][c] != '-':
        print('Поле уже занято, попробуй еще раз...')
        continue
    else:
        f[r][c] = xo
    func.play_field_draw(f)
    game = func.win_check(f, win, xo_arr, xo, game, xo, xo_)
    if game == False:
        break

    # получение символа для компа (второго игрока), проверка, размещение
    print('ход второго игрока\n')
    time.sleep(1)
    f, r_, c_, f_ctr, xo_arr_ = func.rand_smb(f, xo_, f_ctr, xo_arr_)

    func.play_field_draw(f)
    game = func.win_check(f, win, xo_arr_, xo_, game, xo, xo_)

    if game == False:
        break

    if f_ctr ==0:
        print("Свободных полей на поле больше нет. Ничья")
        func.play_field_draw(f)
        game = False
        break






