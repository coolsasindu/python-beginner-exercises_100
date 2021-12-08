friends = ["Kevin", "Ann", "Tom", "Tom", "Jeny"]
print(friends)
print(friends[0])  # First Element
print(friends[1])  # 2 nd Element
print(friends[-1])  # First Element from back of the list
print(friends[1: 3])  # index 1 to 3 Element 3 is not included

# list modify
friends[1] = "mike"  # set new element
print(friends)
marks = ["45", "78", "89", "65"]

friends.extend(marks)
print(friends)

friends.append("USA")  # add item end of the list
print(friends)

friends.insert(1, "kaly")  # add item to index 1 position
print(friends)

friends.remove("kaly")  # remove kaly from list
print(friends)

friends.pop()  # remove last item from list
print(friends)

print(friends.index("mike"))  # get in mike index
print(friends.count("Tom"))  # get count word Tom

my_friends = ["Kevin", "Ann", "Tom", "Tom", "Jeny"]
my_friends.sort()  # A---Z Sort alphabetically 
marks.sort()  # 0 - 9

print(my_friends)
print(marks)

my_friends.reverse()  # reverse order
marks.reverse()  # reverse order 9 - 1

print(my_friends)
print(marks)

school_friends = friends.copy()   # copy to another list
print(school_friends)

friends.clear()   # remove all from list
print(friends)
