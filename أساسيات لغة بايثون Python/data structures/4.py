word = 'Python'
print(word[0])   # 'P'
print(word[5])   # 'n'
print(word[-1])  # 'n' → آخر حرف
print(word[-2])  # 'o' → قبل الأخير
# print(word[10])  # ❌ IndexError: string index out of range

word = 'Python'
print(word[0:2])   # 'Py' → من الفهرس 0 لقبل 2
print(word[2:5])   # 'tho'
numbers = [1 ,2 ,3 ,4 , 5, 6,7,8]
numbers[ : ] =[]
print(numbers)
print(numbers[0:7:2])
print(numbers[7:0:-2])
print(numbers[:])

