import sqlite3
from datetime import datetime, timezone

# Returns current time in UTC, in the format '%Y-%m-%d %H:%M:%S UTC', e.g. 2006-02-15 05:02:19.000
def get_timestamp_now():
	x = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f UTC")
	return x

# Enable 'row_factory_enabled' when processing free text queries
def get_connection_cursor(dbname, row_factory_enabled = False):
	connection = sqlite3.connect(dbname)
	if row_factory_enabled:
		connection.row_factory = sqlite3.Row
	return connection, connection.cursor()

def get_all_tables(dbname):
	connection = sqlite3.connect(dbname)
	cursor = connection.cursor()
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
	return cursor.fetchall()

def get_table_fields_names(dbname, table_name):
	connection, cursor = get_connection_cursor(dbname)
	connection.row_factory = sqlite3.Row
	cursor = connection.execute(f'SELECT * FROM {table_name}')
	row = cursor.fetchone()
	names = row.keys()

	return names