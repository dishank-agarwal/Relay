import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.database.database import SessionLocal
from app.models.policy import Policy

db = SessionLocal()

policy = Policy(
    policy_id = "REFUND_LIMIT_POLICY",
    rule = "REFUND_AMOUNT_GT_50000",
    priority = 1,
    enabled = True
)

db.add(policy)
db.commit()

db.close()

print("Policy created")