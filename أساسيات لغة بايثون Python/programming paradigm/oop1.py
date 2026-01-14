class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def show_info(self):
        print(f" School: {self.name}")
        print(" Teachers:")
        for t in self.teachers:
            print(f"- {t.name} teaches {t.subject}")
        print(" Students:")
        for s in self.students:
            print(f"- {s.name}, Age: {s.age}")




school = School("Vimmerby School")


t1 = Teacher("Mr. Ali", "Math")
t2 = Teacher("Ms. Sara", "English")

s1 = Student("Aya", 16)
s2 = Student("ٍSam", 20)


school.add_teacher(t1)
school.add_teacher(t2)
school.add_student(s1)
school.add_student(s2)


school.show_info()

