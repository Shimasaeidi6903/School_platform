from fastapi import FastAPI

app = FastAPI(
    title="School Platform API",
    version="1.0.0",
)


@app.get("/api/v1/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "school-platform-api",
    }
