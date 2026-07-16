from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.decision_log import DecisionLog

router = APIRouter()

@router.get("/history")
def get_history(db: Session = Depends(get_db)):

    decisions = db.query(DecisionLog).all()

    return decisions
