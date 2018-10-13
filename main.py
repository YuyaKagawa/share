from cal import sum_test
from square import square
from n_th_power import n_th_power
a,b = list(map(int, input().split()))
print('input', a, b)
x = sum_test(a,b)
print('plus', x)
x = square(x)
print('square', x)
x = n_th_power(x, 3)
print('n th power', x)
