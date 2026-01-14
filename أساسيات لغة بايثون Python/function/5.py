class MyType:
    def __len__(self):
        return 1000

my_type =MyType()
print(len(my_type))


def duplicate(value : float)->float:
    return value*2
print(duplicate(5))