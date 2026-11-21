<div align="center">

# 🐾 PawHelp
### Community feeding coordination for local street dogs

**A small local workflow to connect a confirmed feeding need, a real food offer, and a willing nearby volunteer.**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?logo=streamlit&logoColor=white) ![Data](https://img.shields.io/badge/Data-First--hand%20CSV-168C7B) ![Status](https://img.shields.io/badge/Status-Local%20MVP-F2B45B)

</div>

---

## The idea

People who regularly feed community dogs may coordinate food, locations, and helping hands through separate conversations. A feeder may know a point needs a visit, while a donor has suitable food and another person is free to help—but those pieces of information do not always meet.

**PawHelp makes those local records visible in one simple board.** It highlights check-ins that appear overdue and suggests compatible combinations of feeding point + food offer + available volunteer.

> **This is a coordination tool, not a rescue or veterinary service.** It cannot create volunteers, guarantee a delivery, decide whether an animal is hungry, or prove that food was eaten.

## How the workflow works

![PawHelp workflow — report a need, offer food, match, claim, confirm](docs/images/workflow.svg)

1. A feeder confirms a real feeding point and what is needed.
2. A donor records a real food offer, including quantity and expiry.
3. PawHelp checks whether the records are compatible.
4. A volunteer who is actually available can be contacted and agree to help.
5. The feeder/coordinator confirms what happened. A suggestion is never treated as a completed visit.

## How the matching logic works

![PawHelp matching logic — three record types from one CSV, compatibility filters and outputs](docs/images/matching-logic.svg)

A candidate match is shown only when all these checks pass:

- The feeding point is marked `active` and the food offer is `available`.
- All three records use the same manually entered `area_label`.
- Food category and quantity unit match.
- The available quantity is at least the quantity recorded as needed.
- The offer has not expired.
- The volunteer availability window includes the app current local time.

The overview also flags a feeding point when `last_confirmed_visit + visit_interval_hours` is earlier than the current local time. This is a reminder based on entered records, **not proof** that a point was missed.

## Current scope

### Included in this MVP
- Dashboard with counts, due/overdue check-in reminders, and candidate match suggestions.
- Add and view feeding points, food offers, and volunteer availability.
- CSV-based storage that is easy to inspect and explain during the follow-up call.
- Row validation for required fields, positive quantities, timestamps, and supported statuses.
- Six unit tests for the matching rules and validation.

### Not included intentionally
- GPS/live maps or true distance calculations. `area_label` equality is only a simple local approximation.
- Login, payments, chat, push notifications, or automatic dispatch.
- Combining multiple partial food offers into one request.
- Automatic reservation of offers or marking a delivery complete.
- Animal recognition, hunger detection, diagnosis, or feeding/diet recommendations.

## Tech stack

| Part | Choice | Why |
|---|---|---|
| App/UI | Python + Streamlit | A small interactive interface without spending the assignment on frontend setup |
| Data processing | Python + Pandas | Readable tables and transparent matching logic |
| Storage | One typed CSV (`backend/data.csv`) | The required raw data stays in a single inspectable file |
| Tests | Python `unittest` | Core rules can be checked without a live service or external API |

No external dataset, Kaggle data, or API data is used. The unified `backend/data.csv` starts with **a header only**; populate it with your own verified fieldwork records.

## Run locally

**Requirements:** Python 3.10 or newer.

1. Clone the repository: `git clone https://github.com/AshaSaini-033/PawHelp.git`
2. Enter the folder: `cd PawHelp`
3. Create a virtual environment: `python -m venv .venv`
4. Activate it:
   - Windows PowerShell: `.venv\Scripts\Activate.ps1`
   - macOS / Linux: `source .venv/bin/activate`
5. Install packages: `pip install -r backend/requirements.txt`
6. Start the app: `cd backend` then `streamlit run app.py`

Open the local URL printed by Streamlit (normally `http://localhost:8501`). The app reads and writes the unified `backend/data.csv` file. Each row has a `record_type` of `feeding_point`, `food_offer`, or `volunteer`.

### Run the tests

From the repository root, run: `python -m unittest discover -s tests -v`.

The current automated test suite checks compatible matching, area mismatch, quantity-unit mismatch, unavailable volunteers, overdue reminders, and invalid quantity input.

## Data format

| `record_type` | One row represents | Fields that matter |
|---|---|---|
| `feeding_point` | One real point confirmed by a feeder | Area, food need, quantity + unit, last confirmed visit, check interval |
| `food_offer` | One food contribution confirmed by its donor | Area, food category, quantity + unit, valid-until time |
| `volunteer` | One person confirmation of an availability window | Area, available-from and available-until times |

All records live in **one raw file: `backend/data.csv`**. Timestamps are entered in the computer local time as `YYYY-MM-DD HH:MM`. Quantity units must be comparable (for example, do not compare kilograms with portions). Use broad area labels, not private home addresses. Do not put phone numbers or sensitive personal data in this public CSV file.

## Current output with the repository blank CSV template

The committed `backend/data.csv` contains a header and no observations. With no real records, the app shows zero counts, no overdue points, and the empty-state message **No complete match is available right now.** That is expected until real fieldwork entries are entered. Do not add invented data to make the dashboard look busy.

After collecting the records, run the app again and add a screenshot of the genuine output to `docs/screenshots/`. Replace this section with a brief description of what your real data produced.

## Fieldwork and data integrity

This project is for a one-day take-home assignment that requires a problem observed within walking distance, a real person who is helped, and at least 20 first-hand data entries.

- **Place and visit date:** Complete in `fieldwork.md` after your visit.
- **Person helped (name + role):** Complete with their permission.
- **20+ real entries:** Collect and enter them yourself; the unified `backend/data.csv` is a blank template.
- **Evidence:** Add two timestamped photos you captured, with permission, and describe them in `fieldwork.md`.
- **Research:** Complete `research.md` after checking two sources and two existing solutions with the person.
- **Reflection:** Write `reflection.md` yourself. The assignment says this part must not be AI-written.

The project does not claim that local feeders have this problem until your conversation confirms it. If your fieldwork shows the actual bottleneck is different, change the tool to fit the person rather than forcing the person to fit the app.

## Safety, trust, and limitations

- Record only food that a knowledgeable local feeder says is suitable. Do not use PawHelp as dietary or veterinary advice.
- Never use spoiled/unsafe food or place food where it creates a road or public-safety hazard. Follow local rules and the guidance of experienced animal-welfare people.
- An offer is not proof of collection, delivery, or consumption. A candidate match is not an assignment; a claimed task is not confirmation.
- If nobody is available, the app cannot solve the transport gap. The need remains visible but unresolved.
- Records may be outdated, duplicated, inaccurate, or entered in error. Verify with the person before acting.
- Exact feeding locations, names, photos, and any identifying detail should be shared publicly only with permission. Use broad area labels and aliases in the app.

## Demo video

_Add your genuine 3-minute screen recording here after you have run the app using your collected records._

## Repository guide

```text
PawHelp/
├── backend/
│   ├── app.py                 # Streamlit user interface
│   ├── matching.py            # Explainable match + overdue logic
│   ├── validation.py          # CSV loading and row validation
│   ├── requirements.txt
│   ├── .streamlit/config.toml  # UI theme
│   └── data.csv               # 20+ first-hand typed records (header only initially)
├── docs/
│   ├── images/                # Workflow and matching diagrams
│   └── screenshots/           # Add genuine app screenshots here
├── tests/
│   └── test_engine.py
├── ai-chats/                  # Add your actual AI chat export here
├── research.md                # Fill with your real research
├── fieldwork.md               # Fill after your real visit
├── reflection.md              # Write yourself, without AI
└── README.md
```

## Next steps before submitting

- [ ] Confirm the problem and the exact person with your local feeder/coordinator.
- [ ] Complete `research.md` and `fieldwork.md` with real details.
- [ ] Collect at least 20 genuine entries in `backend/data.csv` and explain how each record type was collected.
- [ ] Add two timestamped photos with consent (avoid faces/private details).
- [ ] Run the app against your own records; add genuine screenshots and describe the actual output.
- [ ] Record and link your 3-minute demo.
- [ ] Write the half-page personal reflection yourself.
- [ ] Export the actual AI chats into `ai-chats/`.
- [ ] Keep making honest, incremental commits as you complete the work; do not manufacture timestamps or field evidence.

---

<div align="center">
**Built with care for community dogs and the people who look after them. 🐾**
</div>