from sqlalchemy.orm import Session

from app.models.policy import Policy

class PolicyService:

    @staticmethod
    def evaluate(request, db:Session):

        policies = (
            db.query(Policy)
            .filter(Policy.enabled == True)
            .order_by(Policy.priority)
            .all()
        )

        for policy in policies:

            if(
                policy.rule == "REFUND_AMOUNT_GT_50000"
                and request.action == "REFUND"
                and request.amount > 50000
            ):
                
                return {
                    "triggered": True,
                    "policy": policy.policy_id,
                    "decision": "MANUAL_REVIEW",
                    "reason": "Refund amount exceeds ₹50,000 threshold.",
                    "risk_score": 75,
                    "can_execute": False
                }
            
        return {
            "triggered": False,
            "policy": "DEFAULT_POLICY",
            "decision": "APPROVED",
            "reason": "Transaction satisfies all current policies.",
            "can_execute": True
        }