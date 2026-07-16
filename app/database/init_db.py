from app.database.database import SessionLocal
from app.models.policy import Policy


def seed_default_policies():

    db = SessionLocal()

    try:

        existing = (
            db.query(Policy)
            .filter(
                Policy.policy_id == "REFUND_LIMIT_POLICY"
            )
            .first()
        )

        if not existing:

            policy = Policy(
                policy_id="REFUND_LIMIT_POLICY",
                rule="REFUND_AMOUNT_GT_50000",
                priority=1,
                enabled=True,
            )

            db.add(policy)
            db.commit()

            print("✅ Default policy created.")

        else:

            print("✅ Default policy already exists.")

    finally:

        db.close()