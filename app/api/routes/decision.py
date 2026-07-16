from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
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