import sqlite3

DB_NAME = "students.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS students
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       name
                       TEXT
                       NOT
                       NULL,
                       group_name
                       TEXT
                       NOT
                       NULL,
                       grade
                       INTEGER,
                       age
                       INTEGER
                   )
                   ''')
    conn.commit()
    conn.close()
    print("База данных инициализирована.")


def add_student(name, group_name, grade, age):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, group_name, grade, age) VALUES (?, ?, ?, ?)",
        (name, group_name, grade, age)
    )
    conn.commit()
    conn.close()
    print(f"Студент {name} добавлен.")


def show_all_students():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()

    if not students:
        print("База данных пуста.")
        return

    print("\n{:<5} {:<25} {:<12} {:<8} {:<5}".format("ID", "ФИО", "Группа", "Оценка", "Возраст"))
    print("-" * 60)
    for student in students:
        print("{:<5} {:<25} {:<12} {:<8} {:<5}".format(
            student[0], student[1], student[2], student[3], student[4]
        ))
    print()


def find_by_group(group_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE group_name = ?", (group_name,))
    students = cursor.fetchall()
    conn.close()

    if not students:
        print(f"Студенты в группе {group_name} не найдены.")
        return

    print(f"\nСтуденты группы {group_name}:")
    print("{:<5} {:<25} {:<12} {:<8} {:<5}".format("ID", "ФИО", "Группа", "Оценка", "Возраст"))
    print("-" * 60)
    for student in students:
        print("{:<5} {:<25} {:<12} {:<8} {:<5}".format(
            student[0], student[1], student[2], student[3], student[4]
        ))
    print()


def find_by_grade(grade):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE grade = ?", (grade,))
    students = cursor.fetchall()
    conn.close()

    if not students:
        print(f"Студенты с оценкой {grade} не найдены.")
        return

    print(f"\nСтуденты с оценкой {grade}:")
    print("{:<5} {:<25} {:<12} {:<8} {:<5}".format("ID", "ФИО", "Группа", "Оценка", "Возраст"))
    print("-" * 60)
    for student in students:
        print("{:<5} {:<25} {:<12} {:<8} {:<5}".format(
            student[0], student[1], student[2], student[3], student[4]
        ))
    print()


def update_grade(student_id, new_grade):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    if not student:
        print(f"Студент с ID {student_id} не найден.")
        conn.close()
        return

    cursor.execute(
        "UPDATE students SET grade = ? WHERE id = ?",
        (new_grade, student_id)
    )
    conn.commit()
    conn.close()
    print(f"Оценка студента {student[1]} изменена на {new_grade}.")


def delete_student(student_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    if not student:
        print(f"Студент с ID {student_id} не найден.")
        conn.close()
        return

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    print(f"Студент {student[1]} удалён.")
    show_all_students()


def average_grade():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(grade) FROM students")
    avg = cursor.fetchone()[0]
    conn.close()

    if avg is None:
        print("Нет данных для расчёта.")
        return

    print(f"\nСредняя оценка всех студентов: {avg:.2f}\n")


def add_sample_data():
    add_student("Иванов Иван", "ИСП-101", 5, 19)
    add_student("Петров Пётр", "ИСП-101", 4, 20)
    add_student("Сидоров Алексей", "ИСП-102", 3, 18)
    add_student("Смирнова Анна", "ИСП-102", 5, 19)
    add_student("Кузнецов Максим", "ИСП-101", 4, 21)


def main():
    init_db()


    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM students")
    if cursor.fetchone()[0] == 0:
        print("Добавляем тестовые данные...")
        add_sample_data()
    conn.close()

    while True:
        print("\n===== УЧЁТ СТУДЕНТОВ =====")
        print("1. Показать всех студентов")
        print("2. Добавить студента")
        print("3. Найти студентов по группе")
        print("4. Найти студентов по оценке")
        print("5. Изменить оценку")
        print("6. Удалить студента")
        print("7. Средняя оценка (доп. задание)")
        print("0. Выход")

        choice = input("\nВыберите действие: ").strip()

        if choice == "1":
            show_all_students()

        elif choice == "2":
            name = input("ФИО студента: ").strip()
            group = input("Группа: ").strip()
            try:
                grade = int(input("Оценка (1-5): "))
                age = int(input("Возраст: "))
                if 1 <= grade <= 5:
                    add_student(name, group, grade, age)
                else:
                    print("Оценка должна быть от 1 до 5.")
            except ValueError:
                print("Ошибка: введите число.")

        elif choice == "3":
            group = input("Введите название группы: ").strip()
            find_by_group(group)

        elif choice == "4":
            try:
                grade = int(input("Введите оценку: "))
                find_by_grade(grade)
            except ValueError:
                print("Ошибка: введите число.")

        elif choice == "5":
            try:
                student_id = int(input("ID студента: "))
                new_grade = int(input("Новая оценка (1-5): "))
                if 1 <= new_grade <= 5:
                    update_grade(student_id, new_grade)
                else:
                    print("Оценка должна быть от 1 до 5.")
            except ValueError:
                print("Ошибка: введите число.")

        elif choice == "6":
            try:
                student_id = int(input("ID студента для удаления: "))
                delete_student(student_id)
            except ValueError:
                print("Ошибка: введите число.")

        elif choice == "7":
            average_grade()

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
