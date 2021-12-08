#  Don't repit code
class Animal:
    def walk(self):
        print("Walk..")


class Dog(Animal):  # inheritance to Animal class
    def bark(self):
        print("bark..UUu")


class Cat(Animal):
    def be_annoying(self):
        print("annoying..@@")


tomy = Dog()
tomy.walk()
tomy.bark()

caty = Cat()
caty.walk()
caty.be_annoying()
