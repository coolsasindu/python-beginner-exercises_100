"""
(x, y)
(0, 0)
(0, 1)
(1, 0)
(1, 0)
"""
from builtins import range

for x in range(4):
    for y in range(3):
        print(f'({x} ,{y})')
    print('..........')


numbers = [1, 1, 1, 1, 5]  # print L Letter

for x in numbers:
    out = ''
    for count in range(x):
        out += '*'
print(out)

for x in numbers:
    print('*' * x)
