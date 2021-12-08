number_grid = [
 #  0  1   2    3
    [1, 2, 3,    4],  # 0
    [5, 6, 7,    8],  # 1
    [9, 10, 11, 12],  # 2
    [0]               # 3
]
# how to print one element
print(number_grid[0])
print(number_grid[0][1])
print(number_grid[2][3])

number_grid[2][0] = 99  # value asigment
print("\n")


for row in number_grid:
    print(row)

print("\n")

for row in number_grid:
    for col in row:
        print(col)

