for i in range(5):
    print(i , end= ' ,')

numbers = [10, 20, 30]
for n in numbers:
    print(n , end=' ')
for char in "Python":
    print(char)
colors = {"red", "green", "blue"}

for color in colors:
    print(color)
person = {"name": "Aya", "age": 21}

for key in person.items():
    print(key)  # بيطبع المفاتيح بس
for key, value in person.items():
    print(key, "=>", value)
employees = ['maya' ,'ss' , 'mo' ,'ay']

for index in range (len(employees)):
    print(index,employees[index])
names = ["Aya", "Ali", "Sara"]

for index, name in enumerate(names , start=1):
    print(index, name)
