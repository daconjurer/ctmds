from sqlite3 import OperationalError

from fastapi import APIRouter
from loguru import logger
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from ctmds.core.db.session import engine, get_session

router = APIRouter(tags=["status"])


@router.get("/status")
async def read_system_status():
    with next(get_session()) as db:
        logger.debug(f"Checking database connection on {engine.url}")
        try:
            db.execute(text("SELECT 1"))
            return {"status": "OK"}
        except (SQLAlchemyError, OperationalError) as e:
            return {"status": "ERROR when connecting to database", "message": str(e)}
