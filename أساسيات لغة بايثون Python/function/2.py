def print_name(name):
    print('hello',name)
print_name(name='samm')
def show_info(name="Guest", age= 40, weight=0):
    print("Name:", name)
    print("Age:", age)
    print("Weight:", weight, "kg")

# استدعاءات مختلفة
show_info("Aya", 21, 55)
show_info("Ali", 25)
show_info(name="Sara", weight=48, age=26)
show_info()

def print_fruits(*fruits):
    for fruit in fruits:
        print(f'I like {fruit}')
print_fruits('apple','Orange')


def weather (**kwargs):
    print(kwargs)

weather(location= 'vimmerby',temperature=10 ,condtion='cloudy',wind_speed=19)


