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

        for p in policies:
            print(
                "POLICY:",
                p.policy_id,
                p.rule,
                p.enabled
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
            "risk_score": 20,
            "can_execute": True
        }