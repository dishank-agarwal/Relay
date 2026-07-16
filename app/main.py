from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {
        "status" : "heathly",
        "service" : "Relay",
        "version" : "1.0.0"
    }
