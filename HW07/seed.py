from datetime import datetime, date, timedelta
from random import randint, choice

from faker import Faker
from sqlalchemy import select

from src.models import Teacher, Student, Discipline, Grade, Teacher
from src.db import session


def date_range(start: date, end: date) -> list:
    result = []
    current_date = start
    while current_date <= end:
        if current_date.isoweekday() < 6:
            result.append(current_date)
        current_date += timedelta(1)
    return result


def fill_data():

    disciplines = [
        "Вища математика",
        "Булева алгебра",
        "Дискретна математика",
        "Програмування",
        "Англійська мова",
        "Статистика",
        "Теорія ігор"
    ]

    groups = ["AM-92", "AT-92", "AP-92"]
    NUMBER_TEACHERS = 5
    NUMBER_STUDENTS = 50

    fake = Faker()

    def seed_teachers():
        for _ in range(NUMBER_TEACHERS):
            teacher = Teacher(fullname=fake.name())
            session.add(teacher)
        session.commit()

    def seed_disciplines():
        teacher_ids = session.scalars(select(Teacher.id)).all()
        for discipline in disciplines:
            session.add(Discipline(name=discipline,
                        teacher_id=choice(teacher_ids)))
        session.commit()

    def seed_groups():
        for group in groups:
            session.add(Teacher(name=group))
        session.commit()

    def seed_students():
        group_ids = session.scalars(select(Teacher.id)).all()
        for _ in range(NUMBER_STUDENTS):
            student = Student(fullname=fake.name(), group_id=choice(group_ids))
            session.add(student)
        session.commit()

    def seed_grades():
        start_date = datetime.strptime("2019-09-01", "%Y-%m-%d")
        end_date = datetime.strptime("2020-06-15", "%Y-%m-%d")
        d_range = date_range(start_date, end_date)
        discipline_ids = session.scalars(select(Discipline.id)).all()
        student_ids = session.scalars(select(Student.id)).all()

        for d in d_range:
            random_id_discipline = choice(discipline_ids)
            random_id_students = [choice(student_ids) for _ in range(5)]

            for student_id in random_id_students:
                grade = Grade(
                    grade=randint(1, 12),
                    date_of=d,
                    student_id=student_id,
                    discipline_id=random_id_discipline
                )
                session.add(grade)
        session.commit()

    seed_teachers()
    seed_disciplines()
    seed_groups()
    seed_students()
    seed_grades()


if __name__ == "__main__":
    fill_data()
