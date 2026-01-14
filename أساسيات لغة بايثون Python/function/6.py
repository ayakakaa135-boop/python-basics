def my_function(a):
    return a
add_two= lambda a ,b:a+b
print(add_two(5,2))

id=['id1' ,'id2' ,'id3' ,'id4']
id.sort(key= lambda  x :int(x[2:]))
print(id)

def sort_key(x):
    return int(x[2:])
id.sort(key=sort_key)
print( id)
