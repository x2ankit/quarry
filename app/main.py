from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.documents import router as document_router
from app.api.upload import router as upload_router
from app.api.chat import router as chat_router
from app.api.health import router as health_router
app = FastAPI(
    title="Quarry",
    description="Quarry — AI Knowledge Infrastructure Platform",
    version="1.0.0",
)


@app.get("/")
def home():
    return {"message": "Quarry API"}


app.include_router(auth_router)
app.include_router(document_router)
app.include_router(upload_router)
app.include_router(chat_router)



app.include_router(health_router)