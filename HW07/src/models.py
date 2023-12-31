from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(50), nullable=False)
    group_id = Column(ForeignKey("groups.id", ondelete="CASCADE"))
    group = relationship("Group", backref="students")


class Discipline(Base):
    __tablename__ = "disciplines"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    teacher_id = Column(ForeignKey("teachers.id", ondelete="CASCADE"))
    teacher = relationship("Teacher", backref="disciplines")


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    date_of = Column(Date, nullable=True)
    student_id = Column(ForeignKey("students.id", ondelete="CASCADE"))
    discipline_id = Column(ForeignKey("disciplines.id", ondelete="CASCADE"))
    student = relationship("Student", backref="grades")
    discipline = relationship("Discipline", backref="grades")


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(50), nullable=False)
