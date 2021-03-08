'''
date: 2021-03-08
---------------------------------------------------------------------------------------------------------
this is first step script to learn for MySQL in Python


---------------------------------------------------------------------------------------------------------
links:
    https://realpython.com/python-sql-libraries/#mysql
    https://miroslawzelent.pl/kurs-mysql/

    https://dev.mysql.com/doc/refman/5.5/en/reserved-words.html
'''


import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print(">>> Connection to MySQL DB successful")
    except Error as e:
        print(f">>> The error '{e}' occurred")
    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print(">>> Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


if __name__ == "__main__":

    connection = create_connection("127.0.0.1", "root", "")

    create_database_query = "CREATE DATABASE sm_app"
    create_database(connection, create_database_query)



