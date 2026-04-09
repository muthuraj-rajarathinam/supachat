from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.query import router as query_router

app = FastAPI()

# ✅ ADD THIS (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query_router)

@app.get("/health")
def health():
    return {"status": "ok"}