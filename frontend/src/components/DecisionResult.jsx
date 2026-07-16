function DecisionResult({ result }) {
  return (
    <div className="card">
      <h2>Decision Result</h2>

      {!result ? (
        <div className="empty-result">
          <p>🧠</p>
          <p>Evaluate a transaction to see the decision.</p>
        </div>
      ) : (
        <div className="result-details">
          <div className="result-row">
            <span className="label">Decision</span>

            <span
              className={
                result.decision === "APPROVED"
                  ? "badge approved"
                  : "badge review"
              }
            >
              {result.decision.replace("_", " ")}
            </span>
          </div>

          <div className="result-row">
            <span className="label">Policy</span>

            <span>{result.policy}</span>
          </div>

          <div className="result-row">
            <span className="label">Risk Score</span>

            <span
              className={
                result.risk_score >= 60
                  ? "badge high-risk"
                  : result.risk_score >= 30
                  ? "badge medium-risk"
                  : "badge low-risk"
              }
            >
              {result.risk_score}
            </span>
          </div>

          <div className="result-row">
            <span className="label">Reason</span>

            <span>{result.reason}</span>
          </div>

          <div className="result-row">
            <span className="label">Can Execute</span>

            <span
              className={
                result.can_execute
                  ? "badge approved"
                  : "badge rejected"
              }
            >
              {result.can_execute ? "YES" : "NO"}
            </span>
          </div>
        </div>
      )}
    </div>
  );
}

export default DecisionResult;