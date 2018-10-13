from add import add
from square import square
a,b = list(map(int, input().split()))
print('input', a, b)
x = add(a,b)
print('plus', x)
xx = square(x)
print('square', xx)
