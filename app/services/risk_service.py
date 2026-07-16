class RiskService:

    @staticmethod
    def calculate(request):

        risk_score = 0
        risk_factors = []

        if request.action == "REFUND":
            risk_score += 10
            risk_factors.append("Refund transaction")

        if request.amount > 50000:
            risk_score += 40
            risk_factors.append("High refund amount")

        if request.amount > 100000:
            risk_score += 20
            risk_factors.append("Very high transacation amount")

        return {
            "risk_score": risk_score,
            "risk_factors": risk_factors
        }