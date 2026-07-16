from app.schemas.decision import DecisionRequest

class DecisionService:

    @staticmethod
    def evaluate(request: DecisionRequest):

        if request.action == "REFUND" and request.amount > 50000:
            return {
                "decision" : "MANUAL REVIEW",
                "reason" : "Refund amount exceeds ₹50,000 threshold.",
                "risk_score" : 75,
                "policy" : "REFUND_LIMIT_POLICY",
                "can_execute" : False,
            }
        
        return {
                "decision" : "APPROVED",
                "reason" : "Transaction satisfies all current policies.",
                "risk_score" : 20,
                "policy" : "DEFAULT_POLICY",
                "can_execute" : True,
        }