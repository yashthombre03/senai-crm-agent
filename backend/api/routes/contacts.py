from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.dependencies import get_db
from backend.database.models import Contact

router = APIRouter()

@router.get("/contacts")
def get_contacts(
    db: Session = Depends(get_db)
):

    return db.query(Contact).all()