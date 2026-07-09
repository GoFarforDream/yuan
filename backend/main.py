from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.compatibility import router as compatibility_router


app = FastAPI(title="Name Compatibility API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

app.include_router(compatibility_router, prefix="/api")
