# проверям какой символ был введен

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