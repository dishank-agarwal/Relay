# 🚀 Relay Control Plane

An API-first control plane for AI-driven payment operations.

Relay evaluates payment actions such as refunds against configurable business policies and risk rules, returning automated decisions like **APPROVED** or **MANUAL REVIEW**.

---

## 🌐 Live Demo

### Frontend
https://verdant-bubblegum-3b8ec4.netlify.app/

### Backend API (Swagger)
https://relay-api-8e8n.onrender.com/docs

### GitHub Repository
https://github.com/dishank-agarwal/Relay

---

# ✨ Features

- Evaluate payment decisions
- Policy-based rule engine
- Risk scoring
- Decision history
- RESTful API
- Interactive Swagger documentation
- Responsive React frontend
- Live deployment using Render and Netlify

---

# 🛠 Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Frontend

- React
- Vite
- Axios
- CSS

## Deployment

- Render
- Netlify
- GitHub

---

# 📸 Application

## Decision Evaluation

Users can submit:

- Merchant ID
- Transaction ID
- Action
- Amount

The system evaluates the request against configured policies and returns:

- Decision
- Policy matched
- Risk score
- Execution status
- Reason

---

## Decision History

Every evaluation is stored and displayed in a history table including:

- Merchant
- Transaction
- Decision
- Risk Score
- Execution Status
- Timestamp

---

# 🏗 Project Structure

```
Relay
│
├── app
│   ├── api
│   ├── database
│   ├── models
│   ├── schemas
│   ├── services
│   └── main.py
│
├── frontend
│   ├── src
│   ├── public
│   ├── package.json
│   └── vite.config.js
│
├── requirements.txt
└── README.md
```

---

# 🚀 Running Locally

## Backend

```bash
python -m venv .venv

source .venv/bin/activate
# Windows
.venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/health` | Health Check |
| POST | `/decision` | Evaluate Decision |
| GET | `/decisions` | Decision History |

Interactive API Documentation:

https://relay-api-8e8n.onrender.com/docs

---

# Example Decision

Request

```json
{
  "merchant_id": "M001",
  "transaction_id": "TX1001",
  "action": "REFUND",
  "amount": 75000
}
```

Response

```json
{
  "decision": "MANUAL_REVIEW",
  "policy": "REFUND_LIMIT_POLICY",
  "risk_score": 50,
  "reason": "Refund amount exceeds ₹50,000 threshold.",
  "can_execute": false
}
```

---

# Future Improvements

- JWT Authentication
- Merchant Management
- Dynamic Policy Management
- PostgreSQL Support
- Docker
- CI/CD Pipeline
- Rule Builder UI
- Analytics Dashboard

---

# Author

**Dishank Agarwal**

GitHub:
https://github.com/dishank-agarwal

---

## License

This project is licensed under the MIT License.