from fastapi import FastAPI, WebSocket

from .routers import risk, metrics, alert
from .config import settings

app = FastAPI(title=settings.app_name)

app.include_router(risk.router, prefix="/risk", tags=["risk"])
app.include_router(metrics.router, prefix="/metrics", tags=["metrics"])
app.include_router(alert.router, prefix="/alerts", tags=["alerts"])

@app.get("/")
def read_root():
    return {"message": settings.app_name, "environment": settings.environment}


@app.websocket("/ws/risk")
async def risk_stream(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("risk_stream_connected")
    await websocket.close()

