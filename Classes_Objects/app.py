from stubent import Student

student1 = Student("Tom Dj", "Business", 3.4, True)
print(student1.name)

student2 = Student("Will Klesy", "Physics", 3.8  , False)
print(student2.name)
print(student2.gpa)
print(student2.is_on_probation)

# object function
print('---on_honor_roll---')

# class function -|
print(student2.on_honor_roll())
print(student1.on_honor_roll())
