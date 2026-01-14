class Vimmerby_school:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
        self.school = "vimmerby School"

    def show_info(self):
        return f"Name: {self.name}, Age: {self.age}, Department: {self.department}, School: {self.school}"



class Principal(Vimmerby_school):
    def __init__(self, name, age, department, experience_years):
        super().__init__(name, age, department)
        self.experience_years = experience_years

    def manage_school(self):
        return f"{self.name} manages the school with {self.experience_years} years of experience."


    def hold_meeting(self):
        return f"{self.name} is holding a staff meeting at {self.school}."


class VicePrincipal(Vimmerby_school):
    def __init__(self, name, age, department, assigned_area):
        super().__init__(name, age, department)
        self.assigned_area = assigned_area

    def assist_principal(self):
        return f"{self.name} assists in managing the {self.assigned_area} section."


    def supervise_teachers(self):
        return f"{self.name} is supervising teachers in the {self.assigned_area} section."


class Teacher(Vimmerby_school):
    def __init__(self, name, age, department, subject):
        super().__init__(name, age, department)
        self.subject = subject

    def teach(self):
        return f"{self.name} teaches {self.subject}."


    def prepare_lessons(self):
        return f"{self.name} is preparing lessons for {self.subject}."



principal = Principal("Mr. Samer", 50, "Management", 20)
vice = VicePrincipal("Ms. Lina", 40, "Science", "High School")
teacher = Teacher("Mr. Ahmed", 30, "Math", "Algebra")

print(principal.show_info())
print(principal.manage_school())
print(principal.hold_meeting())

print(vice.show_info())
print(vice.assist_principal())
print(vice.supervise_teachers())

print(teacher.show_info())
print(teacher.teach())
print(teacher.prepare_lessons())
