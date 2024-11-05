from math import *
def f(x):
    "Ввод фи(х) (!), посчитанного предварительно в ручную "
    return ((3 / 2) -  log(x))

def num_diff(x, h = 0.0001):
    """Вычисляет численную производную функции f в точке x, используя небольшое приращение h.

    Args:
        x (float): Точка, в которой вычисляется производная
        h (float, optional): Небольшое приращение, используемое для приближенного вычисления конечной разности. Defaults to 0.0001.

    Returns:
        float: Приближенное значение производной функции f в точке x
    """
    return (f(x + h) - f(x)) / h

E, delta = 0.001, 1
x_0, x_1 = 1.2, 1.3 # отрезок изоляции
x = (x_0 + x_1) / 2

diff_x_0 = num_diff(x_0)
diff_x_1 = num_diff(x_1)

q = max(abs(diff_x_0), abs(diff_x_0)) # коэффициент сжатия

if q < 1:
    print(f'q = {round(q, 3)} \nитерационный процесс сходится :)')
    print()
else:
    print(f'q > 1, итерационный процесс не сходится :(')

count_it = 0
while delta > E:
    x_old = x
    x = f(x)
    count_it += 1
    print(f'x{count_it} = {f(x)}')
    delta = q / (1 - q) * abs(x - x_old)
    