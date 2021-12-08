class Point:  # this is class

    def moves(self):  # this is method
        print("Iam Move")


    def draws(self):  # this is method
        print("Iam Draw")


point1 = Point()
point1.draw()

point1.x = 10  # x is  attribute
point1.y = 20
print(point1.x)
print(point1.y)


try:
    point2 = Point()
    point2.move()
# this is trow Attribute Error
# point2 don't x attribute
    print(point2.x)
except AttributeError:
    print('Have\'t x Attribute')
