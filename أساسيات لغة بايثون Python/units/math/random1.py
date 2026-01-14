import random
print(random.random())
print(random.random())
print(random.randint(1,22))
print(random.randint(1,52))
print(random.randrange(12))
name = ['aya' ,' sam ' ,'maya']
print(random.choice(name))
print(random.choice(name))
print(random.choices(name,k = 2))
print(name)
random.shuffle(name)
print(name)