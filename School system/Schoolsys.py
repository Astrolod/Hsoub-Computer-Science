import sqlite3
import time


class Manage:

    def main(self):
        print("Welcome to School System")
        print(":::::::::\n"
              "Main Menu\n"
              ":::::::::\n"
              "to add a student press a.\n"
              "to add lesson to a student press l.\n"
              "to delete a student press d.\n"
              "to update a student information press u.\n"
              "to show a student information press s.\n"
              "to close the program press c.")
        while True:
            option = input("choose one of the options: ")
            if option == "a":
                return self.add_student()
            elif option == "l":
                return self.add_lesson(None)
            elif option == "d":
                return self.delete_student()
            elif option == "u":
                return self.update_student()
            elif option == "s":
                return self.show_students()
            elif option == "c":
                return None
            else:
                print("please enter a valid option")

    def add_student(self):
        print("::::::::::::::\n"
              "adding student\n"
              "::::::::::::::\n"
        "Enter the student's information, or press c to cancel and go back to main menu")
        while True:
            first_name = input("Enter First Name: ")
            if first_name == "c":
                return self.main()
            elif first_name.isalpha():
                break
            print("Invalid Entry, First Name must be in letters only")

        while True:
            last_name = input("Enter Last Name: ")
            if last_name == "c":
                return self.main()
            elif last_name.isalpha():
                break
            print("Invalid Entry, Last Name must be in letters only")

        while True:
            age = input("Enter Age: ")
            if age == "c":
                return self.main()
            elif age.isdigit():
                break
            print("Invalid Entry, Age must be in numbers")

        while True:
            class_ = input("Enter Class: ")
            if class_ == "c":
                return self.main()
            break

        while True:
            reg_date = input("Enter Registration Date: ")
            if reg_date == "c":
                return self.main()
            break

        exist = cursor.execute('''select * from students where FirstName = ? and LastName = ? and Age = ? and Class = ? and RegDate = ?''',
                       (first_name, last_name, age, class_, reg_date)).fetchone()
        if exist:
            print("Student Already Exist")
            return self.main()
        else:
            try:
                cursor.execute('''insert into students (FirstName, LastName, Age, Class, RegDate)
                values (?, ?, ?, ?, ?)''', (first_name, last_name, age, class_, reg_date))
                print("Student Added Successfully")
                student_id = cursor.lastrowid
                conn.commit()
                time.sleep(1)
                return self.add_lesson(student_id)
            except Exception as e:
                return print(e)

    def add_lesson(self, student_id):
        print("::::::::::::::\n"
              "adding lesson\n"
              "::::::::::::::")
        if not student_id:
            exist = [str(row[0]) for row in cursor.execute('''select student_id from students''')]
            print(f'IDs: {exist}')
            student_id = input("Enter Student ID, or press c to cancel and go back to main menu: ")
            if student_id == "c":
                return self.main()
            if student_id not in exist:
                print("There's no student with this ID")
                return self.add_lesson(None)
            print(cursor.execute('''select * from students where student_id = ?''', (student_id,)).fetchone())
            confirm = input("Is this the right student? press any key to continue, or press n to deny: ")
            if confirm == "n":
                return self.add_lesson(None)
        print("Lesson's list\n"
              "11. Islamic Studies\n"
              "22. Arabic Language\n"
              "33. English Language\n"
              "44. Math\n"
              "55. Physics\n"
              "66. Chemistry")
        valid_option = {"11", "22", "33", "44", "55", "66"}
        while True:
            lesson_id = input(
                "choose one of the options by typing its number, or press c to cancel and go back to main menu: ")
            if lesson_id == "c":
                return self.main()
            elif lesson_id in valid_option:
                exist = cursor.execute('''select 1 from s_l where student_id = ? and lesson_id = ?''',
                                       (student_id, lesson_id)).fetchone()
                if exist:
                    print("Student already have this lesson")
                elif not exist:
                    try:
                        cursor.execute('''insert into s_l (student_id, lesson_id) values (?, ?)''', (student_id, lesson_id))
                        print("Lesson Added Successfully")
                        conn.commit()
                    except Exception as e:
                        print(e)
                while True:
                    other = input("Do you want to add another lesson? y/n: ")
                    if other == "y":
                        return self.add_lesson(student_id)
                    elif other == "n":
                        return self.main()
                    print("Invalid Entry)")
            print("Invalid Entry, Choose one of the options")

    def delete_student(self):
        print("::::::::::::::\n"
              "deleting student\n"
              "::::::::::::::")
        exist = [int(row[0]) for row in cursor.execute('''select student_id from students''')]
        print(f'IDs: {exist}')
        while True:
            sid = input("Enter Student ID, or press c to cancel and go back to main menu: ")
            if sid == "c":
                return self.main()
            student_id = cursor.execute('''select student_id from students where student_id = ?''', (sid,)).fetchone()
            if student_id:
                print(cursor.execute('''select * from students where student_id = ?''', (sid,)).fetchone())
                while True:
                    confirm = input("Do you want to delete this student? y/n: ")
                    if confirm == "y":
                        try:
                            cursor.execute('''delete from students where student_id = ?''', (sid,))
                            cursor.execute('''delete from s_l where student_id = ?''', (sid,))
                            print("Student Deleted Successfully")
                            conn.commit()
                        except Exception as e:
                            print(e)
                        while True:
                            other = input("Do you want to delete another student? y/n: ")
                            if other == "y": return self.delete_student()
                            elif other == "n": return self.main()
                            print("Invalid entry")
                    elif confirm == "n": return self.delete_student()
                    print("Invalid entry")
            elif not student_id:
                print("There's no student with this ID")

    def update_student(self):
        print("::::::::::::::\n"
              "updating student\n"
              "::::::::::::::")
        exist = [int(row[0]) for row in cursor.execute('''select student_id from students''')]
        print(f'IDs: {exist}')
        student_id = input("Enter Student ID, or press c to cancel and go back to main menu: ")
        if student_id == "c":
            return self.main()
        exist = cursor.execute('''select student_id from students where student_id = ?''', (student_id,)).fetchone()
        if not exist:
            print("There's no student with this ID")
            return self.update_student()
        print(cursor.execute('''select * from students where student_id = ?''', (student_id,)).fetchone())
        confirm = input("Do you want to update this student? y/n: ")
        if confirm == "n":
            return self.update_student()
        elif confirm != "y":
            print("Invalid entry")

        while True:
            first_name = input("Enter First Name: ")
            if first_name == "c":
                return self.update_student()
            elif first_name.isalpha():
                break
            print("Invalid Entry, First Name must be in letters only")

        while True:
            last_name = input("Enter Last Name: ")
            if last_name == "c":
                return self.update_student()
            elif last_name.isalpha():
                break
            print("Invalid Entry, Last Name must be in letters only")

        while True:
            age = input("Enter Age: ")
            if age == "c":
                return self.update_student()
            elif age.isdigit():
                break
            print("Invalid Entry, Age must be in numbers")

        while True:
            class_ = input("Enter Class: ")
            if class_ == "c":
                return self.update_student()
            break

        while True:
            reg_date = input("Enter Registration Date: ")
            if reg_date == "c":
                return self.update_student()
            break

        try:
            cursor.execute('''update students set firstname = ?, lastname = ?, age = ?, class = ?, RegDate = ? 
            where student_id = ?''', (first_name, last_name, age, class_, reg_date, student_id))
            print("Student information updated successfully")
            conn.commit()
        except Exception as e:
            print(e)
        while True:
            other = input("Do you want to update another student? y/n: ")
            if other == "y":
                return self.update_student()
            elif other == "n":
                return self.main()
            print("Invalid Entry")

    def show_students(self):
        exist = [str(row[0]) for row in cursor.execute('''select student_id from students''').fetchall()]
        print(f'IDs: {exist}')

        students = (cursor.execute('''select student_id, firstname, lastname, class from students''').fetchall())
        if students: print(students)
        else:
            print("There are no students on the system currently")
            time.sleep(1.5)
            return self.main()
        while True:
            student_id = input("Enter Student ID to show its details, or press c to cancel and go back to main menu: ")
            if student_id == "c":
                return self.main()
            elif student_id in exist:
                try:
                    print(cursor.execute('''select students.student_id, students.firstname, students.lastname, students.age, students.class, students.RegDate,
                    group_concat(lessons.name, ', ')
                    from students
                    left join s_l on s_l.student_id = students.student_id
                    left join lessons on lessons.lesson_id = s_l.lesson_id
                    where students.student_id = ?
                    group by students.student_id''', (student_id,)).fetchone())
                except Exception as e:
                    print(e)
            else: print("There's no student with this ID")


if __name__ == '__main__':
    conn = sqlite3.connect('school_database.db')
    cursor = conn.cursor()

    Manage().main()

    conn.commit()
    conn.close()