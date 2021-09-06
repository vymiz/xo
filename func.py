import random

def check_input(s):
    allowed = 'xoXO'
    if s in allowed:
        s = s.upper()
        return(s)
    else:
        print('недопустимый символ ввода')
        return (False)

def play_field_draw(f):
    for i in range(4):
        print(end=' ')
        for j in range(4):
            print(f[i][j], end=' ')
        print('\n')

def smb_input(ctr, xo_arr):
    print('''
выбери клетку, куда хочешь поставить свой значок
сначала вводим номер строки, затем номер столбца''')
    r = input('Номер строки: ')
    c = input('Номер столбца: ')
    diapason = '012'
    if len(c) == 0 or len(r) == 0:
        print('неверное значение')
        return (False, False, ctr, xo_arr)
    elif (r in diapason) and (c in diapason):
        xo_arr.append(int(r+c))
        xo_arr.sort()
        r = int(r)
        c = int(c)
    else:
        print('неверное значение')
        return(False, False, ctr, xo_arr)

    return (r+1, c+1, ctr-1, xo_arr)

def rand_smb(f, xo_, ctr, xo_arr_):
    smb_gen = True
    while smb_gen == True:
        r_ = random.randint(1,3)
        c_ = random.randint(1,3)

        if f[r_][c_] != '-':
            continue
        else:
            f[r_][c_] = xo_
            xo_arr_.append(int(str(r_-1)+str(c_-1)))
            xo_arr_.sort()
            smb_gen = False

    return (f, r_, c_, ctr-1, xo_arr_)

def win_check(f, win, XO_arr, smb, game, xo, xo_):

    XO = set(XO_arr)

    for i in win:
        i = set(i)
        if XO.issuperset(i):
            game = False
            print('Игра оrончена!')
            if smb == xo:
                print('ты виграл! Поздравляю! Возьми с полки пирожок!')
                return(game)
            elif smb == xo_:
                print('Ты проиграл! Ничего, в следующий раз повезет!')
                return(game)
        else:
            game = True

    return(game)