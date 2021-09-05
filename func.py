# проверям какой символ был введен

def test():
    print('test import')

def check_input(s):
    allowed = 'xoXO'
    if s in allowed:
        return(s.upper())
    else:
        print('недопустимый символ ввода')
        return (None)