from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.compatibility import router as compatibility_router


app = FastAPI(title="Name Compatibility API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(compatibility_router)
