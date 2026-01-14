from functools import reduce




numbers=[1,2,3,4,5]
def get_squares(x):
    return x**2
squares = map(get_squares,numbers)
print(list(squares))
#مكررًا يطبق الدالة المعطاة على كل عنصر من عناصر الكائن الممرر.
squares=map(lambda x:x**2,numbers)
print(list(squares))


temps = [
    ("London", 18),
    ("Paris", 22),
    ("Cairo", 30),
    ("Tokyo", 27)
]
f_temps=list(map(lambda item: (item[0],(1.8)*item[1]+32),temps))
print(f_temps)
def c_to_f(item):
    return item[0],(1.8)*item[1]+32




f_temp = list(map(c_to_f, temps))

print(f_temp)
#عناصر كائن قابل للتكرار.




languages = [
    ("Python", 1991),
    ("C", 1972),
    ("Java", 1995),
    ("Fortran", 1957),
    ("JavaScript", 1995)
]
def old(item):
    return item[1] < 1990

old_languages= filter(old,languages)
print(list(old_languages
           ))


def find(iterable ,text):
    def finder(lang):
        for i in lang:
            if str(i).startswith(text):
                return True
            return False


    return list(filter(finder,iterable))

results = find(languages,'Java')
print(results)
# البحث عن سلسلة نصية واعاداتها


def add (x,y):
    return x+y


print(reduce(add,numbers))
print(sum(numbers))



numberss =[33,55,66,77,88,99]
max_number = reduce(lambda x,y : x if x>y else y , numberss)
print(max_number)
print(max(numberss))