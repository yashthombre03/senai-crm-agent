from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.dependencies import get_db
from backend.database.models import Email

router = APIRouter()

@router.get(
    "/analytics/sentiment"
)
def sentiment_summary(
    db: Session = Depends(get_db)
):

    emails = db.query(Email).all()

    return [
        {
            "sender": e.sender,
            "sentiment": e.sentiment_score
        }
        for e in emails
    ]