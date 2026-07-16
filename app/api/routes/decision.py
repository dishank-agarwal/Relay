from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.decision_log import DecisionLog
from app.schemas.decision import DecisionRequest
from app.services.decision_service import DecisionService

router = APIRouter()

@router.post("/decision")
def make_decision(
    request: DecisionRequest,
    db: Session = Depends(get_db)
):
    decision = DecisionService.evaluate(request, db)

    return {
        "decision_id": decision.id,
        "decision": decision.decision,
        "reason": decision.reason,
        "risk_score": decision.risk_score,
        "policy": decision.policy,
        "can_execute": decision.can_execute,
    }

@router.get("/decision/{decision_id}")
def get_decision(
    decision_id: int,
    db: Session = Depends(get_db)
):
    decision = (
        db.query(DecisionLog)
        .filter(DecisionLog.id == decision_id)
        .first()
    )

    return decision

@router.get("/decisions")
def get_all_decisions(
    db: Session = Depends(get_db)
):

    decisions = (
        db.query(DecisionLog)
        .order_by(DecisionLog.id.desc())
        .all()
    )

    return decisions