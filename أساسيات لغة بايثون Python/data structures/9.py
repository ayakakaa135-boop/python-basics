numbers = [1,33,3,4,6,7,8,8,9]
my_number =[ number for number in numbers if number > 4 ]
print(my_number)
squars = [i**2 for i in range (10)]
print(squars)
percentages =[22,44,44,55,100,200,456]
new_percentages =[i if i<=100 else 100 for i in percentages]
print(new_percentages)


squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
