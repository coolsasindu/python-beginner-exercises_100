
class Point:  # this is class

    def __init__(self, x, y):  #this is constructors
        self.x = x
        self.y = y

    def moves(self):  # this is method
        print("Iam Move")


    def draws(self):  # this is method
        print("Iam Draw")


point = Point(10, 20)
point.x =11
print(point.x)
