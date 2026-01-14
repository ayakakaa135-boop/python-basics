class UnderAgeError(Exception):
    def __init__(self, age):
        self.age = age
    def __str__(self):
        return f"Sorry, your age is {self.age} years old. You are too young to sign in."

class OverAgeError(Exception):
    def __init__(self, age):
        self.age = age
    def __str__(self):
        return f"Sorry, your age is {self.age} years old. You are too old to sign in."

try:
    age_input = input("Enter your age: ")

    if not age_input.isdigit():
        raise ValueError("Invalid input — please enter digits only.")

    age = int(age_input)

    if age < 15:
        raise UnderAgeError(age)
    elif age > 40:
        raise OverAgeError(age)
    else:
        print(f"Welcome! Your age ({age}) is acceptable to sign in.")

except ValueError as e:
    print(e)
except (UnderAgeError, OverAgeError) as e:
    print(e)
finally:
    print("Program execution finished.")
