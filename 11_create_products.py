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

    db_name = "products"

    sql = "INSERT INTO {} (product_name, manufacturer, product_number, price) VALUES (%s, %s, %s, %s)".format(db_name)
    val = [('Młotek', 'NeoTools', 'H402', 129.90),
           ('Wkrętak krzyżowy', 'Yato', '4011', 35.00),
           ('Wkrętak krzyżowy', 'Yato', '4012', 35.00),
           ('Wkrętak płaski', 'Yato', '4001', 35.00),
           ('Wkrętak płaski', 'Yato', '4002', 35.00),
           ]

    execute_sql_val(connection, sql, val)
