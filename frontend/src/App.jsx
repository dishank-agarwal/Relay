import { useState, useEffect } from "react";

import api from "./api/api";

import DecisionForm from "./components/DecisionForm";
import DecisionResult from "./components/DecisionResult";
import DecisionHistory from "./components/DecisionHistory";

import "./App.css";

function App() {

    const [merchantId, setMerchantId] = useState("");
    const [transactionId, setTransactionId] = useState("");
    const [action, setAction] = useState("REFUND");
    const [amount, setAmount] = useState("");

    const [result, setResult] = useState(null);

    const [history, setHistory] = useState([]);

    const [loading, setLoading] = useState(false);

    const loadHistory = async () => {

      try {

        const response = await api.get("/decisions");

        setHistory(response.data);

      } catch (error) {

        console.error(error);

      }

  };

    const evaluateDecision = async () => {

        setLoading(true);

        try {

            const response = await api.post("/decision", {
                merchant_id: merchantId,
                transaction_id: transactionId,
                action: action,
                amount: Number(amount),
            });

            setResult(response.data);

            loadHistory();

        } catch (error) {

            console.error(error);
            alert("Failed to evaluate decision.");

        } finally {

            setLoading(false);

        }

    };

    useEffect(() => {

    loadHistory();

    }, []);

    return (

        <div className="container">

            <h1>Relay Control Plane</h1>

            <div className="dashboard">

    <DecisionForm
        merchantId={merchantId}
        setMerchantId={setMerchantId}
        transactionId={transactionId}
        setTransactionId={setTransactionId}
        action={action}
        setAction={setAction}
        amount={amount}
        setAmount={setAmount}
        evaluateDecision={evaluateDecision}
        loading={loading}
    />

    <DecisionResult result={result} />

</div>

<DecisionHistory history={history} />

        </div>

    );

}

export default App;