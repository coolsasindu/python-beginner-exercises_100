phone = input("phone :")
digits = {
    "1": "one",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"
}
output = ''
for ch in phone:
    output += digits.get(ch, '!') + ' '
print(output)
