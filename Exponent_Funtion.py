print(2**3)
print(3**3)
print(5**5)

def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result


new_result = raise_to_power(5, 3)
print(new_result)

