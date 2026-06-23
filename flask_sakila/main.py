from flask import Flask, render_template, request, url_for, redirect, flash
import sqlite3
from datetime import datetime, timezone

from myutil.util import get_table_fields_names
from sql_queries.actor import get_actors, del_actor, insert_actor, get_actor_by_id, edit_actor
from sql_queries.category import get_categories, del_category, insert_category, get_category_by_id, edit_category
from sql_queries.film import get_films, del_film, insert_film, get_film_by_id, edit_film
from sql_queries.language import get_languages, del_language, insert_language, get_language_by_id, edit_language

from sql_queries.known_queries import process_query

#print(get_table_fields_names("db/mysakila.db", "film_actor"))

app = Flask(__name__)
app.secret_key = "super secret key" # dummy example, don't use in production

@app.route('/', methods=['GET', 'POST'])
def index():
	# Uncomment categories, films and languages (depending on your case) once you implement them
	return(render_template('index.html', heading="Index page", submit_query_link=url_for("free_txt_queries"), index_actor_link=url_for("actors_index"), index_category_link=url_for("categories_index"), index_film_link=url_for("films_index"), index_language_link=url_for("languages_index"),))

# =============================================================================================
# ACTORS
# =============================================================================================

# ACTORS INDEX
@app.route('/actors/index', methods=['GET', 'POST'])
def actors_index():
	actors_list = get_actors()
	return(render_template('/actors/index.html', heading="Listing actors", actors=actors_list, show_actor_link=url_for("show_actor"), update_actor_link=url_for("update_actor"), delete_actor_link=url_for("delete_actor"), create_actor_link=url_for("create_actor")))

# ACTORS DELETE
@app.route('/actors/delete', methods=['POST'])
def delete_actor():
	del_actor()
	return(redirect(url_for("actors_index")))	

# ACTORS CREATE
@app.route('/actors/create', methods=['GET', 'POST'])
def create_actor():
	return(render_template("/actors/create.html", heading="Create a new Actor", index_actor_link=url_for("actors_index"), save_actor_link=url_for("save_actor")))

# ACTORS CREATE SAVE
@app.route('/actors/save', methods=['POST'])
def save_actor():
	all_ok = True
	if len(request.form['first_name']) == 0:
		all_ok = False
		flash("Sorry the actor's first name cannot be empty. Try again.")
	if all_ok:
		actors_list = insert_actor(request.form['first_name'],request.form['last_name']) 
		return(render_template('/actors/index.html', heading="Listing actors", actors=actors_list, show_actor_link=url_for("show_actor"), update_actor_link=url_for("update_actor"), delete_actor_link=url_for("delete_actor"), create_actor_link=url_for("create_actor")))
	else:
		return(redirect(url_for("create_actor")))

# ACTORS UPDATE
@app.route('/actors/update', methods=['POST'])
def update_actor():
	actor_info = get_actor_by_id()
	return(render_template("/actors/update.html", heading="Editing actor", actor=actor_info, show_actor_link=url_for("show_actor"), index_actor_link=url_for("actors_index"), update_actor_save_link=url_for("save_actor_changes")))

# ACTORS UPDATE SAVE
@app.route('/actors/update_save', methods=['POST'])
def save_actor_changes():
	actors_list = edit_actor(request.form['first_name'],request.form['last_name'])
	return(render_template('/actors/index.html', heading="Listing actors", actors=actors_list, show_actor_link=url_for("show_actor"), update_actor_link=url_for("update_actor"), delete_actor_link=url_for("delete_actor"), create_actor_link=url_for("create_actor")))

# ACTORS SHOW
@app.route('/actors/show', methods=['POST'])
def show_actor():
	actor_info = get_actor_by_id()
	return(render_template('/actors/show.html', actor=actor_info, index_actor_link=url_for("actors_index"), update_actor_link=url_for("update_actor")))


# =============================================================================================
# CATEGORIES
# =============================================================================================

# categories INDEX
@app.route('/categories/index', methods=['GET', 'POST'])
def categories_index():
	categories_list = get_categories()
	return(render_template('/categories/index.html', heading="Listing categories", categories=categories_list, show_category_link=url_for("show_category"), update_category_link=url_for("update_category"), delete_category_link=url_for("delete_category"), create_category_link=url_for("create_category")))

# categories DELETE
@app.route('/categories/delete', methods=['POST'])
def delete_category():
	del_category()
	return(redirect(url_for("categories_index")))	

# categories CREATE
@app.route('/categories/create', methods=['GET', 'POST'])
def create_category():
	return(render_template("/categories/create.html", heading="Create a new category", index_category_link=url_for("categories_index"), save_category_link=url_for("save_category")))

# categories CREATE SAVE
@app.route('/categories/save', methods=['POST'])
def save_category():
	all_ok = True
	if len(request.form['name']) == 0:
		all_ok = False
		flash("Sorry the category's first name cannot be empty. Try again.")
	if all_ok:
		categories_list = insert_category(request.form['name']) 
		return(render_template('/categories/index.html', heading="Listing categories", categories=categories_list, show_category_link=url_for("show_category"), update_category_link=url_for("update_category"), delete_category_link=url_for("delete_category"), create_category_link=url_for("create_category")))
	else:
		return(redirect(url_for("create_category")))

# categories UPDATE
@app.route('/categories/update', methods=['POST'])
def update_category():
	category_info = get_category_by_id()
	return(render_template("/categories/update.html", heading="Editing category", category=category_info, show_category_link=url_for("show_category"), index_category_link=url_for("categories_index"), update_category_save_link=url_for("save_category_changes")))

# categories UPDATE SAVE
@app.route('/categories/update_save', methods=['POST'])
def save_category_changes():
	categories_list = edit_category(request.form['name'])
	return(render_template('/categories/index.html', heading="Listing categories", categories=categories_list, show_category_link=url_for("show_category"), update_category_link=url_for("update_category"), delete_category_link=url_for("delete_category"), create_category_link=url_for("create_category")))

# categories SHOW
@app.route('/categories/show', methods=['POST'])
def show_category():
	category_info = get_category_by_id() 
	return(render_template('/categories/show.html', category=category_info, index_category_link=url_for("categories_index"), update_category_link=url_for("update_category")))


# =============================================================================================
# FILMS
# =============================================================================================

# FILMS INDEX
@app.route('/films/index', methods=['GET', 'POST'])
def films_index():
	films_list = get_films()
	return(render_template('/films/index.html', heading="Listing films", films=films_list, show_film_link=url_for("show_film"), update_film_link=url_for("update_film"), delete_film_link=url_for("delete_film"), create_film_link=url_for("create_film")))

# FILMS DELETE
@app.route('/films/delete', methods=['POST'])
def delete_film():
	del_film()
	return(redirect(url_for("films_index")))	

# FILMS CREATE
@app.route('/films/create', methods=['GET', 'POST'])
def create_film():
	return(render_template("/films/create.html", heading="Create a new film", index_film_link=url_for("films_index"), save_film_link=url_for("save_film")))

# FILMS CREATE SAVE
@app.route('/films/save', methods=['POST'])
def save_film():
	all_ok = True
	if len(request.form['title']) == 0:
		all_ok = False
		flash("Sorry the film's title cannot be empty. Try again.")
	if all_ok:
		films_list = insert_film(request.form['title'], request.form['description'], request.form['release_year'], request.form['language_id'], request.form['original_language_id'], request.form['rental_duration'], request.form['rental_rate'], request.form['length'], request.form['replacement_cost'], request.form['rating'], request.form['special_features']) 
		

		return(render_template('/films/index.html', heading="Listing films", films = films_list ,show_film_link=url_for("show_film"), update_film_link=url_for("update_film"), delete_film_link=url_for("delete_film"), create_film_link=url_for("create_film")))
	else:
		return(redirect(url_for("create_film")))

# FILMS UPDATE
@app.route('/films/update', methods=['POST'])
def update_film():
	film_info = get_film_by_id()
	return(render_template("/films/update.html", heading="Editing film", film=film_info, show_film_link=url_for("show_film"), index_film_link=url_for("films_index"), update_film_save_link=url_for("save_film_changes")))

# FILMS UPDATE SAVE
@app.route('/films/update_save', methods=['POST'])
def save_film_changes():
	films_list = edit_film(request.form['title'], request.form['description'], request.form['release_year'], request.form['language_id'], request.form['original_language_id'], request.form['rental_duration'], request.form['rental_rate'], request.form['length'], request.form['replacement_cost'], request.form['rating'], request.form['special_features'])
	
	return(render_template('/films/index.html', heading="Listing films", films=films_list, show_film_link=url_for("show_film"), update_film_link=url_for("update_film"), delete_film_link=url_for("delete_film"), create_film_link=url_for("create_film")))

# FILMS SHOW
@app.route('/films/show', methods=['POST'])
def show_film():
	film_info = get_film_by_id()
	return(render_template('/films/show.html', film=film_info, index_film_link=url_for("films_index"), update_film_link=url_for("update_film")))

# =============================================================================================
# LANGUAGES
# =============================================================================================

# languages INDEX
@app.route('/languages/index', methods=['GET', 'POST'])
def languages_index():
	languages_list = get_languages()
	return(render_template('/languages/index.html', heading="Listing languages", languages=languages_list, show_language_link=url_for("show_language"), update_language_link=url_for("update_language"), delete_language_link=url_for("delete_language"), create_language_link=url_for("create_language")))

# languages DELETE
@app.route('/languages/delete', methods=['POST'])
def delete_language():
	del_language()
	return(redirect(url_for("languages_index")))	

# languages CREATE
@app.route('/languages/create', methods=['GET', 'POST'])
def create_language():
	return(render_template("/languages/create.html", heading="Create a new language", index_language_link=url_for("languages_index"), save_language_link=url_for("save_language")))

# languages CREATE SAVE
@app.route('/languages/save', methods=['POST'])
def save_language():
	all_ok = True
	if len(request.form['name']) == 0:
		all_ok = False
		flash("Sorry the language's first name cannot be empty. Try again.")
	if all_ok:
		languages_list = insert_language(request.form['name']) 

		return(render_template('/languages/index.html', heading="Listing languages", languages=languages_list , show_language_link=url_for("show_language"), update_language_link=url_for("update_language"), delete_language_link=url_for("delete_language"), create_language_link=url_for("create_language")))
	else:
		return(redirect(url_for("create_language")))

# languages UPDATE
@app.route('/languages/update', methods=['POST'])
def update_language():
	language_info = get_language_by_id()
	return(render_template("/languages/update.html", heading="Editing language", language=language_info, show_language_link=url_for("show_language"), index_language_link=url_for("languages_index"), update_language_save_link=url_for("save_language_changes")))

# languages UPDATE SAVE
@app.route('/languages/update_save', methods=['POST'])
def save_language_changes():
	languages_list = edit_language(request.form['name'])
	return(render_template('/languages/index.html', heading="Listing languages", languages=languages_list, show_language_link=url_for("show_language"), update_language_link=url_for("update_language"), delete_language_link=url_for("delete_language"), create_language_link=url_for("create_language")))

# languages SHOW
@app.route('/languages/show', methods=['POST'])
def show_language():
	language_info = get_language_by_id() 
	return(render_template('/languages/show.html', language=language_info, index_language_link=url_for("languages_index"), update_language_link=url_for("update_language")))

# =============================================================================================
# FREE TEXT QUERIES
# =============================================================================================

# FREE TEXT QUERIES INDEX
@app.route('/queries', methods=['POST'])
def free_txt_queries():
	all_ok = True
	print(f"{request.form['query']}")
	if len(request.form['query']) == 0:
		all_ok = False
		flash("Sorry the query cannot be empty. Try again.")
	if all_ok:
		results = process_query(request.form['query'])
		if len(results) > 0:
			field_names = list(dict(results[0]).keys())
		else:
			field_names = ["Empty result set."]

		return(render_template('/free_text_queries/show_dynamic_table.html', results=results, field_names=field_names, index_link=url_for("index")))
	else:
		return(redirect(url_for("index")))
