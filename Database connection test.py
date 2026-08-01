# .is_connected() Checks if the database is connected
# cursor.excute() To execute queries
# cursor.close() To close the method use to manipulate database
# connection.close() To close the database connection
import mysql.connector # connecting to database
from mysql.connector import Error # Used to show errors when it occurs
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="314159265358979",
        database="school"
    )
    # print(db) # Output <mysql.connector.connection_cext.CMySQLConnection object at 0x000001A8E76BD400>
    print('successfully connected to database')
    cursor = db.cursor()
    cursor.execute("""
        #  CREATE TABLE student
        # (
        #    student_id INT PRIMARY KEY,
        #    student_name VARCHAR(100),
        #    student_age  INT   
        # )
                   """)
    cursor.execute("insert into student values (1,'John',23),(2,'Nelson',20),(3,'Raph', 20)")
    print('successfully inserted into table')
    db.commit()

except Error as e:
    print(e)

# add =   lambda x,y: x+y
# print(add(1,2))