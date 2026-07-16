function DecisionHistory({ history }) {
  return (
    <div className="card">
      <h2>Decision History</h2>

      <div className="table-container">
        <table className="history-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Merchant</th>
              <th>Transaction</th>
              <th>Decision</th>
              <th>Risk</th>
              <th>Execute</th>
              <th>Time</th>
            </tr>
          </thead>

          <tbody>
            {history.map((item) => (
              <tr key={item.id}>
                <td>{item.id}</td>

                <td>{item.merchant_id}</td>

                <td>{item.transaction_id}</td>

                <td>
                  <span
                    className={
                      item.decision === "APPROVED"
                        ? "badge approved"
                        : "badge review"
                    }
                  >
                    {item.decision.replace("_", " ")}
                  </span>
                </td>

                <td>
                  <span
                    className={
                      item.risk_score >= 60
                        ? "badge high-risk"
                        : item.risk_score >= 30
                        ? "badge medium-risk"
                        : "badge low-risk"
                    }
                  >
                    {item.risk_score}
                  </span>
                </td>

                <td>
                  <span
                    className={
                      item.can_execute
                        ? "badge approved"
                        : "badge rejected"
                    }
                  >
                    {item.can_execute ? "YES" : "NO"}
                  </span>
                </td>

                <td>
                  {new Date(item.created_at).toLocaleString("en-IN", {
                    dateStyle: "medium",
                    timeStyle: "short",
                  })}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default DecisionHistory;