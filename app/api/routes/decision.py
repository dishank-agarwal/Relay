from fastapi import APIRouter

from app.schemas.decision import DecisionRequest
from app.services.decision_service import DecisionService

router = APIRouter()

@router.post("/decision")
def make_decision(request: DecisionRequest):
    decision = DecisionService.evaluate(request)

    return decision