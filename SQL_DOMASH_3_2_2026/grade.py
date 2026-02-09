import sqlite3



def main():
    conn = sqlite3.connect("students.sqlite")
    cursor = conn.cursor()

    cursor.executescript("""
    DROP TABLE IF EXISTS grades;
    DROP TABLE IF EXISTS subjects;
    DROP TABLE IF EXISTS students;

    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        city TEXT NOT NULL,
        country TEXT NOT NULL,
        birth_date DATE NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone TEXT NOT NULL,
        group_name TEXT NOT NULL
    );

    CREATE TABLE subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    );

    CREATE TABLE grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        subject_id INTEGER NOT NULL,
        year INTEGER NOT NULL,
        grade REAL NOT NULL CHECK (grade >= 0 AND grade <= 12),
        FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
        FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
    );
    """)

    conn.commit()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    print("ТАБЛИЦІ:", cursor.fetchall())

    YEAR = 2026

    # студент
    cursor.execute("""
    INSERT INTO students(full_name, city, country, birth_date, email, phone, group_name)
    VALUES(?,?,?,?,?,?,?)
    """, ("Іван Петренко", "Київ", "Україна", "2003-05-12", "ivan@gmail.com", "+380991112233", "CS-21"))
    student1_id = cursor.lastrowid

    cursor.execute("""
    INSERT INTO students(full_name, city, country, birth_date, email, phone, group_name)
    VALUES(?,?,?,?,?,?,?)
    """, ("Оля Іваненко", "Львів", "Україна", "2004-02-20", "olya@gmail.com", "+380671234567", "CS-22"))
    student2_id = cursor.lastrowid

    cursor.execute("""
    INSERT INTO students(full_name, city, country, birth_date, email, phone, group_name)
    VALUES(?,?,?,?,?,?,?)
    """, ("Юлія Миколаївна","Житомир","Україна","2002-07-18","ulya@gmail.com","+38067349018","CS-23"))
    student3_id = cursor.lastrowid




    # предмети
    cursor.executemany("INSERT INTO subjects(name) VALUES(?)",
                       [("Математика",), ("Фізика",), ("Англійська",)])

    cursor.execute("SELECT id, name FROM subjects")
    subj = {name: sid for sid, name in cursor.fetchall()}

    # оцінки: (student_id, subject_id, year, grade)
    cursor.executemany(
        "INSERT INTO grades(student_id, subject_id, year, grade) VALUES(?,?,?,?)",
        [

          (student1_id, subj["Математика"], YEAR, 10),
            (student1_id, subj["Математика"], YEAR, 11),
            (student1_id, subj["Фізика"], YEAR, 7),
            (student1_id, subj["Фізика"], YEAR, 8),
            (student1_id, subj["Англійська"], YEAR, 9),
            (student1_id, subj["Англійська"], YEAR, 10),

            (student2_id, subj["Математика"], YEAR, 12),
            (student2_id, subj["Математика"], YEAR, 11),
            (student2_id, subj["Фізика"], YEAR, 9),
            (student2_id, subj["Фізика"], YEAR, 10),
            (student2_id, subj["Англійська"], YEAR, 8),
            (student2_id, subj["Англійська"], YEAR, 9),

            (student3_id, subj["Математика"], YEAR, 6),
            (student3_id, subj["Математика"], YEAR, 7),
            (student3_id, subj["Фізика"], YEAR, 8),
            (student3_id, subj["Фізика"], YEAR, 8),
            (student3_id, subj["Англійська"], YEAR, 11),
            (student3_id, subj["Англійська"], YEAR, 12)
        ]
    )

    conn.commit()

    # Звіт по студенту за рік (avg загальна + предмет min avg + предмет max avg)
    sql = """
    WITH per_subject AS (
        SELECT
            g.student_id,
            s.name AS subject_name,
            AVG(g.grade) AS subject_avg
        FROM grades g
        JOIN subjects s ON s.id = g.subject_id
        WHERE g.year = ?
        GROUP BY g.student_id, g.subject_id
    ),
    ranked AS (
        SELECT *,
            student_id,
            subject_name,
            subject_avg,
            ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY subject_avg ASC, subject_name ASC) AS rn_min,
            ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY subject_avg DESC, subject_name ASC) AS rn_max
        FROM per_subject
    ),
    total_avg AS (
        SELECT
            student_id,
            AVG(grade) AS avg_year_grade
        FROM grades
        WHERE year = ?
        GROUP BY student_id
    )
    SELECT
        st.full_name,
        st.city,
        st.country,
        st.birth_date,
        st.email,
        st.phone,
        st.group_name,
        ROUND(t.avg_year_grade, 2) AS avg_year_grade,
        (SELECT subject_name FROM ranked r WHERE r.student_id = st.id AND r.rn_min = 1) AS subject_min_avg,
        (SELECT subject_name FROM ranked r WHERE r.student_id = st.id AND r.rn_max = 1) AS subject_max_avg
    FROM students st
    LEFT JOIN total_avg t ON t.student_id = st.id
    ORDER BY st.full_name;
    """

    cursor.execute(sql, (YEAR, YEAR))
    rows = cursor.fetchall()

    print("\nЗВІТ:")
    for r in rows:
        print(r)


    conn.close()

if __name__ == "__main__":
    main()
