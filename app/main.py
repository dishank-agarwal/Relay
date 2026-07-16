from fastapi import FastAPI

from app.api.routes import decision, health

app = FastAPI(
    title="Relay API",
    description="API-first control plane for AI-driven payment operations.",
    version="1.0.0"
)

app.include_router(health.router)
app.include_router(decision.router)