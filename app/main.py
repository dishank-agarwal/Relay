from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import decision, health, history

from app.database.database import Base, engine
from app.database.init_db import seed_default_policies

from app.models import decision_log, policy

Base.metadata.create_all(bind=engine)

seed_default_policies()

app = FastAPI(
    title="Relay API",
    description="API-first control plane for AI-driven payment operations.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(decision.router)
app.include_router(history.router)