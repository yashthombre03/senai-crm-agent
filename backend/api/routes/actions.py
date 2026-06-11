from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.dependencies import get_db
from backend.database.models import Action

router = APIRouter()

@router.get("/actions")
def get_actions(
    db: Session = Depends(get_db)
):
    return db.query(Action).all()