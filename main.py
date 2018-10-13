from cal import sum_test
from square import square
from n_th_power import n_th_power

import sys
args = sys.argv

print('Can you expect the answer of this code?')
if len(args) < 3:
	print("input as [python main.py a b]")
	sys.exit()

_, a, b = args
a, b = list(map(int, [a, b]))

print("a, b = {}, {}".format(a, b))

"""
a, b = list(map(int, input().split()))

print('input = ', a, b)
"""

x = sum_test(a,b)

print('plus', x)
x = square(x)
print('square', x)
x = n_th_power(x, 3)
print('n th power', x)
