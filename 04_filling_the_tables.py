'''
date: 2021-03-08
---------------------------------------------------------------------------------------------------------
this is first step script to learn for MySQL in Python


---------------------------------------------------------------------------------------------------------
links:
    https://realpython.com/python-sql-libraries/#mysql
    https://miroslawzelent.pl/kurs-mysql/
'''


import mysql.connector
from mysql.connector import Error



def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection
#------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    connection = create_connection("localhost", "root", "", "sm_app")

    sql = "INSERT INTO users (name, age, gender, nationality) VALUES (%s, %s, %s, %s)"
    val = [('James', 25, 'male', 'USA'),
           ('Leila', 32, 'female', 'France'),
           ('Brigitte', 35, 'female', 'England'),
           ('Mike', 40, 'male', 'Denmark'),
           ('Elizabeth', 21, 'female', 'Canada')]

    cursor = connection.cursor()
    cursor.executemany(sql, val)
    connection.commit()
