import view

main_dict = {}
student_name = []
lessons = []


def start():
    while True:
        opt = view.get_option()
        if opt == 1:
            student = view.get_student()
            main_dict[student] = {}
            student_name.append(student)
            if lessons:
                for ls in lessons:
                    main_dict[student][ls] = []
        elif opt == 2:
            lsn = view.get_lesson()
            lessons.append(lsn)
            for name in student_name:
                main_dict[name][lsn] = []
        elif opt == 3:
            name, lsn, grade = view.get_grade()
            main_dict[name][lsn].append(grade)
        elif opt == 4:
            for i, v in main_dict.items():
                print(i, ':',  v)
        elif opt == 5:
            name = view.get_students_grades()
            print(f"Оценки {name} - {main_dict[name]}")
        elif opt == 6:
            break
        print(main_dict)


