from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.dependencies import get_db

from backend.services.thread_service import (
    get_thread_history
)

router = APIRouter()

#Endpoint
@router.get(
    "/threads/{thread_id}"
)
def get_thread(
    thread_id: str,
    db: Session = Depends(get_db)
):

    emails = get_thread_history(
        db,
        thread_id
    )

    return emails