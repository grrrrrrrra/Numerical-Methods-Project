from math import *

E, delta = 0.01, 1
x_0, x_1 = 2, 3 # отрезок изоляции

def function(x):
    """Ввод функции f(x)"""
    return log(x) + x ** 2 - 8
count_it = 0

while delta > 2 * E:
    x_2 = (x_0 + x_1) / 2
    if (function(x_0) + function(x_2)) ** 2 < function(x_0) ** 2 + function(x_2) ** 2:
        delta = x_2 - x_0
        x_1 = x_2
        count_it += 1
    elif (function(x_2) + function(x_1)) ** 2 < function(x_2) ** 2 + function(x_1) ** 2:
        delta = x_1 - x_2
        x_0 = x_2
        count_it += 1

    print(count_it, ' iteration')
    print(f'[{x_0}; {x_1}]')
    print()
    
print(f'корень уравнения — {(x_0 + x_1) / 2}')

    
    