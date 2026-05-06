import os

# Only install pymysql as MySQLdb compatibility layer when the app is
# configured to use MySQL. This avoids import errors when using Postgres
# (e.g., DATABASE_URL contains 'postgres').
_db_url = os.environ.get("DATABASE_URL", "").lower()
_use_mysql = os.environ.get("USE_MYSQL", "").lower() == "true" or "mysql" in _db_url

if _use_mysql:
	try:
		import pymysql

		pymysql.install_as_MySQLdb()
	except Exception:
		# If pymysql is not installed or fails to initialize, skip gracefully.
		# The requirements already include `pymysql` for deployments that need it.
		pass
