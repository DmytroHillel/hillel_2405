from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from hw_22_for_lesson_22.alchemy_base import Base
from sqlalchemy.orm import relationship


class CourseTable(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    course_name = Column(String)
    instructor = Column(String)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship("StudentTable", back_populates="courses")
