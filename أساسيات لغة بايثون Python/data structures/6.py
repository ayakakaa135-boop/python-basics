# إنشاء قاموس أولي
student = {
    "name": "Aya",
    "age": 22,
    "course": "Python"
}

# 1️⃣ الوصول للقيم
print(student["name"])          # 'Aya'
print(student.get("course"))    # 'Python'
print(student.get("grade", "N/A"))  # 'N/A' (قيمة افتراضية لو المفتاح مو موجود)

# 2️⃣ إضافة أو تعديل قيم
student["grade"] = "A"
student["age"] = 23
print(student)
# {'name': 'Aya', 'age': 23, 'course': 'Python', 'grade': 'A'}

# 3️⃣ حذف عناصر
student.pop("course")   # يحذف العنصر ويرجع قيمته
print(student)

del student["grade"]    # يحذف العنصر بدون إرجاع
print(student)

# 4️⃣ نسخ القاموس
copy_student = student.copy()
print(copy_student)

# 5️⃣ دمج قاموسين
extra_info = {"country": "Sweden", "language": "English"}
student.update(extra_info)
print(student)
# {'name': 'Aya', 'age': 23, 'country': 'Sweden', 'language': 'English'}

# 6️⃣ التكرار على القاموس
for key, value in student.items():
    print(f"{key}: {value}")

# 7️⃣ مفاتيح وقيم
print(student.keys())    # dict_keys(['name', 'age', 'country', 'language'])
print(student.values())  # dict_values(['Aya', 23, 'Sweden', 'English'])
print(student.items())   # dict_items([...])

# 8️⃣ إنشاء قاموس من مفاتيح محددة
keys = ["x", "y", "z"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)          # {'x': 0, 'y': 0, 'z': 0}

# 9️⃣ مسح جميع العناصر
student.clear()
print(student)           # {}
