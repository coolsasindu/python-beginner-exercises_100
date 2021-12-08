# if else used make logic

is_male = True  # True or False
is_tall = False  # True or False


if is_male and is_tall:
    print("you are a tall male")

elif is_male and not is_tall:
    print("you are a short male")

elif not is_male and is_tall:
    print("you are not a male but are tall")

else:
    print("you are ether not male not tall or both")

