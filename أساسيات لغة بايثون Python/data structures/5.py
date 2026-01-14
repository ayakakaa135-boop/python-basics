
d = {'one': 1,
     'two': 2,
     'three': 3}
d['one']='zero'
d['four']= 'v'
dr=d['one'][2]
print( f'dr:{dr}')
print(d)

print(type(d))
d = dict([('one', 1), ('two', 2), ('three', 3)])

print(d)
print('one' in d)
print(len(d))
de=d.values()

print(de)

employess={1:'aya' ,2:'rasha',3:'sam'}
print(employess[1])