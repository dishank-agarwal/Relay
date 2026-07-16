from app.models.decision_log import DecisionLog
from app.schemas.decision import DecisionRequest
from app.services.policy_service import PolicyService

class DecisionService:

    @staticmethod
    def evaluate(request: DecisionRequest, db):

        result = PolicyService.evaluate(request, db)

        decision = DecisionLog(
            merchant_id=request.merchant_id,
            transaction_id=request.transaction_id,
            action=request.action,
            amount=request.amount,
            decision=result["decision"],
            reason=result["reason"],
            risk_score=result["risk_score"],
            policy=result["policy"],
            can_execute=result["can_execute"],
        )

        db.add(decision)
        db.commit()
        db.refresh(decision)

        return decision