from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from hw_22_for_lesson_22.alchemy_base import Base
from sqlalchemy.orm import relationship


class StudentTable(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    courses = relationship("CourseTable", back_populates="student")