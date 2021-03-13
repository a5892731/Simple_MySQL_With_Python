'''
author: a5892731
date: 2021-03-13
'''

import mysql.connector
from mysql.connector import Error

from shop_db_exercise_functions import create_connection_to_server, create_database, execute_query, execute_query





#------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    connection = create_connection_to_server("127.0.0.1", "root", "")

    create_database_query = "CREATE DATABASE shop"
    create_database(connection, create_database_query)
#-------------------------------------------------

    create_database_query = "CREATE DATABASE shop_order_list"
    create_database(connection, create_database_query)