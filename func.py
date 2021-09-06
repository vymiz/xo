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

def smb_input():
    print('''
выбери клетку, куда хочешь поставить свой значок
сначала вводим номер строки, затем номер столбца''')
    r = input('Номер строки: ')
    c = input('Номер столбца: ')
    diapason = '012'
    if (r in diapason) and (c in diapason):
        r = int(r)
        c = int(c)
    else:
        print('неверное значение')
        return(False, False)

    return (r+1, c+1)

def rand_smb(f, xo_):
    smb_gen = True
    while smb_gen == True:
        r = random.randint(1,3)
        c = random.randint(1,3)

        if f[r][c] != '-':
            continue
        else:
            f[r][c] = xo_
            smb_gen = False

    return (f)