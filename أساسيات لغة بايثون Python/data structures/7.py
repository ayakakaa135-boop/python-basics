fruits_list =['apple' ,'banana' , 'lemon','orange' ,'apple']
fruits_set =set(fruits_list)
print(fruits_set)
empty_set =set()
print(empty_set)
print(type(empty_set))
print(bool(empty_set))
print('apple' in fruits_set)
a = {1, 2, 3}
b = {3, 4, 5}
c= {2,3,4}

print(a | b | c)        # {1, 2, 3, 4, 5}
print(a.union(b))   # نفس النتيجة
print(a & b)              # {3}
print(a.intersection(b))  # {3}
print(a - b)           # {1, 2}
print(a.difference(b)) # {1, 2}
print(a ^ b)                   # {1, 2, 4, 5}
print(a.symmetric_difference(b))  # نفس الشي

s = {1, 2, 3}
s.add(4)          # إضافة عنصر
s.remove(2)       # حذف عنصر (بيعطي خطأ لو مش موجود)
s.discard(5)      # حذف بدون خطأ لو مش موجود
s.clear()         # تفريغ المجموعة
