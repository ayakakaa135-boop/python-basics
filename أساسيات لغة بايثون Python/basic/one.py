"""while True:
    name = input("enter your name :")
    if name == 'stop':
        break
    age = input('Enter your birth')
    print("hello", name)

    print('Your age ', 2021 - int(age), 'years old ')
"""
"""for i in range(0,5):
    if i==2:
        print("* python3 *")
        continue
    else:
        print("*" * 6)"""
num= 1
for i in range (0,7):
    for j in range (0,i+1):
        print(num ,end = " ")
        num+=1
    print()
