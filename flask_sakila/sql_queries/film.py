from flask import request
from myutil.util import get_connection_cursor
from myutil.util import get_timestamp_now
'''
Return the information of all the films. You are going to execute one SQL query.
'''
def get_films():
    connection, cursor = get_connection_cursor("db/mysakila.db")

	# Select and display data from the 'film' table
    cursor.execute("SELECT * FROM film;")
    films = cursor.fetchall()

    connection.close()

    films_list = films 
    print(f"get_films(): {films_list[0]}")
    return films_list

'''
Delete an film and then return nothing. You are going to execute one SQL query.
'''
def del_film():
    connection, cursor = get_connection_cursor("db/mysakila.db", {'timeout': 15})
    sql_q = f"DELETE FROM film WHERE film_id = {request.form['id']};"
    cursor.execute(sql_q)
    connection.commit()
    connection.close()

'''
Insert a film and then return a list of tuples with all the films. You are going to execute two SQL queries.
'''
def insert_film(title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features):
    connection, cursor = get_connection_cursor("db/mysakila.db", 'timeout: 30')
    last_update=get_timestamp_now()
    sql_q = f"INSERT INTO film (title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, last_update) VALUES('{title}', '{description}', '{release_year}', '{language_id}','{original_language_id}', '{rental_duration}', '{rental_rate}', '{length}', '{replacement_cost}', '{rating}', '{special_features}', '{last_update}');"
    cursor.execute(sql_q)
    connection.commit()
    cursor.execute("SELECT * FROM film;")
    films = cursor.fetchall()

    connection.close()

    films_list = films 
    print(f"get_films(): {films_list[0]}")
    return films_list

'''
Return the information of a specific film.
'''
def get_film_by_id():
    connection, cursor = get_connection_cursor("db/mysakila.db")

    sql_q = f"SELECT * FROM film WHERE film_id = {request.form['id']};"
    cursor.execute(sql_q)
    film_info = cursor.fetchall()

    connection.close()
    return film_info

'''
Update the film and then return a list of tuples with all the films. You are going to execute two SQL queries.
'''
def edit_film(title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features):
    connection, cursor = get_connection_cursor("db/mysakila.db", 'timeout: 30')
    last_update=get_timestamp_now()
    sql_q = f"UPDATE film SET title = '{title}', description = '{description}', release_year = '{release_year}', language_id='{language_id}', original_language_id='{original_language_id}', rental_duration = '{rental_duration}', rental_rate = '{rental_rate}', length = '{length}', replacement_cost = '{replacement_cost}', rating = '{rating}', special_features = '{special_features}', last_update = '{last_update}' WHERE film_id = '{request.form['id']}';"
    cursor.execute(sql_q)
    connection.commit()
    cursor.execute("SELECT * FROM film;")
    films = cursor.fetchall()

    connection.close()

    films_list = films 
    print(f"get_films(): {films_list[0]}")
    return films_list
