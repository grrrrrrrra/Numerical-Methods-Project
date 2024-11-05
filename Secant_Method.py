from math import *
def f(x):
    """Ввод функции f(x)"""
    return (2*log(x) - x ** 2 + 5)

def num_diff(x, h = 0.0001):
    """Вычисляет численную производную функции f в точке x, используя небольшое приращение h.

    Args:
        x (float): Точка, в которой вычисляется производная
        h (float, optional): Небольшое приращение, используемое для приближенного вычисления конечной разности. Defaults to 0.0001.

    Returns:
        float: Приближенное значение производной функции f в точке x
    """
    return (f(x + h) - f(x)) / h

E = 0.000001
x_very_old, x_old = 2.5, 2.6

m = abs(min(num_diff(x_very_old), num_diff(x_old)))

def my_fun(x_very_old, x_old):
    delta = 1
    while delta > E:
        x = x_old - (f(x_old) * ((x_old - x_very_old)/(f(x_old) - f(x_very_old)))) 
        x_very_old = x_old
        x_old = x
        delta = abs(f(x_old)) / m
        print(x)
    return x

print(my_fun(x_very_old, x_old))