from sqlalchemy import func, desc, select, and_

from src.models import Teacher, Student, Discipline, Group, Grade
from src.db import session


def select_1():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    result = session.query(Student.fullname,
                           func.round(func.avg(Grade.grade), 2).label('average_grade'))\
        .select_from(Grade) \
        .join(Student) \
        .group_by(Student.id) \
        .order_by(desc('average_grade')) \
        .limit(5).all()
    return result


def select_2(discipline_name):
    # Знайти студента із найвищим середнім балом з певного предмета.
    result = session.query(Discipline.name,
                           Student.fullname,
                           func.round(func.avg(Grade.grade),
                                      2).label('average_grade')
                           ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .filter(Discipline.name == discipline_name) \
        .group_by(Student.id, Discipline.name) \
        .order_by(desc('average_grade')) \
        .limit(1).all()
    return result


def select_3(discipline_name):
    # Знайти середній бал у групах з певного предмета.
    result = session.query(Discipline.name,
                           Group.name,
                           func.round(func.avg(Grade.grade),
                                      2).label('average_grade')
                           ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group) \
        .filter(Discipline.name == discipline_name) \
        .group_by(Discipline.name, Group.name) \
        .all()
    return result


def select_4():
    # Знайти середній бал на потоці (по всій таблиці оцінок).
    result = session.query(func.round(func.avg(Grade.grade), 2).label('average_grade')
                           ) \
        .select_from(Grade).all()
    return result


def select_5(teacher_id):
    # Знайти які курси читає певний викладач.
    result = session.query(Teacher.fullname,
                           Discipline.name
                           ) \
        .select_from(Teacher) \
        .join(Discipline) \
        .filter(Discipline.teacher_id == teacher_id) \
        .all()
    return result


def select_6(group_id):
    # Знайти список студентів у певній групі.
    result = session.query(Group.name,
                           Student.fullname
                           ) \
        .select_from(Student) \
        .join(Group) \
        .filter(Group.id == group_id) \
        .order_by(Student.fullname) \
        .all()
    return result


def select_7(group_id, discipline_id):
    # Знайти оцінки студентів у окремій групі з певного предмета
    result = session.query(Group.name,
                           Discipline.name,
                           Student.fullname,
                           Grade.grade
                           ) \
        .select_from(Grade) \
        .join(Discipline) \
        .join(Student) \
        .join(Group) \
        .filter(and_(Grade.discipline_id == discipline_id,
                     Student.group_id == group_id)) \
        .order_by(Group.name, Discipline.name, Student.fullname, desc(Grade.grade)) \
        .all()
    return result


def select_8(teacher_id):
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    result = session.query(Teacher.fullname,
                           func.round(func.avg(Grade.grade),
                                      2).label('average_grade')
                           ) \
        .select_from(Grade) \
        .join(Discipline) \
        .join(Teacher) \
        .filter(and_(Grade.discipline_id == Discipline.id, Discipline.teacher_id == teacher_id)) \
        .group_by(Teacher.id) \
        .all()
    return result


def select_9(student_id):
    # Знайти список курсів, які відвідує певний студент.
    result = session.query(Student.fullname,
                           Discipline.name
                           ) \
        .select_from(Grade) \
        .join(Discipline) \
        .join(Student) \
        .filter(and_(Grade.discipline_id == Discipline.id,
                     Grade.student_id == student_id)) \
        .group_by(Discipline.id, Student.fullname) \
        .all()
    return result


def select_10(student_id, teacher_id):
    # Список курсів, які певному студенту читає певний викладач.
    result = session.query(Student.fullname,
                           Teacher.fullname,
                           Discipline.name
                           ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Teacher) \
        .filter(and_(Grade.student_id == Student.id,
                     Grade.discipline_id == Discipline.id,
                     Discipline.teacher_id == teacher_id,
                     Student.id == student_id)) \
        .group_by(Student.id, Teacher.id, Discipline.id) \
        .all()
    return result


def select_11(teacher_id, student_id):
    # Середній бал, який певний викладач ставить певному студентові.
    result = session.query(Teacher.fullname,
                           Student.fullname,
                           func.round(func.avg(Grade.grade),
                                      2).label('average_grade')
                           ) \
        .select_from(Grade) \
        .join(Discipline) \
        .join(Teacher) \
        .join(Student) \
        .filter(and_(Grade.discipline_id == Discipline.id,
                     Discipline.teacher_id == teacher_id,
                     Grade.student_id == student_id)) \
        .group_by(Teacher.id, Student.id) \
        .all()
    return result


def select_12(discipline_id, group_id):
    # Оцінки студентів у певній групі з певного предмета на останньому занятті.
    subquery = (select(Grade.date_of).join(Student).join(Group)
                .where(and_(Grade.discipline_id == discipline_id, Group.id == group_id))
                .order_by(desc(Grade.date_of)).limit(1).scalar_subquery())

    result = session.query(Discipline.name,
                           Group.name,
                           Student.fullname,
                           Grade.grade,
                           Grade.date_of
                           ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group) \
        .filter(and_(Discipline.id == discipline_id, Group.id == group_id, Grade.date_of == subquery)) \
        .order_by(Student.fullname, desc(Grade.date_of)) \
        .all()
    return result


if __name__ == "__main__":

    res1 = select_1()
    print(
        f'Запит 1.\n5 студентів із найбільшим середнім балом з усіх предметів:\n')
    for s in res1:
        print(f'{s[0]} = {s[1]}')
    print('\n')

    res2 = select_2("Програмування")
    print(
        f'Запит 2.\nНайвищий середній бал по предмету {res2[0][0]} у студента {res2[0][1]}: {res2[0][2]}\n')

    res3 = select_3("Програмування")
    print(
        f'Запит 3.\nCередній бал з {res3[0][0]} у групах:\n {[(gr[1],gr[2]) for gr in res3]}\n')

    res4 = select_4()
    print(f'Запит 4.\nCередній бал на потоці: {res4[0][0]}\n')

    res5 = select_5(4)
    print(
        f'Запит 5.\nВикладач {res5[0][0]} викладає наступні предмети:\n {[d[1] for d in res5]}\n')

    res6 = select_6(1)
    print(
        f'Запит 6.\nCтуденти які навчаються у групі {res6[0][0]}:\n {[s[1] for s in res6]}\n')

    res7 = select_7(1, 1)
    print(
        f'Запит 7.\nОцінки студентів в групі {res7[0][0]} по {res7[0][1]}:')
    repeats = {}
    for r in res7:
        if r[2] not in repeats:
            grades = []
        grades.append(r[3])
        repeats[r[2]] = grades
    print(repeats)
    print('\n')

    res8 = select_8(2)
    print(
        f'Запит 8.\nCередній бал, який ставить викладач {res8[0][0]} зі своїх предметів {res8[0][1]}\n')

    res9 = select_9(25)
    print(
        f'Запит 9.\nCписок курсів, які відвідує {res9[0][0]}:  {[d[1] for d in res9]}\n')

    res10 = select_10(34, 2)
    print(
        f'Запит 10.\nСтуденту {res10[0][0]} викладач {res10[0][1]} читає наступні предмети {[d[2] for d in res10]}\n')

    res11 = select_11(3, 32)
    print(
        f'Запит 11.\nСередня оцінка студента {res11[0][1]} у викладача {res11[0][0]} становить: {res11[0][2]}\n')

    res12 = select_12(4, 1)
    print(
        f'Запит 12.\nОцінки студентів у групі {res12[0][1]} з предмету {res12[0][0]} на останньому занятті {res12[0][4]}:\n {[(r[2], r[3]) for r in res12]}\n')
