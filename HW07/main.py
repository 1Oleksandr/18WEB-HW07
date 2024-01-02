import argparse
from src.crud import get_groups, get_teachers, get_students, get_disciplines, get_grades, \
    create_group, update_group, remove_group, create_teacher, update_teacher, remove_teacher, \
    create_student, update_student, remove_student, create_discipline, update_discipline, \
    remove_discipline, create_grade, update_grade, remove_grade

parser = argparse.ArgumentParser(description='HW07 App')
parser.add_argument(
    '-a', '--action', help='Command: create, update, list, remove')
parser.add_argument(
    '-m', '--model', help='Models: Group, Teacher, Student, Discipline, Grade')
parser.add_argument('-n', '--name')
parser.add_argument('--id', help='number id in the table')
parser.add_argument('-g_id', '--group_id')
parser.add_argument('-t_id', '--teacher_id')
parser.add_argument('-st_id', '--student_id')
parser.add_argument('-d_id', '--discipline_id')
parser.add_argument('--grade')
parser.add_argument('--date')

arguments = parser.parse_args()

my_arg = vars(arguments)

action = my_arg.get('action')
model = my_arg.get('model')
name = my_arg.get('name')
grade = my_arg.get('grade')
date_of = my_arg.get('date')
_id = my_arg.get('id')
group_id = my_arg.get('group_id')
teacher_id = my_arg.get('teacher_id')
student_id = my_arg.get('student_id')
discipline_id = my_arg.get('discipline_id')


def main():
    match model:
        case 'Group':
            print('Model Group')
            match action:
                case 'create':
                    create_group(name=name)
                case 'list':
                    all = get_groups()
                    for r in all:
                        print(r.name)
                case 'update':
                    gr = update_group(_id=_id, name=name)
                    if gr:
                        print(gr.id, gr.name)
                    else:
                        print('Record not found!')
                case 'remove':
                    r = remove_group(_id=_id)
                    print(f'Remove {r} record')
                case _:
                    print('Wrong command!')
        case 'Teacher':
            print('Model Teacher')
            match action:
                case 'create':
                    create_teacher(fullname=name)
                case 'list':
                    all = get_teachers()
                    for r in all:
                        print(r.id, r.fullname)
                case 'update':
                    t = update_teacher(_id=_id, fullname=name)
                    if t:
                        print(t.id, t.fullname)
                    else:
                        print('Record not found!')
                case 'remove':
                    r = remove_teacher(_id=_id)
                    print(f'Remove {r} record')
                case _:
                    print('Wrong command!')
        case 'Student':
            print('Model Student')
            match action:
                case 'create':
                    create_student(fullname=name, group_id=_id)
                case 'list':
                    all = get_students()
                    num = 1
                    for r in all:
                        print(num, r.name, r.fullname)
                        num += 1
                case 'update':
                    st = update_student(
                        _id=_id, fullname=name, group_id=group_id)
                    if st:
                        print(st.id, st.fullname, st.group_id)
                    else:
                        print('Record not found!')
                case 'remove':
                    r = remove_student(_id=_id)
                    print(f'Remove {r} record')
                case _:
                    print('Wrong command!')
        case 'Discipline':
            print('Model Discipline')
            match action:
                case 'create':
                    create_discipline(name=name, teacher_id=teacher_id)
                case 'list':
                    all = get_disciplines()
                    for r in all:
                        print(r.id, r.name)
                case 'update':
                    d = update_discipline(
                        _id=_id, name=name, teacher_id=teacher_id)
                    if d:
                        print(d.id, d.name, d.teacher_id)
                    else:
                        print('Record not found!')
                case 'remove':
                    r = remove_discipline(_id=_id)
                    print(f'Remove {r} record')
                case _:
                    print('Wrong command!')
        case 'Grade':
            print('Model Grade')
            match action:
                case 'create':
                    create_grade(grade=grade, date_of=date_of,
                                 student_id=student_id, discipline_id=discipline_id)
                case 'list':
                    all = get_grades()
                    for r in all:
                        print(r.name, r.fullname, r.grade, r.date_of)
                case 'update':
                    gr = update_grade(_id=_id, grade=grade, date_of=date_of,
                                      student_id=student_id, discipline_id=discipline_id)
                    if gr:
                        print(gr.id, gr.grade, gr.date_of,
                              gr.student_id, gr.discipline_id)
                    else:
                        print('Record not found!')
                case 'remove':
                    r = remove_grade(_id=_id)
                    print(f'Remove {r} record')
        case _:
            print('Wrong command!')


if __name__ == '__main__':
    main()
