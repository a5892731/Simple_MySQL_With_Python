'''
author: a5892731
date: 2021-03-13
'''



import mysql.connector
from mysql.connector import Error


from shop_db_exercise_functions import create_connection_to_server, create_database, execute_query, execute_query, \
    create_connection_to_db, execute_sql_val

#------------------------------------------------------------------------------------------------------





if __name__ == "__main__":
    connection = create_connection_to_db("localhost", "root", "", "shop")

    sql = "INSERT INTO coustomers (name, last_name, city, street) VALUES (%s, %s, %s, %s)"
    val = [('Marek', 'Kowalski', 'Poznań', 'Długa 1/25'),
           ('Monika', 'Janoska', 'Łódź', 'Wąska 7a/4'),
           ('Mirosław', 'Dźięcioł', 'Gdańsk', 'Grunwaldzka 4'),
           ('Jakub', 'Zieliński', 'Gdynia', 'Śledziowa 41'),
           ]

    execute_sql_val(connection, sql, val)



