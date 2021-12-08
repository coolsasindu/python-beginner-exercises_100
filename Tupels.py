coordinates = (4, 5, 6)  # Cannot change below in code
print(coordinates)
print(coordinates[0])
# coordinates [2] =5 can't modify

coordinates1 = [(4, 5), (44, 55), (11, 99)]
print(coordinates1)
print(coordinates1[2])


a = coordinates[0]
b = coordinates[1]
c = coordinates[2]
print(a)
print(c)
print(c)

# unpacking tuple
x, y, z = coordinates
print(x)
print(y)
print(z)
