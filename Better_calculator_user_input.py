num1 = float(input("Enter first Number : "))
op = input("Enter operator : ")
num2 = float(input("Enter Second Number : "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1 + num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")