from fastapi import APIRouter

from backend.services.intelligence_service import (
    analyze_email
)

router = APIRouter()

@router.get("/intelligence/test")
def test():

    return analyze_email(

        sender="devops@internal.com",

        body="""
        URGENT:
        We suspect ransomware attack
        on production server.
        """
    )