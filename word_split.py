phone = input("type  '1 or 2 score' word :")
digits = {
    "1": "one",
    "2": "Two",

}
output = ''
for word in phone:
    output += digits.get(word,word)
print(output)
