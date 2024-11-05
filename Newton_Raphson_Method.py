from math import *
def f(x):
    """Ввод функции f(x)"""
    return (2 * log(x) + 2 * x - 3)

def num_diff(x: float, h: float = 0.0001) -> float:
    """Вычисляет численную производную функции f в точке x, используя небольшое приращение h.

    Args:
        x (float): Точка, в которой вычисляется производная
        h (float, optional): Небольшое приращение, используемое для приближенного вычисления конечной разности. Defaults to 0.0001.

    Returns:
        float: Приближенное значение производной функции f в точке x
    """
    return (f(x + h) - f(x)) / h

def second_num_diff(x, h = 0.0001):
    """Вычисляет вторую численную производную функции f в точке x, используя небольшое приращение h.

    Args:
        x (float): Точка, в которой вычисляется производная
        h (float, optional): Небольшое приращение, используемое для приближенного вычисления конечной разности. Defaults to 0.0001.

    Returns:
        float: Приближенное значение второй производной функции f в точке x
    """
    return (num_diff(x + h) - num_diff(x)) / h

E, delta = 0.001, 1
x_0, x_1 = 1, 1.5 # отрезок изоляции
x = (x_0 + x_1) / 2

f1_diff_0 = num_diff(x_0)
f1_diff_1 = num_diff(x_1)
f2_diff_0 = second_num_diff(x_0)
f2_diff_1 = second_num_diff(x_1)

first_condition = (f1_diff_0 + f1_diff_1) ** 2 > f1_diff_0 ** 2 + f1_diff_1 ** 2
second_condition = (f2_diff_0 + f2_diff_1) ** 2 > f2_diff_0 ** 2 + f2_diff_1 ** 2

if first_condition and second_condition:
    print('итерационный процесс сходится :)')
else:
    print('итерационный процесс не сходится :(')
    
m = min(abs(num_diff(x_0)), abs(num_diff(x_1)))

count_it = 0
while delta > E:
    x_old = x
    x = x_old - (f(x_old) / num_diff(x_old))
    count_it += 1
    print(f'x{count_it} = {x}')
    delta = f(x) / m
    

