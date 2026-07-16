from app.models.decision_log import DecisionLog
from app.schemas.decision import DecisionRequest

class DecisionService:

    @staticmethod
    def evaluate(request: DecisionRequest, db):

        if request.action == "REFUND" and request.amount > 50000:
            
            decision = DecisionLog(
                merchant_id = request.merchant_id,
                transaction_id = request.transaction_id,
                action = request.action,
                amount = request.amount,
                decision = "MANUAL_REVIEW",
                reason = "Refund amount exceeds ₹50,000 threshold.",
                risk_score = 75,
                policy = "REFUND_LIMIT_POLICY",
                can_execute = False,
            )

        else:

            decision = DecisionLog(
                merchant_id = request.merchant_id,
                transaction_id = request.transaction_id,
                action = request.action,
                amount = request.amount,
                decision = "APPROVED",
                reason = "Transaction satisfies all current policies.",
                risk_score = 20,
                policy = "DEFAULT_POLICY",
                can_execute = True,
            )

        db.add(decision)
        db.commit()
        db.refresh(decision)

        return decision