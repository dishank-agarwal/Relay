import { useState } from "react";
import api from "./api/api";

function App() {
  const [merchantId, setMerchantId] = useState("");
  const [transactionId, setTransactionId] = useState("");
  const [action, setAction] = useState("REFUND");
  const [amount, setAmount] = useState("");
  const [result, setResult] = useState(null);

  const evaluateDecision = async () => {
    try {
      const response = await api.post("/decision", {
        merchant_id: merchantId,
        transaction_id: transactionId,
        action: action,
        amount: Number(amount),
      });

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Failed to evaluate decision.");
    }
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>Relay Control Plane</h1>

      <div>
        <input
          placeholder="Merchant ID"
          value={merchantId}
          onChange={(e) => setMerchantId(e.target.value)}
        />
      </div>

      <br />

      <div>
        <input
          placeholder="Transaction ID"
          value={transactionId}
          onChange={(e) => setTransactionId(e.target.value)}
        />
      </div>

      <br />

      <div>
        <select
          value={action}
          onChange={(e) => setAction(e.target.value)}
        >
          <option value="REFUND">REFUND</option>
        </select>
      </div>

      <br />

      <div>
        <input
          type="number"
          placeholder="Amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />
      </div>

      <br />

      <button onClick={evaluateDecision}>
        Evaluate Decision
      </button>

      {result && (
        <div style={{ marginTop: "30px" }}>
          <h2>Decision Result</h2>

          <p><strong>Decision:</strong> {result.decision}</p>
          <p><strong>Policy:</strong> {result.policy}</p>
          <p><strong>Risk Score:</strong> {result.risk_score}</p>
          <p><strong>Reason:</strong> {result.reason}</p>
          <p><strong>Can Execute:</strong> {String(result.can_execute)}</p>
        </div>
      )}
    </div>
  );
}

export default App;