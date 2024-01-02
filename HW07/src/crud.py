from sqlalchemy import and_

from src.db import session
from src.models import Group, Teacher, Teacher, Student, Discipline, Grade


def get_groups():
    groups = session.query(Teacher).all()
    return groups


def get_teachers():
    teachers = session.query(Teacher).all()
    return teachers


def get_disciplines():
    teachers = session.query(Discipline).all()
    return teachers


def get_students():
    students = session.query(Teacher.name, Student.fullname).select_from(Student).join(
        Teacher).order_by(Teacher.name, Student.fullname).all()
    print(students)
    return students


def get_grades():
    grades = session.query(Discipline.name, Student.fullname, Grade.grade, Grade.date_of).select_from(Grade).join(
        Student).join(Discipline).order_by(Discipline.name, Student.fullname).all()
    return grades


def create_group(name):
    group = Group(name=name)
    session.add(group)
    session.commit()
    session.close()


def update_group(_id, name):
    group = session.query(Group).filter(Group.id == _id)
    if group:
        group.update({'name': name})
        session.commit()
    session.close()
    return group.first()


def remove_group(_id):
    r = session.query(Group).filter(Group.id == _id).delete()
    session.commit()
    session.close()
    return r


def create_teacher(fullname):
    teacher = Teacher(fullname=fullname)
    session.add(teacher)
    session.commit()
    session.close()


def update_teacher(_id, fullname):
    teacher = session.query(Teacher).filter(Teacher.id == _id)
    if teacher:
        teacher.update({'fullname': fullname})
        session.commit()
    session.close()
    return teacher.first()


def remove_teacher(_id):
    r = session.query(Teacher).filter(Teacher.id == _id).delete()
    session.commit()
    session.close()
    return r


def create_student(fullname, group_id):
    student = Student(fullname=fullname, group_id=group_id)
    session.add(student)
    session.commit()
    session.close()


def update_student(_id, fullname, group_id):
    teacher = session.query(Student).filter(Student.id == _id)
    if teacher:
        if fullname is None:
            teacher.update({'group_id': group_id})
        elif group_id is None:
            teacher.update({'fullname': fullname})
        else:
            teacher.update({'fullname': fullname, 'group_id': group_id})
        session.commit()
    session.close()
    return teacher.first()


def remove_student(_id):
    r = session.query(Student).filter(Student.id == _id).delete()
    session.commit()
    session.close()
    return r


def create_discipline(name, teacher_id):
    discipline = Discipline(name=name, teacher_id=teacher_id)
    session.add(discipline)
    session.commit()
    session.close()


def update_discipline(_id, name, teacher_id):
    d = session.query(Discipline).filter(Discipline.id == _id)
    if d:
        if name is None:
            d.update({'teacher_id': teacher_id})
        elif teacher_id is None:
            d.update({'name': name})
        else:
            d.update({'name': name, 'teacher_id': teacher_id})
        session.commit()
    session.close()
    return d.first()


def remove_discipline(_id):
    r = session.query(Discipline).filter(Discipline.id == _id).delete()
    session.commit()
    session.close()
    return r


def create_grade(grade, date_of, discipline_id, student_id):
    grade = Grade(grade=grade, date_of=date_of,
                  discipline_id=discipline_id, student_id=student_id)
    session.add(grade)
    session.commit()
    session.close()


def update_grade(_id, grade, date_of, student_id, discipline_id):
    r = session.query(Grade).filter(Grade.id == _id)
    gr = r.first()
    if r:
        r.update({'grade': grade if grade else gr.grade,
                  'date_of': date_of if date_of else gr.date_of,
                  'student_id': student_id if student_id else gr.student_id,
                  'discipline_id': discipline_id if discipline_id else gr.discipline_id})
        session.commit()
    session.close()
    return r.first()


def remove_grade(_id):
    r = session.query(Grade).filter(Grade.id == _id).delete()
    session.commit()
    session.close()
    return r
