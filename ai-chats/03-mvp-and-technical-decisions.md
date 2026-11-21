# AI discussion 03 — MVP scope, matching logic and technical choices

**Purpose:** Capture why the first PawHelp version was kept deliberately small.

**Evidence status:** This records design reasoning and implementation decisions. It is not a transcript of exact prompts and answers.

## 1. Why not build a full rescue platform?

A rescue platform would need a dependable responder network, transport, emergency escalation, veterinary support and clear responsibility. A student prototype cannot promise these services. The project was therefore narrowed to community-dog feeding coordination, where a local feeder can confirm the need and people can voluntarily coordinate food and help.

## 2. What should the first version do?

- Record a feeding point confirmed by a feeder.
- Record the food type and quantity the feeder says is needed.
- Record a donor's actual food offer, quantity and valid-until time.
- Record a volunteer's actual availability window.
- Show overdue check-in reminders.
- Suggest compatible combinations and explain why they match.
- Keep all records inspectable in one CSV file.

## 3. How should matching work?

The first version uses explicit rules rather than machine learning:

1. The feeding point is active.
2. The food offer is available and has not expired.
3. The manually entered area labels match.
4. The food categories match.
5. The quantity units match.
6. The offer quantity is at least the recorded quantity needed.
7. The volunteer's availability window includes the app's current local time.

This is intentionally conservative. The app does not calculate GPS distance; two identical area labels do not prove that a person can safely or conveniently travel between those places.

## 4. Why flag overdue feeding points?

A reminder can be calculated from the feeder-entered last-confirmed visit and the usual check interval. This makes it easier to notice a point that may need follow-up.

It must be labelled as a **check-in reminder**, not as proof that animals were not fed. Another person may have visited without updating the record, or the interval may no longer be correct.

## 5. Why Python + Streamlit + CSV?

The project was built as a 24-hour prototype. Python was already a familiar language, Streamlit provides a quick interactive interface, and CSV keeps the collected records transparent and easy to inspect.

A React + Node.js architecture could be considered later if fieldwork shows a real need for multiple users, authentication, concurrent updates or a deployed public service. It was not necessary to demonstrate the first matching workflow.

## 6. What was intentionally left out?

- Login and account management
- Live GPS, maps and background location tracking
- Chat, push notifications and automatic dispatch
- Payments or collection of money
- AI image recognition or hunger detection
- Veterinary advice or food recommendations
- Automatic reservation of an offer
- Automatic marking of a delivery as completed
- Combining multiple partial offers

These omissions keep the prototype explainable and avoid implying capabilities it does not have.

## 7. What should be tested?

- Valid compatible records produce a suggestion.
- Different areas do not match.
- Different food categories or units do not match.
- Expired offers do not match.
- An unavailable volunteer does not match.
- An overdue point is flagged using the configured interval.
- Invalid quantities and malformed timestamps are rejected.
- Duplicate record IDs are rejected.

## 8. What should improve after fieldwork?

The next version should be driven by the feeder's feedback. Possible changes include simplifying data entry, using the feeder's actual area names, changing the reminder interval, adding a manual confirmation field, or removing a feature that does not solve a real problem.

Do not add GPS, notifications, accounts or AI merely to make the project look more advanced. Add a feature only when the person using the tool needs it and the 24-hour scope permits a safe implementation.

## Outcome

The first MVP is a local coordination dashboard with transparent rule-based suggestions and reminders. It supports human coordination; it does not replace it.
