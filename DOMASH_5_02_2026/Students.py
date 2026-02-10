import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student_grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    country TEXT,
    city TEXT,
    group_name TEXT,
    subject TEXT,
    grade INTEGER
)
""")

cursor.executemany("""
INSERT INTO student_grades (full_name, country, city, group_name, subject, grade)
VALUES (?, ?, ?, ?, ?, ?)
""", [
    ("Іван Петренко", "Україна", "Київ", "A1", "Математика", 85),
    ("Іван Петренко", "Україна", "Київ", "A1", "Фізика", 78),
    ("Олена Коваль", "Україна", "Львів", "A1", "Математика", 92),
    ("Олена Коваль", "Україна", "Львів", "A1", "Фізика", 88),
    ("Марек Новак", "Польща", "Краків", "B2", "Математика", 60),
    ("Марек Новак", "Польща", "Краків", "B2", "Фізика", 55),
])

conn.commit()


cursor.execute("SELECT * FROM student_grades")
print(cursor.fetchall())


cursor.execute("SELECT DISTINCT full_name FROM student_grades")
print(cursor.fetchall())


cursor.execute("""
SELECT full_name, AVG(grade)
FROM student_grades
GROUP BY full_name
""")
print(cursor.fetchall())


cursor.execute("""
SELECT full_name
FROM student_grades
GROUP BY full_name
HAVING MIN(grade) > 70
""")
print(cursor.fetchall())


cursor.execute("SELECT DISTINCT country FROM student_grades")
print(cursor.fetchall())


cursor.execute("SELECT DISTINCT city FROM student_grades")
print(cursor.fetchall())


cursor.execute("SELECT DISTINCT group_name FROM student_grades")
print(cursor.fetchall())


cursor.execute("""
SELECT subject
FROM student_grades
GROUP BY subject
HAVING AVG(grade) = (                          
    SELECT MIN(avg_grade)
    FROM (
        SELECT AVG(grade) AS avg_grade
        FROM student_grades
        GROUP BY subject
    )
)
""")
print(cursor.fetchall())

conn.close()
