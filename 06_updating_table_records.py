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

def filling_the_table():

    sql = "INSERT INTO posts (title, description, user_id) VALUES (%s, %s, %s)"
    val = [('test1', "test1 dectiption", 3),
           ('test2', "test2 dectiption", 1,),
           ('test3', "test3 dectiption", 2),
        ]

    cursor = connection.cursor()
    cursor.executemany(sql, val)
    connection.commit()



if __name__ == "__main__":
    connection = create_connection("localhost", "root", "", "sm_app")

    filling_the_table()  # create table


    update_post_description = """
    UPDATE 
        posts
    SET 
        description = "The weather has become pleasant now"
    WHERE 
        id = 2
    """

    insetr_post_decription = """
    "INSERT INTO users (name, age, gender, nationality) VALUES (%s, %s, %s, %s)"
    """



    execute_query(connection, update_post_description)

