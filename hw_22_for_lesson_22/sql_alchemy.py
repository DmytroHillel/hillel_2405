from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from hw_22_for_lesson_22.alchemy_base import engine, Base
from hw_22_for_lesson_22.tables.students_table import StudentTable
from hw_22_for_lesson_22.tables.courses_table import CourseTable

import random

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Додавання нового студента
# new_student = StudentTable(name='Harry Potter', age=21, phone='094000333')
# session.add(new_student)
# session.commit()

# Видалення студента
# student = session.query(StudentTable).filter_by(name='Harry Potter').first()
# student.age = 22
# session.commit()


# Оновлення інформації про студента
# student = session.query(StudentTable).filter_by(name='Harry Potter').first()
# student.age = 22
# session.commit()
# student.age = 22
# session.commit()


#Додавання курсів та студентів до бази даних
# transfig_course = CourseTable(name='TF')
# potion_course = CourseTable(name='PC')
# dark_magic = CourseTable(name='DM')
# magles = CourseTable(name='MC')
# flying = CourseTable(name='FC')
#
# harry = StudentTable(name='Harry Potter', age=21, phone='094000333')
# ron = StudentTable(name='Ron Weasley', age=21, phone='094000555')
# george = StudentTable(name='George Weasley', age=23, phone='095000555')
# fred = StudentTable(name='Fred Weasley', age=23, phone='094000556')
# ginny = StudentTable(name='Ginny Weasley', age=20, phone='094000355')
# neville = StudentTable(name='Neville Longbottom', age=21, phone='094000111')
# sheimus = StudentTable(name='Sheimus Finnigan', age=21, phone='094000797')
# lavanda = StudentTable(name='Lavanda Rose', age=21, phone='094000544')
# drako = StudentTable(name='Drako Malfoy', age=21, phone='095000666')
# nino = StudentTable(name='Nino Dors', age=25, phone='094000121')
# artur = StudentTable(name='Artur James', age=20, phone='091000355')
# voland = StudentTable(name='Volan de Mort', age=55, phone='0933333333')
# mathiew = StudentTable(name='Mathiew Pot', age=24, phone='0956665544')
# vasia = StudentTable(name='Vasia Pupkin', age=23, phone='09400888')
# vasylina = StudentTable(name='Vasylina Gors', age=23, phone='095000000')
# toha = StudentTable(name='Toha Res', age=23, phone='0940003434')
# brand = StudentTable(name='Brand Pork', age=20, phone='092000355')
# nick = StudentTable(name='Nick Jugger', age=21, phone='094440111')
# kolya = StudentTable(name='Kolya Zolot', age=21, phone='091000797')
# lav = StudentTable(name='Lav Nokol', age=21, phone='094008844')
#
# courses = [transfig_course, potion_course, dark_magic, magles, flying]
# students = [harry, ron, george, fred, ginny, neville, sheimus, lavanda, drako, nino, artur, voland,
#             mathiew, vasia, vasylina, toha, brand, nick, kolya, lav]
#
#
# student_course_assignments = {}
#
#
# for student in students:
#     assigned_course = random.choice(courses)
#     student_course_assignments[student] = assigned_course
#
# for student, course in student_course_assignments.items():
#     session.add_all([student, course])

students = [StudentTable(first_name="Студент" + str(i)) for i in range(1, 21)]
session.add_all(students)

courses = [
    CourseTable(course_name="Основи Python", instructor="Іванов"),
    CourseTable(course_name="Веб-розробка з Django", instructor="Петров"),
    CourseTable(course_name="Машинне навчання", instructor="Сидоров"),
    CourseTable(course_name="Аналіз даних", instructor="Коваленко"),
    CourseTable(course_name="Тестування програмного забезпечення", instructor="Мельник")
]
session.add_all(courses)

# Рандомний розподіл студентів на курси
random.shuffle(students)
for i, student in enumerate(students):
    course = courses[i % len(courses)]
    student.courses.append(course)

session.commit()

