from databases import Database
from os import getenv


def init_app() -> Database:
    """Create databases instance to connect and disconnect.

    Returns:
        Database: Databases instance.
    """
    SQL_DATABASE_URI = getenv("SQL_DATABASE_URI")
    database = Database(url=SQL_DATABASE_URI)
    return database
