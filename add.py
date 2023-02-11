import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\baki\Desktop\СПб ' \
                 r'КИТ\Работы\БД\Студенты.accdb;'
    conn = pyodbc.connect(con_string)
    print("Connected To Database")

    Студенты = (11, 'Boyarinev', 'Pavel', 'Viktorovich', '07.12.2020', 'И', '203', '01.09.2022', 'М', '97540', '1')
    cur = conn.cursor()
    cur.execute('INSERT INTO Студенты VALUES (?,?,?,?,?,?,?,?,?,?,?)', Студенты)
    conn.commit()
    print('Data Inserted')
    print('Успешно')
except pyodbc.Error as e:
    print("Error in Connection")