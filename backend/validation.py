"""Unified CSV loading and validation for PawHelp's first-hand local records."""

from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path

COLUMNS = (
    "record_type", "record_id", "recorded_at", "area_label", "food_type", "quantity",
    "quantity_unit", "last_confirmed_visit", "visit_interval_hours", "available_from",
    "available_until", "valid_until", "person_alias", "status", "notes",
)

RECORD_TYPES = {"feeding_point", "food_offer", "volunteer"}


def _parse_datetime(value: str) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(value)
        # Normalise timezone-aware values to the app machine's local clock.
        if parsed.tzinfo is not None:
            parsed = parsed.astimezone().replace(tzinfo=None)
        return parsed
    except (TypeError, ValueError):
        return None


def read_records(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    """Read data.csv and return valid rows plus row-specific issues."""
    if not path.exists():
        return [], [f"Missing file: {path}"]

    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        headers = set(reader.fieldnames or [])
        missing = set(COLUMNS) - headers
        if missing:
            return [], ["Missing required columns: " + ", ".join(sorted(missing))]

        records: list[dict[str, str]] = []
        issues: list[str] = []
        for line_number, raw in enumerate(reader, start=2):
            row = {key: (value or "").strip() for key, value in raw.items() if key}
            if not any(row.values()):
                continue
            errors = validate_row(row)
            if errors:
                issues.append(f"Row {line_number}: " + "; ".join(errors))
            else:
                records.append(row)
    return records, issues


def validate_row(row: dict[str, str]) -> list[str]:
    errors: list[str] = []
    for field in ("record_type", "record_id", "recorded_at", "area_label", "person_alias", "status"):
        if not row.get(field, "").strip():
            errors.append(f"{field} is blank")

    record_type = row.get("record_type", "").lower()
    if record_type and record_type not in RECORD_TYPES:
        errors.append("record_type must be feeding_point, food_offer, or volunteer")
    _check_datetime(row, "recorded_at", errors)

    if record_type == "feeding_point":
        for field in ("food_type", "quantity", "quantity_unit", "last_confirmed_visit", "visit_interval_hours"):
            if not row.get(field, ""):
                errors.append(f"{field} is required for feeding_point")
        _check_positive_number(row, "quantity", errors)
        _check_positive_number(row, "visit_interval_hours", errors)
        _check_datetime(row, "last_confirmed_visit", errors)
        _check_choice(row, "status", {"active", "paused"}, errors)
    elif record_type == "food_offer":
        for field in ("food_type", "quantity", "quantity_unit", "valid_until"):
            if not row.get(field, ""):
                errors.append(f"{field} is required for food_offer")
        _check_positive_number(row, "quantity", errors)
        _check_datetime(row, "valid_until", errors)
        _check_choice(row, "status", {"available", "reserved", "withdrawn"}, errors)
    elif record_type == "volunteer":
        for field in ("available_from", "available_until"):
            if not row.get(field, ""):
                errors.append(f"{field} is required for volunteer")
        _check_datetime(row, "available_from", errors)
        _check_datetime(row, "available_until", errors)
        _check_choice(row, "status", {"available", "unavailable"}, errors)
        start = _parse_datetime(row.get("available_from", ""))
        end = _parse_datetime(row.get("available_until", ""))
        if start and end and end <= start:
            errors.append("available_until must be after available_from")
    return errors


def _check_positive_number(row: dict[str, str], field: str, errors: list[str]) -> None:
    try:
        value = float(row.get(field, ""))
        if value <= 0:
            errors.append(f"{field} must be greater than zero")
    except ValueError:
        errors.append(f"{field} must be a number")


def _check_datetime(row: dict[str, str], field: str, errors: list[str]) -> None:
    value = row.get(field, "")
    if value and _parse_datetime(value) is None:
        errors.append(f"{field} must use YYYY-MM-DD HH:MM or ISO format")


def _check_choice(row: dict[str, str], field: str, choices: set[str], errors: list[str]) -> None:
    value = row.get(field, "").lower()
    if value and value not in choices:
        errors.append(f"{field} must be one of: {', '.join(sorted(choices))}")


def append_record(path: Path, record: dict[str, str]) -> None:
    """Validate and append one typed row; reject duplicate IDs and malformed input."""
    errors = validate_row(record)
    if errors:
        raise ValueError("; ".join(errors))

    if path.exists() and path.stat().st_size > 0:
        with path.open("r", encoding="utf-8-sig", newline="") as file:
            existing = csv.DictReader(file)
            if any((row.get("record_id") or "").strip() == record["record_id"] for row in existing):
                raise ValueError("record_id already exists; refresh the app and try again")

    path.parent.mkdir(parents=True, exist_ok=True)
    write_header = not path.exists() or path.stat().st_size == 0
    with path.open("a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=COLUMNS, extrasaction="ignore")
        if write_header:
            writer.writeheader()
        writer.writerow(record)
