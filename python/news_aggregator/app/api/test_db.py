from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.database import get_db

router = APIRouter()

@router.get("/db-test")
def test_db_connection(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT NOW() as now;")).fetchone()
    return {"db_time": result.now}
