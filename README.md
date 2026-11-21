<div align="center">

# 🐾 PawHelp
### Community feeding coordination for local street dogs

**A local coordination board connecting confirmed feeding needs, real food offers and willing volunteers.**

![Node.js](https://img.shields.io/badge/Backend-Node.js%20%2B%20Express-339933?logo=nodedotjs&logoColor=white) ![React](https://img.shields.io/badge/Frontend-React-61DAFB?logo=react&logoColor=20232a) ![CSV](https://img.shields.io/badge/Storage-CSV-168C7B)

</div>

---

## The idea

People who regularly feed community dogs may coordinate food, locations and helping hands through separate conversations. PawHelp puts confirmed local records in one place, highlights check-ins that may be overdue, and suggests compatible combinations of a feeding point, food offer and available volunteer.

> **PawHelp is a coordination tool, not a rescue or veterinary service.** It cannot create volunteers, guarantee delivery, assess animal hunger or prove that food was eaten.

## How it works

![PawHelp workflow](docs/images/workflow.svg)

1. A feeder confirms a real feeding point and the need.
2. A donor records a real food offer, quantity and expiry.
3. A volunteer records a genuine availability window.
4. PawHelp checks compatibility and displays suggestions.
5. People coordinate and confirm outside the app.

## Matching rules

A suggestion is displayed only when:
- The feeding point is active and the offer is available.
- Area labels match exactly (case-insensitive).
- Food category and quantity unit match.
- The offered quantity is at least the recorded need.
- The offer has not expired.
- The volunteer is available now and uses the same area label.

The app does not calculate GPS distance, reserve food, dispatch volunteers, or confirm delivery. An overdue reminder is based only on the feeder-entered last visit and interval; it is not proof that a point was missed.

## Tech stack

| Layer | Technology |
|---|---|
| Frontend | React + Vite |
| Backend | Node.js + Express |
| Storage | One inspectable CSV file |
| Tests | Node.js built-in test runner |

## Run locally

**Requirements:** Node.js 18+ and npm.

```bash
git clone https://github.com/AshaSaini-033/PawHelp.git
cd PawHelp
npm install
npm run dev
```

Open the Vite URL printed in the terminal (usually `http://localhost:5173`). The Express API runs on `http://localhost:4000`.

For a production build:

```bash
npm run build
NODE_ENV=production npm start
```

## Run tests

```bash
npm test
```

The tests cover compatible matching, area mismatch, insufficient quantity, expired offers, unavailable volunteers, overdue reminders and invalid quantities.

## Initial field observations and data integrity

`fieldwork/initial-observations.csv` records the locations and animal sightings you have described so far: Nescafe, cafeteria, hostel, parks, school/college roads, roadside garbage areas and nearby streets. These are **user-reported preliminary observations**, not independently verified field records. Dates, times and counts are intentionally blank because they have not yet been provided.

`backend/data.csv` is the app's operational dataset and currently contains only its header. Do not treat the preliminary observations as 20 fieldwork entries or as confirmed feeding needs, food offers or volunteer availability. The assignment's 20+ real entries still need to be collected and dated by you during fieldwork.

Record broad area labels rather than private home addresses. Use names/aliases only with permission; do not put phone numbers or sensitive personal data in this public repository.

Required before submission:
- [ ] Confirm the problem with one real local feeder/coordinator.
- [ ] Complete `research.md` and `fieldwork.md` with your own visit details.
- [ ] Collect at least 20 first-hand records in `backend/data.csv`.
- [ ] Add two timestamped photos in `evidence/`, with permission.
- [ ] Add genuine app screenshots in `docs/screenshots/`.
- [ ] Record and link your three-minute demo.
- [ ] Write `reflection.md` yourself, as required by the assignment.
- [ ] Add the actual AI chat export if required; summaries in `ai-chats/` are not verbatim transcripts.

## Safety and limitations

- Only record food that an experienced local feeder confirms is suitable.
- Do not use spoiled food or place food where it creates a road or public-safety hazard.
- A match is a suggestion, not an assignment or proof of delivery.
- If nobody is available, the need remains unresolved.
- Verify stale or duplicate records before acting.
- Respect local rules, campus permissions and privacy.

## Repository structure

```text
PawHelp/
├── backend/
│   ├── server.js
│   ├── matching.js
│   ├── validation.js
│   └── data.csv
├── frontend/src/
│   ├── App.jsx
│   ├── main.jsx
│   └── style.css
├── fieldwork/initial-observations.csv
├── docs/images/
├── evidence/
├── ai-chats/
├── tests/matching.test.js
├── package.json
└── README.md
```

<div align="center">

**Built with care for community animals and the people who look after them. 🐾**

</div>
