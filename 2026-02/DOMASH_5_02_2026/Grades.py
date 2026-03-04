import sqlite3

conn = sqlite3.connect("grades.db")
cursor = conn.cursor()

# CREATE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS student_grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    first_name TEXT,
    age INTEGER,
    country TEXT,
    city TEXT,
    group_name TEXT,
    subject TEXT,
    grade INTEGER,
    student_number TEXT,
    email TEXT
);
""")

# CLEAN (щоб не дублювалось при повторному запуску)
cursor.execute("DELETE FROM student_grades;")

# INSERT DATA
cursor.executemany("""
INSERT INTO student_grades
(full_name, first_name, age, country, city, group_name, subject, grade, student_number, email)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
""", [
    ("Борис Іваненко", "Борис", 20, "Україна", "Київ", "A1", "Математика", 72, "A77701", "boris@gmail.com"),
    ("Борис Іваненко", "Борис", 20, "Україна", "Київ", "A1", "Фізика", 65, "A77701", "boris@gmail.com"),
    ("Олена Коваль", "Олена", 21, "Україна", "Львів", "A1", "Математика", 92, "B12345", "olena@mail.com"),
    ("Олена Коваль", "Олена", 21, "Україна", "Львів", "A1", "Фізика", 88, "B12345", "olena@mail.com"),
    ("Іван Петренко", "Іван", 19, "Україна", "Харків", "B2", "Математика", 58, "C77799", "ivan@yahoo.com"),
    ("Іван Петренко", "Іван", 19, "Україна", "Харків", "B2", "Фізика", 61, "C77799", "ivan@yahoo.com"),
])

conn.commit()

# 1) full_name with MIN(grade) in range
cursor.execute("""
SELECT full_name
FROM student_grades
GROUP BY full_name
HAVING MIN(grade) BETWEEN 60 AND 75;
""")
print(cursor.fetchall())

# 2) students age = 20
cursor.execute("""
SELECT *
FROM student_grades
WHERE age = 20;
""")
print(cursor.fetchall())

# 3) students age between 18 and 22
cursor.execute("""
SELECT *
FROM student_grades
WHERE age BETWEEN 18 AND 22;
""")
print(cursor.fetchall())

# 4) students with first_name = 'Борис'
cursor.execute("""
SELECT *
FROM student_grades
WHERE first_name = 'Борис';
""")
print(cursor.fetchall())

# 5) students with student_number containing 777
cursor.execute("""
SELECT *
FROM student_grades
WHERE student_number LIKE '%777%';
""")
print(cursor.fetchall())

# 6) emails starting with 'b'
cursor.execute("""
SELECT email
FROM student_grades
WHERE email LIKE 'b%';
""")
print(cursor.fetchall())

conn.close()
