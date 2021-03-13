'''
author: a5892731
date: 2021-03-13
'''

import mysql.connector
from mysql.connector import Error

from shop_db_exercise_functions import create_connection_to_server, create_database, execute_query, execute_query, \
    create_connection_to_db, execute_sql_val



#------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    shop_order_list_connection = create_connection_to_db("127.0.0.1", "root", "", "shop_order_list")

    order_number = 1
    order_name = "ord_{}".format(str(order_number))

    create_order_table = """
    CREATE TABLE IF NOT EXISTS {} (
      id INT AUTO_INCREMENT, 
      product_id INT,
      amount INT,
      PRIMARY KEY (id)
    ) ENGINE = InnoDB 
    """.format(str(order_number))

    execute_query(shop_order_list_connection, create_order_table)



    sql_order = "INSERT INTO {} (product_id, amount) VALUES (%s, %s)".format(order_name)
    val_order = [(1, 11),
                 (2, 14),
                 (3, 2),
                ]

    execute_sql_val(shop_order_list_connection, sql_order, val_order)

