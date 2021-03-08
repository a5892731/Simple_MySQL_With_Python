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
def execute_query(connection, query):

    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")



if __name__ == "__main__":
    connection = create_connection("localhost", "root", "", "sm_app")

    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
      id INT AUTO_INCREMENT, 
      name TEXT NOT NULL, 
      age INT, 
      gender TEXT, 
      nationality TEXT, 
      PRIMARY KEY (id)
    ) ENGINE = InnoDB
    """

    execute_query(connection, create_users_table)

    create_posts_table = """
    CREATE TABLE IF NOT EXISTS posts(
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
      title TEXT NOT NULL, 
      description TEXT NOT NULL, 
      user_id INTEGER NOT NULL, 
      FOREIGN KEY (user_id) REFERENCES users (id)
    );
    """

    execute_query(connection, create_posts_table)

    create_posts_table = """
    CREATE TABLE IF NOT EXISTS posts (
      id INT AUTO_INCREMENT, 
      title TEXT NOT NULL, 
      description TEXT NOT NULL, 
      user_id INTEGER NOT NULL, 
      FOREIGN KEY fk_user_id (user_id) REFERENCES users(id), 
      PRIMARY KEY (id)
    ) ENGINE = InnoDB
    """

    execute_query(connection, create_posts_table)
