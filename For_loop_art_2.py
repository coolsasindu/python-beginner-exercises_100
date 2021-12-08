for x in range(6):
    out = ''
    for count in range(x):
        out += '*'

    print(out)
print("\n")

numbers = [1, 1, 1, 1, 5]  # print L Letter

for x in numbers:
    out = ''
    for count in range(x):
        out += '*'

    print(out)
print("\n")

numbers = [5, 1, 5, 1, 1]  # F print L Letter

for x in numbers:
    out = ''
    for count in range(x):
        out += '*'

    print(out)
print("\n")

numbers = [5, 1, 5, 1, 5]  # E print L Letter

for x in numbers:
    out = ''
    for count in range(x):
        out += '*'

    print(out)
print("\n")

numbers = [5, 1, 1, 1, 5]  # I print L Letter

for x in numbers:
    out = ''
    for count in range(x):
        if x == 1:
            out += '  *'
        else:
            out += '*'
    print(out)
