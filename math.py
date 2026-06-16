import random

def common_level(term = 0):
    a = random.random() * 10 + term
    b = random.random() * 10
    a = int(a)
    b = int(b)
    r = input(f'{a} * {b} = ')
    r = int(r)
    if r == a * b:
        print('Верно!')
    else:
        print('Неверно!', a * b)

def level1():
    common_level()

def level2():
    common_level(10)

level2()
