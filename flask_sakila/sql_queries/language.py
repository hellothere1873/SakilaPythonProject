from flask import request
from myutil.util import get_connection_cursor
from myutil.util import get_timestamp_now
'''
Return the information of all the languages. You are going to execute one SQL query.
'''
def get_languages():
    connection, cursor = get_connection_cursor("db/mysakila.db")

	# Select and display data from the 'language' table
    cursor.execute("SELECT * FROM language;")
    languages = cursor.fetchall()

    connection.close()

    languages_list = languages 
    print(f"get_languages(): {languages_list[0]}")
    return languages_list

'''
Delete an language and then return nothing. You are going to execute one SQL query.
'''
def del_language():
    connection, cursor = get_connection_cursor("db/mysakila.db")

    sql_q = f"DELETE FROM language WHERE language_id = {request.form['id']};"
    cursor.execute(sql_q)
    connection.commit()
    connection.close()

'''
Insert an language and then return a list of tuples with all the languages. You are going to execute two SQL queries.
'''
def insert_language(name):
    connection, cursor = get_connection_cursor("db/mysakila.db")
    last_update=get_timestamp_now()
    sql_q = f"INSERT INTO language (name, last_update) VALUES('{name}', '{last_update}');"
    cursor.execute(sql_q)
    connection.commit()
    cursor.execute("SELECT * FROM language;")
    languages = cursor.fetchall()

    connection.close()

    languages_list = languages 
    print(f"get_languages(): {languages_list[0]}")
    return languages_list

'''
Return the information of a specific language.
'''
def get_language_by_id():
    connection, cursor = get_connection_cursor("db/mysakila.db")

    sql_q = f"SELECT * FROM language WHERE language_id = {request.form['id']};"
    cursor.execute(sql_q)
    language_info = cursor.fetchall()

    connection.close()
    return language_info

'''
Update the language and then return a list of tuples with all the languages. You are going to execute two SQL queries.
'''
def edit_language(name):
    connection, cursor = get_connection_cursor("db/mysakila.db")
    last_update=get_timestamp_now()
    sql_q = f"UPDATE language SET  name = '{name}', last_update = '{last_update}' WHERE language_id = '{request.form['id']}';"
    cursor.execute(sql_q)
    connection.commit()
    cursor.execute("SELECT * FROM language;")
    languages = cursor.fetchall()

    connection.close()

    languages_list = languages 
    print(f"get_languages(): {languages_list[0]}")
    return languages_list