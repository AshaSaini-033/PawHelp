"""Explainable matching and overdue checks for PawHelp.

Matching is intentionally conservative: same user-entered area label, same food
category, sufficient quantity, active point, available offer, and available volunteer.
It does not calculate real-world distance or assess an animal's health or hunger.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any


def _date(value: str) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(value)
        if parsed.tzinfo is not None:
            parsed = parsed.astimezone().replace(tzinfo=None)
        return parsed
    except (TypeError, ValueError):
        return None


def find_overdue_points(points: list[dict[str, str]], now: datetime | None = None) -> list[dict[str, Any]]:
    now = now or datetime.now()
    overdue: list[dict[str, Any]] = []
    for point in points:
        if point.get("status", "").lower() != "active":
            continue
        last_visit = _date(point.get("last_confirmed_visit", ""))
        try:
            interval = float(point.get("visit_interval_hours", ""))
        except ValueError:
            continue
        if last_visit is None or interval <= 0:
            continue
        due_at = last_visit + timedelta(hours=interval)
        if due_at < now:
            overdue.append({**point, "due_at": due_at, "hours_overdue": round((now - due_at).total_seconds() / 3600, 1)})
    return sorted(overdue, key=lambda item: item["hours_overdue"], reverse=True)


def suggest_matches(
    points: list[dict[str, str]],
    offers: list[dict[str, str]],
    volunteers: list[dict[str, str]],
    now: datetime | None = None,
) -> list[dict[str, Any]]:
    """Return candidate combinations; suggestions never reserve or confirm anything."""
    now = now or datetime.now()
    suggestions: list[dict[str, Any]] = []
    for point in points:
        if point.get("status", "").lower() != "active":
            continue
        area = point.get("area_label", "").casefold()
        food = point.get("food_type_needed", "").casefold()
        try:
            required = float(point.get("quantity_needed", ""))
        except ValueError:
            continue
        last_visit = _date(point.get("last_confirmed_visit", ""))
        try:
            interval = float(point.get("visit_interval_hours", ""))
        except ValueError:
            continue
        due_at = last_visit + timedelta(hours=interval) if last_visit and interval > 0 else None
        overdue_hours = max(0.0, (now - due_at).total_seconds() / 3600) if due_at else 0.0

        for offer in offers:
            if offer.get("status", "").lower() != "available":
                continue
            if offer.get("area_label", "").casefold() != area:
                continue
            if offer.get("food_type", "").casefold() != food:
                continue
            if offer.get("quantity_unit", "").casefold() != point.get("quantity_unit", "").casefold():
                continue
            expiry = _date(offer.get("available_until", ""))
            try:
                offered = float(offer.get("quantity", ""))
            except ValueError:
                continue
            if expiry is None or expiry <= now or offered < required:
                continue

            for volunteer in volunteers:
                if volunteer.get("status", "").lower() != "available":
                    continue
                if volunteer.get("area_label", "").casefold() != area:
                    continue
                start = _date(volunteer.get("available_from", ""))
                end = _date(volunteer.get("available_until", ""))
                if start is None or end is None or not (start <= now <= end):
                    continue
                suggestions.append({
                    "point_id": point["point_id"],
                    "area_label": point["area_label"],
                    "food_type": food,
                    "quantity_needed": required,
                    "offer_id": offer["offer_id"],
                    "quantity_offered": offered,
                    "donor": offer["donor_alias"],
                    "volunteer_id": volunteer["volunteer_id"],
                    "volunteer": volunteer["volunteer_alias"],
                    "feeder": point["feeder_alias"],
                    "hours_overdue": round(overdue_hours, 1),
                    "priority": "Overdue" if overdue_hours > 0 else "Not overdue",
                })
    return sorted(suggestions, key=lambda item: item["hours_overdue"], reverse=True)
