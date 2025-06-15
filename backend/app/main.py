from fastapi import FastAPI

from .routers import risk, metrics, alert

app = FastAPI(title="Risk Analytics Dashboard API")

app.include_router(risk.router, prefix="/risk", tags=["risk"])
app.include_router(metrics.router, prefix="/metrics", tags=["metrics"])
app.include_router(alert.router, prefix="/alerts", tags=["alerts"])

@app.get("/")
def read_root():
    return {"message": "Risk Analytics Dashboard API"}

