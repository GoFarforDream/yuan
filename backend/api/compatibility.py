from datetime import date

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from backend.services.compatibility import calculate_compatibility


router = APIRouter(prefix="/compatibility", tags=["compatibility"])


class CompatibilityRequest(BaseModel):
    name1: str = Field(..., min_length=1)
    name2: str = Field(..., min_length=1)
    birthday1: date | None = None
    birthday2: date | None = None


class CompatibilityResponse(BaseModel):
    name1: str
    name2: str
    birthday1: str | None
    birthday2: str | None
    score: int
    message: str
    chemistry: int
    rhythm: int
    destiny: int


@router.post("", response_model=CompatibilityResponse)
def create_compatibility(payload: CompatibilityRequest) -> dict[str, int | str]:
    try:
        return calculate_compatibility(
            payload.name1,
            payload.name2,
            payload.birthday1,
            payload.birthday2,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.get("", response_model=CompatibilityResponse)
def get_compatibility(
    name1: str,
    name2: str,
    birthday1: date | None = None,
    birthday2: date | None = None,
) -> dict[str, int | str]:
    try:
        return calculate_compatibility(name1, name2, birthday1, birthday2)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
