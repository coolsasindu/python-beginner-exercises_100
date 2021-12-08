numbers = [2,2,3,3,4,4,5,5,6,6,7,7,8,8]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
