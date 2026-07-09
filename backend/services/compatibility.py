from datetime import date
from functools import lru_cache
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
LEVEL_FILE = PROJECT_ROOT / "data" / "level.yaml"


def _text_to_number(text: str) -> int:
    """Match the original idea: take the first 8 bytes and view them as an integer."""
    raw = text.encode("utf-8")[:8].ljust(8, b"\0")
    return int.from_bytes(raw, byteorder="little", signed=False)


def _birth_to_number(birth_date: date | None) -> int:
    if birth_date is None:
        return 0
    digits = birth_date.strftime("%Y%m%d")
    return int(digits)


def _parse_score_messages(content: str) -> dict[int, str]:
    messages: dict[int, str] = {}
    in_scores = False

    for line in content.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped == "scores:":
            in_scores = True
            continue
        if not in_scores or ":" not in stripped:
            continue

        key, value = stripped.split(":", 1)
        key = key.strip().strip("'\"")
        if not key.isdigit():
            continue

        text = value.strip()
        if len(text) >= 2 and text[0] in {"'", '"'} and text[-1] == text[0]:
            text = text[1:-1]
        messages[int(key)] = text

    return messages


@lru_cache(maxsize=1)
def load_level_messages() -> dict[int, str]:
    if not LEVEL_FILE.exists():
        raise FileNotFoundError(f"Level config not found: {LEVEL_FILE}")

    return _parse_score_messages(LEVEL_FILE.read_text(encoding="utf-8"))


def calculate_compatibility(
    name1: str,
    name2: str,
    birthday1: date | None = None,
    birthday2: date | None = None,
) -> dict[str, int | str | None]:
    clean_name1 = name1.strip()
    clean_name2 = name2.strip()
    if not clean_name1 or not clean_name2:
        raise ValueError("name1 and name2 cannot be empty")

    total = (
        _text_to_number(clean_name1)
        + _text_to_number(clean_name2)
        + _birth_to_number(birthday1) * 31
        + _birth_to_number(birthday2) * 37
    )
    score = total % 101
    message = load_level_messages().get(score, "暂无对应文案")

    return {
        "name1": clean_name1,
        "name2": clean_name2,
        "birthday1": birthday1.isoformat() if birthday1 else None,
        "birthday2": birthday2.isoformat() if birthday2 else None,
        "score": score,
        "message": message,
        "chemistry": min(100, 35 + score // 2),
        "rhythm": (score * 7 + 13) % 101,
        "destiny": (score * 5 + 29) % 101,
    }
