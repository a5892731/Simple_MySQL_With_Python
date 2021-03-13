'''
author: a5892731
date: 2021-03-13
'''

import mysql.connector
from mysql.connector import Error

from shop_db_exercise_functions import create_connection_to_server, create_database, execute_query, execute_query, \
    create_connection_to_db



#------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    connection = create_connection_to_db("127.0.0.1", "root", "", "shop")


    create_products_table = """
    CREATE TABLE IF NOT EXISTS products (
      product_id INT AUTO_INCREMENT, 
      product_name CHAR(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci,
      manufacturer CHAR(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci, 
      product_number CHAR(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci,
      price FLOAT, 
      PRIMARY KEY (product_id)
    ) ENGINE = InnoDB 
    """

    create_coustomers_table = """
    CREATE TABLE IF NOT EXISTS coustomers (
      coustomer_id INT AUTO_INCREMENT, 
      name CHAR(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci,
      last_name CHAR(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci, 
      city CHAR(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci,
      street CHAR(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci,      
      PRIMARY KEY (coustomer_id)
    ) ENGINE = InnoDB 
    """

    create_orders_table = """
    CREATE TABLE IF NOT EXISTS orders (
      orders_id INT AUTO_INCREMENT, 
      date DATE,
      coustomer_id INT,
      order_name CHAR(20),
      order_value Float,
      status CHAR(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci,
      PRIMARY KEY (orders_id)
    ) ENGINE = InnoDB 
    """
    #date: YYYY-MM-DD


    execute_query(connection, create_products_table)
    execute_query(connection, create_coustomers_table)
    execute_query(connection, create_orders_table)
