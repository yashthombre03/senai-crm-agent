from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.dependencies import get_db
from backend.database.models import AuditLog

router = APIRouter()

@router.get("/audit")
def get_audit_logs(
    db: Session = Depends(get_db)
):

    return db.query(AuditLog).all()