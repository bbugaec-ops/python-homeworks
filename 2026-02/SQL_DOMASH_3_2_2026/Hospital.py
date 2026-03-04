import sqlite3


connection = sqlite3.connect("hospital.sqlite")
cursor = connection.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS Doctors;
DROP TABLE IF EXISTS Examinations;
DROP TABLE IF EXISTS Wards;

CREATE TABLE IF NOT EXISTS Doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL ,
    Surname TEXT NOT NULL ,
    Phone TEXT,
    Salary REAL NOT NULL ,
    UNIQUE (Name,Surname)
);

CREATE TABLE IF NOT EXISTS Examinations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    DayOfWeek INTEGER NOT NULL ,
    StartTime TEXT NOT NULL ,
    EndTime TEXT NOT NULL ,
    Name TEXT NOT NULL UNIQUE,
    Wards_id INTEGER,
    FOREIGN KEY (Wards_id)
    REFERENCES Wards (id)
);

CREATE TABLE IF NOT EXISTS Diseases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL CHECK (Name <> ''),
    Severity INTEGER NOT NULL DEFAULT 1 CHECK (Severity >= 1)
);

CREATE TABLE IF NOT EXISTS Wards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Building INTEGER NOT NULL ,
    Floor INTEGER NOT NULL ,
    Name TEXT NOT NULL UNIQUE 
    
);
""")



# Додаємо 2 лікарів
cursor.execute("""
INSERT OR IGNORE INTO Doctors (Name, Surname, Phone, Salary)
VALUES (?, ?, ?, ?);
""", ('Maxim', 'Petrenko', '0987654321', 12500))
#doctor1_id = cursor.lastrowid


cursor.execute("""
INSERT OR IGNORE INTO Doctors (Name, Surname, Phone, Salary)
VALUES (?, ?, ?, ?);
""", ('Nicolas', 'Tomson', '0768934562', 11700))
#doctor2_id = cursor.lastrowid

cursor.execute("""
INSERT OR IGNORE INTO Wards (Building, Floor, Name)
VALUES (?, ?, ?);
""", (2, 4, "102-B"))
res = cursor.fetchone()


cursor.execute("SELEcT id FROM Wards WHERE Name = '102- B'")
res = cursor.fetchone()
if res:
    numer = res[0]


    cursor.execute("""
    INSERT OR IGNORE INTO Examinations (DayOfWeek, StartTime, EndTime, Name, Wards_id)
    VALUES (?, ?, ?, ?, ?);
    """, (1, "09:00", "09:30", "Blood test", numer))

    print("База Hospital створена!")


connection.commit()
connection.close()

# cursor.execute("SELECT * FROM Examinations")
# all_data = cursor.fetchone()
#
# if all_data:
#     print("Домашня !")
#     for row in all_data:
#         print(row)
# else:
#     print("Шось не вся ")
#
