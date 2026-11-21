"""PawHelp — local community-dog feeding coordination MVP."""

from __future__ import annotations

import sys
from datetime import datetime, timedelta
from pathlib import Path
from uuid import uuid4

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data.csv"
sys.path.insert(0, str(ROOT))
from matching import find_overdue_points, suggest_matches  # noqa: E402
from validation import append_record, read_records  # noqa: E402

st.set_page_config(page_title="PawHelp | Local feeding coordination", page_icon="🐾", layout="wide")


def make_id(prefix: str) -> str:
    return f"{prefix}-{uuid4().hex[:7].upper()}"


def local_string(value: datetime) -> str:
    return value.strftime("%Y-%m-%d %H:%M")


def load_data():
    records, issues = read_records(DATA_FILE)
    points, offers, volunteers = [], [], []
    for row in records:
        record_type = row["record_type"]
        if record_type == "feeding_point":
            points.append({**row, "point_id": row["record_id"], "feeder_alias": row["person_alias"],
                           "food_type_needed": row["food_type"], "quantity_needed": row["quantity"]})
        elif record_type == "food_offer":
            offers.append({**row, "offer_id": row["record_id"], "donor_alias": row["person_alias"],
                           "available_until": row["valid_until"]})
        elif record_type == "volunteer":
            volunteers.append({**row, "volunteer_id": row["record_id"], "volunteer_alias": row["person_alias"]})
    return points, offers, volunteers, issues, len(records)


def save_record(record: dict[str, str]) -> None:
    append_record(DATA_FILE, record)


def show_records(rows, empty_message: str):
    if rows:
        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
    else:
        st.info(empty_message)


points, offers, volunteers, issues, record_count = load_data()
now = datetime.now()

st.title("🐾 PawHelp")
st.caption("A small coordination board for local community-dog feeders, food donors, and volunteers.")
st.warning(
    "PawHelp only coordinates people. It cannot assess animal health or hunger, guarantee a delivery, "
    "or replace advice from an experienced feeder or veterinarian. Only record food known to be suitable."
)

with st.sidebar:
    st.header("Local data")
    st.write(f"**Last loaded:** {now.strftime('%d %b %Y, %I:%M %p')} (this computer's local time)")
    st.metric("Real records in data.csv", record_count)
    st.metric("Active feeding points", sum(r.get("status") == "active" for r in points))
    st.metric("Available food offers", sum(r.get("status") == "available" for r in offers))
    st.metric("Available volunteers", sum(r.get("status") == "available" for r in volunteers))
    if st.button("↻ Reload data.csv", use_container_width=True):
        st.rerun()
    st.divider()
    st.caption("All records are stored in backend/data.csv. Back up the file before editing it manually.")

if issues:
    with st.expander(f"⚠️ Data needs attention ({len(issues)} issue(s))", expanded=True):
        for issue in issues:
            st.error(issue)

tab_overview, tab_points, tab_offers, tab_volunteers, tab_matches = st.tabs(
    ["Overview", "Feeding points", "Food offers", "Volunteers", "Match suggestions"]
)

with tab_overview:
    st.subheader("Today's local picture")
    overdue = find_overdue_points(points, now)
    matches = suggest_matches(points, offers, volunteers, now)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Active feeding points", sum(p.get("status") == "active" for p in points))
    c2.metric("Overdue check-ins", len(overdue))
    c3.metric("Candidate matches", len(matches))
    c4.metric("Open food offers", sum(o.get("status") == "available" for o in offers))

    st.markdown("#### Feeding points due for a check-in")
    if overdue:
        view = [{"Point": p["point_id"], "Area": p["area_label"], "Feeder": p["feeder_alias"],
                 "Hours overdue": p["hours_overdue"], "Due since": p["due_at"].strftime("%d %b, %H:%M")}
                for p in overdue]
        st.dataframe(pd.DataFrame(view), use_container_width=True, hide_index=True)
        st.caption("Overdue is calculated from the feeder-entered last confirmed visit and check interval. It is a reminder, not proof that animals have not been fed.")
    else:
        st.success("No active point is currently overdue based on the records entered.")

    st.markdown("#### Current limitations")
    st.write("Matches require the same manually entered area label, food category, and quantity unit. The app does not calculate GPS distance, combine partial donations, reserve food, or prove that food was delivered or eaten.")

with tab_points:
    st.subheader("Feeding points")
    show_records(points, "No feeding points recorded yet. Add a point only after observing it or confirming it with the feeder.")
    with st.expander("＋ Add a feeding point"):
        with st.form("add_point", clear_on_submit=True):
            area = st.text_input("Local area label", placeholder="Use a broad, agreed label — not a private home address")
            food = st.text_input("Food type needed", placeholder="Use the category confirmed by the feeder")
            left, right = st.columns(2)
            quantity = left.number_input("Quantity needed", min_value=0.1, step=0.5)
            unit = right.text_input("Quantity unit", placeholder="e.g. kg or portions")
            last_visit = st.datetime_input("Last confirmed visit (local time)", value=now - timedelta(hours=4))
            interval = st.number_input("Usual check interval (hours)", min_value=1.0, value=24.0, step=1.0)
            feeder = st.text_input("Feeder alias", help="Use a name/alias with consent. Do not add phone numbers.")
            notes = st.text_area("Observation / source note", placeholder="Who confirmed the need? What did you personally observe?")
            submitted = st.form_submit_button("Save feeding point", type="primary")
            if submitted:
                record = {"record_type": "feeding_point", "record_id": make_id("FP"), "recorded_at": local_string(now),
                          "area_label": area.strip(), "food_type": food.strip(), "quantity": str(quantity),
                          "quantity_unit": unit.strip(), "last_confirmed_visit": local_string(last_visit),
                          "visit_interval_hours": str(interval), "available_from": "", "available_until": "",
                          "valid_until": "", "person_alias": feeder.strip(), "status": "active", "notes": notes.strip()}
                try:
                    save_record(record)
                    st.success("Saved to data.csv. Reloading…")
                    st.rerun()
                except ValueError as exc:
                    st.error(str(exc))

with tab_offers:
    st.subheader("Food offers")
    show_records(offers, "No food offers recorded. Add only a real offer that the donor has confirmed.")
    with st.expander("＋ Add a food offer"):
        with st.form("add_offer", clear_on_submit=True):
            area = st.text_input("Area label", key="offer_area")
            food = st.text_input("Food category", key="offer_food")
            left, right = st.columns(2)
            quantity = left.number_input("Available quantity", min_value=0.1, step=0.5, key="offer_qty")
            unit = right.text_input("Quantity unit", key="offer_unit")
            expiry = st.datetime_input("Available until (local time)", value=now + timedelta(hours=8))
            donor = st.text_input("Donor alias")
            notes = st.text_area("Offer notes", placeholder="Any condition or pickup arrangement confirmed by the donor")
            submitted = st.form_submit_button("Save food offer", type="primary")
            if submitted:
                record = {"record_type": "food_offer", "record_id": make_id("OF"), "recorded_at": local_string(now),
                          "area_label": area.strip(), "food_type": food.strip(), "quantity": str(quantity),
                          "quantity_unit": unit.strip(), "last_confirmed_visit": "", "visit_interval_hours": "",
                          "available_from": "", "available_until": "", "valid_until": local_string(expiry),
                          "person_alias": donor.strip(), "status": "available", "notes": notes.strip()}
                try:
                    save_record(record)
                    st.success("Saved to data.csv. Reloading…")
                    st.rerun()
                except ValueError as exc:
                    st.error(str(exc))

with tab_volunteers:
    st.subheader("Volunteer availability")
    show_records(volunteers, "No volunteer availability recorded. Add a person only after they have agreed to help.")
    with st.expander("＋ Add volunteer availability"):
        with st.form("add_volunteer", clear_on_submit=True):
            area = st.text_input("Area label", key="vol_area")
            alias = st.text_input("Volunteer alias", help="Use a name/alias with consent; do not add contact details.")
            left, right = st.columns(2)
            start = left.datetime_input("Available from", value=now)
            end = right.datetime_input("Available until", value=now + timedelta(hours=3))
            submitted = st.form_submit_button("Save availability", type="primary")
            if submitted:
                record = {"record_type": "volunteer", "record_id": make_id("VL"), "recorded_at": local_string(now),
                          "area_label": area.strip(), "food_type": "", "quantity": "", "quantity_unit": "",
                          "last_confirmed_visit": "", "visit_interval_hours": "", "available_from": local_string(start),
                          "available_until": local_string(end), "valid_until": "", "person_alias": alias.strip(),
                          "status": "available", "notes": ""}
                try:
                    save_record(record)
                    st.success("Saved to data.csv. Reloading…")
                    st.rerun()
                except ValueError as exc:
                    st.error(str(exc))

with tab_matches:
    st.subheader("Candidate matches")
    st.caption("Suggestions only. PawHelp does not automatically assign a donor or volunteer.")
    if matches:
        frame = pd.DataFrame(matches)
        frame = frame.rename(columns={"point_id": "Feeding point", "area_label": "Area", "food_type": "Food",
                                      "quantity_needed": "Needed", "quantity_offered": "Offered", "donor": "Donor",
                                      "volunteer": "Available volunteer", "feeder": "Feeder", "priority": "Check-in status",
                                      "hours_overdue": "Hours overdue"})
        st.dataframe(frame, use_container_width=True, hide_index=True)
        st.info("Next step: contact the feeder/coordinator and donor through your agreed local channel. Mark a task completed only after the feeder confirms it. This MVP does not send messages or reserve offers.")
    else:
        st.info("No complete match is available right now. A match requires an active feeding point, an unexpired compatible offer with enough quantity, and a volunteer whose availability window includes the current local time in the same area label.")

st.divider()
st.caption("PawHelp • First-hand records in data.csv • Use approximate locations • Verify before acting")
