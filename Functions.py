def sayhi():
    print("Hi sayhi Funtion..")


print("Top")
sayhi()  # call sayhi() funtion
print("Bottom")


def say_hi(name):  # name is parameter
    print("Hello " + name)


say_hi("Steve")  # set name argument to name value
say_hi("Tom")


def sayhello(name, age):  # name ,age is parameter
    print("Hello " + name + " you are " + age)


sayhello("Toby", "25")  # set name, age argument to values
sayhello("any", "22")

sayhello(name="Mary", age="22")  # keyword argument




