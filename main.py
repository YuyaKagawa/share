from cal import sum_test
from square import square
import sys

args = sys.argv

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

xx = square(x)

print('square', xx)
