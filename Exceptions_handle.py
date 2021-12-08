try:
    number = int(input("Need number but Enter letters or 0 to error: "))
    income = 2500
    rick = income / number
    print(number)
except ZeroDivisionError as zr:
    print("Age can't be 0.")  # Custom Error msg
    print(zr)  # real Error msg

except ValueError as e:
    print("invalid input")  # Custom Error msg
    print(e)  # real Error msg

