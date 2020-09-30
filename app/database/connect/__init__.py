from fastapi import FastAPI
from databases import Database


def init_app(app: FastAPI, database: Database) -> FastAPI:
    """Create methods start and stop the database.

    Args:
        app (FastAPI): Object of app fastapi
        database (Database): Instance of db

    Returns:
        FastApi: return app modified
    """

    @app.on_event("startup")
    async def startup():
        await database.connect()

    @app.on_event("shutdown")
    async def shutdown():
        await database.disconnect()

    return app
