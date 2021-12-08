
data = open("data.txt", "r")  # open data.txt file
# r is read | w is writing | a is append file

# remove # mark and run line by line

#print(data.readable())  # if w > False
#print(data.read())  # read all

#print(data.readline())  # read line by line
#print(data.readline())  # read line by line

#print(data.readlines())
#print(data.readlines()[1])

for dt in data.readlines():  # print all lines
    print(dt)



data.close()  # close file

