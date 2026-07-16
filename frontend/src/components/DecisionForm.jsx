function DecisionForm({
    merchantId,
    setMerchantId,
    transactionId,
    setTransactionId,
    action,
    setAction,
    amount,
    setAmount,
    evaluateDecision,
    loading,
}) {

    return (
        <div className="card">

            <h2>Evaluate Transaction</h2>

            <input
                placeholder="Merchant ID"
                value={merchantId}
                onChange={(e) => setMerchantId(e.target.value)}
            />

            <input
                placeholder="Transaction ID"
                value={transactionId}
                onChange={(e) => setTransactionId(e.target.value)}
            />

            <select
                value={action}
                onChange={(e) => setAction(e.target.value)}
            >
                <option value="REFUND">REFUND</option>
            </select>

            <input
                type="number"
                placeholder="Amount"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
            />

            <button
                onClick={evaluateDecision}
                disabled={loading}
            >
                {loading ? "Evaluating..." : "Evaluate Decision"}
            </button>

        </div>
    );
}

export default DecisionForm;