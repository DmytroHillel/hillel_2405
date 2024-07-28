
class Student:
    def __init__(self, name, second_name, age, average_mark):
        self.name = name
        self.second_name = second_name
        self.age = age
        self.average_mark = average_mark

    def student_presentation(self):
        return (f'This is {first_student.name} {first_student.second_name}, '
                f'he is {first_student.age} years old and he has {first_student.average_mark} average mark.')

    def change_mark(self, average_mark):
        self.average_mark = average_mark


first_student = Student(name='John', second_name='Palmer', age=17, average_mark=85)
print(first_student.student_presentation())
first_student.change_mark(120)
print(first_student.student_presentation())

