from myutil.util import get_connection_cursor
import sqlite3

known_queries_lst = [
    "Actors with first name 'TOM'", "Actors with first name 'TOM'.",
    "Actor with most films", "Actor with most films.",
    "Count films per category", "Count films per category.",
    "What is the average running time of all the films", "What is the average running time of all the films?"
]

def process_query(q):
    connection, cursor = get_connection_cursor(dbname = "db/mysakila.db", row_factory_enabled = True)

    # Actor with most films
    if q == known_queries_lst[0] or q == known_queries_lst[1]:
        cursor.execute("SELECT *"
                        "FROM actor "
                        "WHERE first_name == 'TOM' "
                        )
        result = cursor.fetchall()
    elif q == known_queries_lst[2] or q == known_queries_lst[3]:
        cursor.execute("""SELECT a.actor_id, a.first_name, a.last_name, COUNT(fa.film_id) AS film_count
                        FROM film_actor fa
                        JOIN actor a ON fa.actor_id = a.actor_id
                        GROUP BY fa.actor_id
                        ORDER BY film_count DESC
                        LIMIT 1
                        """
                        )
        result = cursor.fetchall()
    elif q == known_queries_lst[4] or q == known_queries_lst[5]:
        cursor.execute("""SELECT c.category_id, c.name, COUNT(fc.category_id) AS category_count
                        FROM film_category fc
                        JOIN category c ON fc.category_id = c.category_id
                        GROUP BY fc.category_id
                        ORDER BY category_count DESC
                        """
                        )
        result = cursor.fetchall()
    elif q == known_queries_lst[6] or q == known_queries_lst[7]:
        cursor.execute("""SELECT ROUND(AVG(f.length)) AS Length_Average
                        FROM film f
                        """
                        )
        result = cursor.fetchall()
    else:
        result = "AI SQL query."

    connection.close()

    return result