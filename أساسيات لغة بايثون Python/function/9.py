x = iter(['a','b','c'])
print(x)
print(next(x))


def my_generator():
    i=0
    print('First value')
    yield i
    i+=1
    print('Second value')
    yield i
    i += 1
    print('Last value')
    yield i

my_gen = my_generator()
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

def odd_number(numbers):
    for num in range(1,numbers,2):
        yield num

def square(nums):
    for num in nums:
        yield num **2

print(sum(square(odd_number(10))))

odd_numbers=(num for num in range(1,10,2))
squares =(num**2 for num in odd_numbers)
print(sum(squares))