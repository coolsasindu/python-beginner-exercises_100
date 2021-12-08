def maxnum(num1, num2, num3):
    if num1 >= num2 >= num3:
        return num1
    elif num2 >= num1 >= num3:
        return num2
    else:
        return num3


print(maxnum(12, 45, 8))
print(maxnum(330, 405, 128))


def chkceq(num1, num2):
    if num1 == num2:
        return "Yes"
    elif num2 != num1:
        return "No"
    else:
        return "Opss"


print(chkceq(12,12))