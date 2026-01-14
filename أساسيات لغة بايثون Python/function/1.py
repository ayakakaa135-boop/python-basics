def my_function():
    print('hello world ')
my_function()
def sum():
     print(3)
     print(4)
     return
sum()

def get_age():
    age=int(input('Enter Your Age :'))
    if age <0 :
        return
    if age >120:
        return
    print(age)
get_age()


def degree():
    return 40
temperature = degree()
print(temperature)
degree()

def temp_scales():
    return ['a','x','d']
scale = temp_scales()[2]
print(scale)