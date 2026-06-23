from flask import request
from myutil.util import get_connection_cursor
from myutil.util import get_timestamp_now
'''
Return the information of all the actors. You are going to execute one SQL query.
'''
def get_actors():
    connection, cursor = get_connection_cursor("db/mysakila.db")

	# Select and display data from the 'actor' table
    cursor.execute("SELECT * FROM actor;")
    actors = cursor.fetchall()

    connection.close()

    actors_list = actors 
    print(f"get_actors(): {actors_list[0]}")
    return actors_list

'''
Delete an actor and then return nothing. You are going to execute one SQL query.
'''
def del_actor():
    connection, cursor = get_connection_cursor("db/mysakila.db")

    sql_q = f"DELETE FROM actor WHERE actor_id = {request.form['id']};"
    cursor.execute(sql_q)
    connection.commit()
    connection.close()

'''
Insert an actor and then return a list of tuples with all the actors. You are going to execute two SQL queries.
'''
def insert_actor(fname, lname):
    connection, cursor = get_connection_cursor("db/mysakila.db")
    last_update=get_timestamp_now()
    sql_q = f"INSERT INTO actor (first_name, last_name, last_update) VALUES('{fname}','{lname}','{last_update}');"
    cursor.execute(sql_q)
    connection.commit()
    cursor.execute("SELECT * FROM actor;")
    actors = cursor.fetchall()

    connection.close()

    actors_list = actors 
    print(f"get_actors(): {actors_list[0]}")
    return actors_list

'''
Return the information of a specific actor.
'''
def get_actor_by_id():
    connection, cursor = get_connection_cursor("db/mysakila.db")

    sql_q = f"SELECT * FROM actor WHERE actor_id = {request.form['id']};"
    cursor.execute(sql_q)
    actor_info = cursor.fetchall()

    connection.close()
    return actor_info

'''
Update the actor and then return a list of tuples with all the actors. You are going to execute two SQL queries.
'''
def edit_actor(fname, lname):
    connection, cursor = get_connection_cursor("db/mysakila.db")
    last_update=get_timestamp_now()
    sql_q = f"UPDATE actor SET  first_name = '{fname}', last_name = '{lname}', last_update = '{last_update}' WHERE actor_id = '{request.form['id']}';"
    cursor.execute(sql_q)
    connection.commit()
    cursor.execute("SELECT * FROM actor;")
    actors = cursor.fetchall()

    connection.close()

    actors_list = actors 
    print(f"get_actors(): {actors_list[0]}")
    return actors_list