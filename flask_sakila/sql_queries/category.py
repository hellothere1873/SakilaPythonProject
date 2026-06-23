from flask import request
from myutil.util import get_connection_cursor
from myutil.util import get_timestamp_now
'''
Return the information of all the categories. You are going to execute one SQL query.
'''
def get_categories():
    connection, cursor = get_connection_cursor("db/mysakila.db")

	# Select and display data from the 'category' table
    cursor.execute("SELECT * FROM category;")
    categories = cursor.fetchall()

    connection.close()

    categories_list = categories 
    print(f"get_categories(): {categories_list[0]}")
    return categories_list

'''
Delete a category and then return nothing. You are going to execute one SQL query.
'''
def del_category():
    connection, cursor = get_connection_cursor("db/mysakila.db")

    sql_q = f"DELETE FROM category WHERE category_id = {request.form['id']};"
    cursor.execute(sql_q)
    connection.commit()
    connection.close()

'''
Insert an category and then return a list of tuples with all the categories. You are going to execute two SQL queries.
'''
def insert_category(name):
    connection, cursor = get_connection_cursor("db/mysakila.db")
    last_update=get_timestamp_now()
    sql_q = f"INSERT INTO category (name, last_update) VALUES('{name}','{last_update}');"
    cursor.execute(sql_q)
    connection.commit()
    cursor.execute("SELECT * FROM category;")
    categories = cursor.fetchall()

    connection.close()

    categories_list = categories 
    print(f"get_categories(): {categories_list[0]}")
    return categories_list

'''
Return the information of a specific category.
'''
def get_category_by_id():
    connection, cursor = get_connection_cursor("db/mysakila.db")

    sql_q = f"SELECT * FROM category WHERE category_id = {request.form['id']};"
    cursor.execute(sql_q)
    category_info = cursor.fetchall()

    connection.close()
    return category_info

'''
Update the actor and then return a list of tuples with all the actors. You are going to execute two SQL queries.
'''
def edit_category(name):
    connection, cursor = get_connection_cursor("db/mysakila.db")
    last_update=get_timestamp_now()
    sql_q = f"UPDATE category SET  name = '{name}', last_update = '{last_update}' WHERE category_id = '{request.form['id']}';"
    cursor.execute(sql_q)
    connection.commit()
    cursor.execute("SELECT * FROM category;")
    categories = cursor.fetchall()

    connection.close()

    categories_list = categories 
    print(f"get_categories(): {categories_list[0]}")
    return categories_list