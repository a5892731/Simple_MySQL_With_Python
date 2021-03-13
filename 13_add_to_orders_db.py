'''
author: a5892731
date: 2021-03-13
'''

import mysql.connector
from mysql.connector import Error

from shop_db_exercise_functions import create_connection_to_server, create_database, execute_query, execute_query, \
    create_connection_to_db, execute_sql_val, execute_read_query


def select_order_price(shop_connection, shop_order_list_connection, order_name):


    select_ordered_products = "SELECT product_id, amount FROM {}".format(order_name)
    ordered_products = execute_read_query(shop_order_list_connection, select_ordered_products)
    order_value = 0
    print()
    for product in ordered_products: # where procuct is (product_id, quantity)
        print("product id: {} and quantity: {}".format(product[0], product[1]))

        select_select_price= "SELECT price FROM {} WHERE product_id <= {}".format("products", product[0])
        product_price = execute_read_query(shop_connection, select_select_price)

        product_value = product_price[0][0] * product[1]
        print("product price {} and total cost {}".format(product_price[0][0], round(product_value, 2)))
        order_value = order_value + product_value

    print("order value: {}".format(round(order_value, 2)))

    return round(order_value, 2)


#------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    shop_order_list_connection = create_connection_to_db("127.0.0.1", "root", "", "shop_order_list")
    shop_connection = create_connection_to_db("127.0.0.1", "root", "", "shop")

    order_number = 1
    order_name = "ord_{}".format(str(order_number))
    user_id = 1
    status = "zrealizowano"

    order_value = select_order_price(shop_connection, shop_order_list_connection, order_name)

    sql = "INSERT INTO {} (date, coustomer_id, order_name, order_value, status) VALUES (%s, %s, %s, %s, %s)".format("orders")
    val = [('SELECT DATE(NOW())', user_id, order_name, order_value, status,)]

    execute_sql_val(shop_connection, sql, val)


