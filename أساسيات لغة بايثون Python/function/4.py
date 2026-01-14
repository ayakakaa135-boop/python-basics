x = 100
def add(y):
    z= x + y
    return z
print(add(79))

xx=100
def print_number():
    global xx
    print(xx)

print_number()


def outer():
    x1=100
    def inner():
        nonlocal x1
        x1=300
    inner()

    print(x1)
outer()