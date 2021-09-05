# проверям какой символ был введен

def check_input(s):
    allowed = 'xoXO'
    if s in allowed:
        s = s.upper()
        return(s)
    else:
        print('недопустимый символ ввода')
        return (False)

def play_field_draw():
    print('''так выглядит наше игровое поле
      0 1 2
    0 _ _ _
    1 _ _ _
    2 _ _ _
    ''')