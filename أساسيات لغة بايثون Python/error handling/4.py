class UnderAgeError(Exception):
    def __init__(self, message):
        self.message= message

    def __str__(self):
        return self.message



class OverAgeError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

age = int (input('Enter your age : '))
if age < 15 : raise UnderAgeError(f'Sorry , but your age {age}years old .you are too young to sign in')
if age > 40 : raise OverAgeError(f'Sorry , but your age {age}years old .you are too old to sign in')

