from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status" : "healthly",
        "service" : "Relay",
        "version" : "1.0.0"
    }